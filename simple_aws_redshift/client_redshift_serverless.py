# -*- coding: utf-8 -*-

import typing as T

import botocore.exceptions

from .model_redshift_serverless import (
    RedshiftServerlessNamespace,
    RedshiftServerlessNamespaceIterProxy,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_serverless.client import RedshiftServerlessClient


def list_namespaces(
    redshift_serverless_client: "RedshiftServerlessClient",
    page_size: int = 100,
    max_items: int = 9999,
) -> RedshiftServerlessNamespaceIterProxy:
    """
    Ref:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListNamespaces.html
    """

    def func():
        paginator = redshift_serverless_client.get_paginator("list_namespaces")
        response_iterator = paginator.paginate(
            PaginationConfig={
                "MaxItems": max_items,
                "PageSize": page_size,
            }
        )
        for response in response_iterator:
            for dct in response.get("namespaces", []):
                yield RedshiftServerlessNamespace(_data=dct)

    return RedshiftServerlessNamespaceIterProxy(func())


def get_namespace(
    redshift_serverless_client: "RedshiftServerlessClient",
    namespace_name: str,
) -> T.Optional[RedshiftServerlessNamespace]:
    """
    Ref:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_namespace.html
    """
    try:
        response = redshift_serverless_client.get_namespace(
            namespaceName=namespace_name
        )
        return RedshiftServerlessNamespace(_data=response["namespace"])
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            return None
        else:  # pragma: no cover
            raise
