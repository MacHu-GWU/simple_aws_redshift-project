# -*- coding: utf-8 -*-

from simple_aws_redshift import api


def test():
    _ = api
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


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.api",
        preview=False,
    )
