# -*- coding: utf-8 -*-

from simple_aws_redshift.redshift_serverless.model import (
    RedshiftServerlessNamespace,
    RedshiftServerlessWorkgroup,
)


from simple_aws_redshift.tests.test_property_helpers import verify_all_properties

from rich import print as rprint


class TestRedshiftServerlessNamespace:
    def test(self):
        raw_data = {
            "status": "AVAILABLE",
        }
        namespace = RedshiftServerlessNamespace(raw_data=raw_data)
        verify_all_properties(RedshiftServerlessNamespace, namespace)

        rprint(f"{namespace.is_available = }")
        rprint(f"{namespace.is_modifying = }")
        rprint(f"{namespace.is_deleting = }")


class TestRedshiftServerlessWorkgroup:
    def test(self):
        raw_data = {
            "status": "AVAILABLE",
            "endpoint": {
                "address": "example-redshift-serverless-endpoint",
                "port": 5439,
            },
        }
        workgroup = RedshiftServerlessWorkgroup(raw_data=raw_data)
        verify_all_properties(RedshiftServerlessWorkgroup, workgroup)

        rprint(f"{workgroup.is_available = }")
        rprint(f"{workgroup.is_creating = }")
        rprint(f"{workgroup.is_modifying = }")
        rprint(f"{workgroup.is_deleting = }")
        rprint(f"{workgroup.endpoint_address = }")
        rprint(f"{workgroup.endpoint_port = }")


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.redshift_serverless.model.py",
        preview=False,
    )
