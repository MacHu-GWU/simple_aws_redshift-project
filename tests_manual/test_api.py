# -*- coding: utf-8 -*-

from simple_aws_redshift import api


def test():
    _ = api
    _ = api.RedshiftServerlessNamespace
    _ = api.RedshiftServerlessNamespaceIterProxy
    _ = api.list_namespaces
    _ = api.get_namespace


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.api",
        preview=False,
    )
