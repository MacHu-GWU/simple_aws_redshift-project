# -*- coding: utf-8 -*-

from simple_aws_redshift.model_redshift_serverless import RedshiftServerlessNamespace

from simple_aws_redshift.tests.bsm import bsm
from simple_aws_redshift.tests.test_property_helpers import verify_all_properties

from rich import print as rprint


class TestRedshiftServerlessNamespace:
    def test(self):
        res = bsm.redshiftserverless_client.list_namespaces()
        namespaces = [
            RedshiftServerlessNamespace(raw_data=dct)
            for dct in res.get("namespaces", [])
        ]
        namespace = namespaces[0]
        verify_all_properties(RedshiftServerlessNamespace, namespace)

        rprint(f"{namespace.is_available = }")
        rprint(f"{namespace.is_modifying = }")
        rprint(f"{namespace.is_deleting = }")


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.model_redshift_serverless.py",
        preview=False,
    )
