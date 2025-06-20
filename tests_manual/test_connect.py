# -*- coding: utf-8 -*-

from simple_aws_redshift.connect import (
    RedshiftClusterConnectionParams,
    RedshiftServerlessConnectionParams,
)
from simple_aws_redshift.tests.settings import get_settings, run_test_sql

from rich import print as rprint


class TestRedshiftServerlessConnectionParams:
    def test_with_redshift_connector(self):
        settings = get_settings()  # don't use singleton settings in tests
        params = RedshiftServerlessConnectionParams.new(
            redshift_serverless_client=settings.bsm.redshiftserverless_client,
            namespace_name=settings.namespace_name,
            workgroup_name=settings.workgroup_name,
        )
        conn = params.get_connection()
        run_test_sql(conn)

    def test_with_sqlalchemy_engine(self):
        settings = get_settings()
        params = RedshiftServerlessConnectionParams.new(
            redshift_serverless_client=settings.bsm.redshiftserverless_client,
            namespace_name=settings.namespace_name,
            workgroup_name=settings.workgroup_name,
        )
        engine = params.get_engine()
        run_test_sql(engine)


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.connect.py",
        preview=False,
    )
