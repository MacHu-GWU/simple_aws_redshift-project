# -*- coding: utf-8 -*-

from simple_aws_redshift.client_redshift_serverless import (
    list_namespaces,
    get_namespace,
    list_workgroups,
    get_workgroup,
)

from simple_aws_redshift.tests.bsm import bsm

from rich import print as rprint


def test_list_namespaces():
    namespaces = list_namespaces(bsm.redshiftserverless_client)
    rprint(namespaces.one())


def test_get_namespace():
    namespace = get_namespace(
        redshift_serverless_client=bsm.redshiftserverless_client,
        namespace_name="invalid-namespace",
    )
    assert namespace is None

    namespace = get_namespace(
        redshift_serverless_client=bsm.redshiftserverless_client,
        namespace_name="my-ohmy-sql-dev",
    )
    rprint(namespace)


def test_list_workgroups():
    workgroups = list_workgroups(bsm.redshiftserverless_client)
    rprint(workgroups.one())


def test_get_workgroup():
    workgroup = get_workgroup(
        redshift_serverless_client=bsm.redshiftserverless_client,
        workgroup_name="invalid-workgroup",
    )
    assert workgroup is None

    workgroup = get_workgroup(
        redshift_serverless_client=bsm.redshiftserverless_client,
        workgroup_name="my-ohmy-sql-dev",
    )
    rprint(workgroup)


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.client_redshift_serverless.py",
        preview=False,
    )
