# -*- coding: utf-8 -*-

from simple_aws_redshift import api


def test():
    _ = api

    _ = api.RedshiftServerlessConnectionParams

    _ = api.redshift_serverless.RedshiftServerlessNamespace
    _ = api.redshift_serverless.RedshiftServerlessNamespaceIterProxy
    _ = api.redshift_serverless.RedshiftServerlessWorkgroup
    _ = api.redshift_serverless.RedshiftServerlessWorkgroupIterProxy
    _ = api.redshift_serverless.list_namespaces
    _ = api.redshift_serverless.get_namespace
    _ = api.redshift_serverless.delete_namespace
    _ = api.redshift_serverless.list_workgroups
    _ = api.redshift_serverless.get_workgroup
    _ = api.redshift_serverless.delete_workgroup

    _ = api.redshift_data_api.DescribeStatementResponse
    _ = api.redshift_data_api.RedshiftDataType
    _ = api.redshift_data_api.type_to_field_mapping
    _ = api.redshift_data_api.extract_field_raw_value
    _ = api.redshift_data_api.extract_field_python_native_value
    _ = api.redshift_data_api.GetStatementResultResponse
    _ = api.redshift_data_api.GetStatementResultResponseIterProxy
    _ = api.redshift_data_api.RunSqlResult
    _ = api.redshift_data_api.run_sql
    _ = api.redshift_data_api.get_statement_result


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.api",
        preview=False,
    )
