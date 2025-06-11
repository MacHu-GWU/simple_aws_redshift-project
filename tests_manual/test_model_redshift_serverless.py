# -*- coding: utf-8 -*-

from simple_aws_redshift.model_redshift_serverless import RedshiftServerlessNamespace

from simple_aws_redshift.tests.bsm import bsm

from rich import print as rprint


class TestRedshiftServerlessNamespace:
    def test(self):
        res = bsm.redshiftserverless_client.list_namespaces()
        namespaces = [
            RedshiftServerlessNamespace(_data=dct) for dct in res.get("namespaces", [])
        ]
        namespace = namespaces[0]

        print(f"{namespace.admin_password_secret_arn = }")
        print(f"{namespace.admin_password_secret_kms_key_id = }")
        print(f"{namespace.admin_username = }")
        print(f"{namespace.creation_date = }")
        print(f"{namespace.db_name = }")
        print(f"{namespace.default_iam_role_arn = }")
        print(f"{namespace.iam_roles = }")
        print(f"{namespace.kms_key_id = }")
        print(f"{namespace.log_exports = }")
        print(f"{namespace.namespace_arn = }")
        print(f"{namespace.namespace_id = }")
        print(f"{namespace.namespace_name = }")
        print(f"{namespace.status = }")
        rprint(f"{namespace.core_data = }")

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
