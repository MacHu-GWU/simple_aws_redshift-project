# -*- coding: utf-8 -*-

"""
Improve the original redshift data api boto3 API.

Ref:

- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html
"""

import dataclasses
import typing as T

import botocore.exceptions
from func_args.api import REQ, OPT, remove_optional, BaseModel

from .vendor.waiter import Waiter

from .model_redshift_data_api import (
    DescribeStatementResponse,
    GetStatementResultResponse,
    GetStatementResultResponseIterProxy,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient
    from mypy_boto3_redshift_data.literals import ResultFormatStringType
    from mypy_boto3_redshift_data.type_defs import (
        ExecuteStatementOutputTypeDef,
        GetStatementResultResponseTypeDef,
    )


@dataclasses.dataclass
class RunSqlResult(BaseModel):
    """
    Result of running a SQL statement using the Redshift Data API.

    :param execute_statement_response: Response from the `execute_statement` API call.
    :param describe_statement_response: Response from the `describe_statement` API call.
    """

    # fmt: off
    execute_statement_response: "ExecuteStatementOutputTypeDef" = dataclasses.field(default=REQ)
    describe_statement_response: "DescribeStatementResponse" = dataclasses.field(default=REQ)
    # fmt: on

    @property
    def execution_id(self) -> str:
        """
        Get the execution ID of the SQL statement. This ID can be used to
        retrieve the results of the SQL execution using the `get_statement_result` API.
        """
        return self.execute_statement_response["Id"]


def run_sql(
    redshift_data_api_client: "RedshiftDataAPIServiceClient",
    sql: str,
    client_token: str = OPT,
    cluster_identifier: str = OPT,
    database: str = OPT,
    db_user: str = OPT,
    parameters: dict[str, T.Any] = OPT,
    result_format: "ResultFormatStringType" = OPT,
    secret_arn: str = OPT,
    session_id: str = OPT,
    session_keep_alive_seconds: int = OPT,
    statement_name: str = OPT,
    with_event: bool = OPT,
    workgroup_name: str = OPT,
    delay: int = 1,
    timeout: int = 10,
    verbose: bool = False,
):
    """
    Run redshift SQL statement using Data API and get the results. It will
    run ``execute_statement`` API to run the SQL asynchronously, then do a
    long polling to check the status of the SQL execution using``describe_statement``
    API. Once the SQL execution is finished, it will run ``get_statement_result``
    API to get the result.

    In other words, this function is a human-friendly wrapper of the Data API.

    :param rs_data_client: boto3.client("redshift-data") object
    :param database: database name.
    :param sql: SQL statement you want to execute.
    :param cluster_id: cluster id. this is for Redshift provisioned cluster only.
    :param workgroup_name: workgroup name. this is for Redshift serverless only.
    :param statement_name: statement name. a human-friendly name you want to give
        to this SQL statement.
    :param delay: how many seconds to wait between each long polling.
    :param timeout: how many seconds to wait before timeout.
    :param max_items: maximum number of items to return (not 100% sure what
        the "items" refers to, I guess it refers to rows).
    :param no_result: some SQL statement doesn't return any result, for
        example, ``CREATE TABLE``, ``DELETE TABLE``. If this is True,
        then it will only wait the status to reach FINISHED, but won't run
        ``get_statement_result`` API.

    Reference:

    - execute_statement: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/execute_statement.html
    - describe_statement: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/describe_statement.html
    - get_statement_result: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_statement_result.html

    :return:
    """
    # --- execute_statement
    # process arguments
    kwargs = dict(
        Sql=sql,
        ClientToken=client_token,
        ClusterIdentifier=cluster_identifier,
        Database=database,
        DbUser=db_user,
        Parameters=parameters,
        ResultFormat=result_format,
        SecretArn=secret_arn,
        SessionId=session_id,
        SessionKeepAliveSeconds=session_keep_alive_seconds,
        StatementName=statement_name,
        WithEvent=with_event,
        WorkgroupName=workgroup_name,
    )
    execute_statement_response = redshift_data_api_client.execute_statement(
        **remove_optional(**kwargs)
    )
    id = execute_statement_response["Id"]

    # --- describe_statement
    # wait for the status to reach FINISHED
    describe_statement_response = None
    for _ in Waiter(delays=delay, timeout=timeout, verbose=verbose):
        try:
            response = redshift_data_api_client.describe_statement(Id=id)
            describe_statement_response = DescribeStatementResponse(raw_data=response)
            # 'SUBMITTED'|'PICKED'|'STARTED'|'FINISHED'|'ABORTED'|'FAILED'|'ALL'
            status = describe_statement_response.status
            if status == "FINISHED":
                break
            # still pending
            elif status in ["SUBMITTED", "PICKED", "STARTED"]:
                continue
            # raise exception when failed
            elif status == "FAILED":
                raise RuntimeError(
                    "FAILED! error: {}".format(describe_statement_response.error)
                )
            elif status == "ABORTED":
                raise RuntimeError("ABORTED!")
            else:  # pragma: no cover
                raise NotImplementedError
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                continue
            else:  # pragma: no cover
                raise e
    run_sql_result = RunSqlResult(
        execute_statement_response=execute_statement_response,
        describe_statement_response=describe_statement_response,
    )
    return run_sql_result


def get_statement_result(
    redshift_data_api_client: "RedshiftDataAPIServiceClient",
    id: str,
    max_items: int = 1000,
) -> GetStatementResultResponseIterProxy:
    """
    Ref:

    - get_statement_result: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_statement_result.html
    - GetStatementResult: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResult.html
    """

    def func():
        paginator = redshift_data_api_client.get_paginator("get_statement_result")
        response_iterator = paginator.paginate(
            Id=id,
            PaginationConfig=dict(
                MaxItems=max_items,
            ),
        )
        get_statement_result_response: GetStatementResultResponseTypeDef
        for get_statement_result_response in response_iterator:
            statement_result = GetStatementResultResponse(
                raw_data=get_statement_result_response
            )
            yield statement_result

    return GetStatementResultResponseIterProxy(func())
