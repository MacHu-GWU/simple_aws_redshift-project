# -*- coding: utf-8 -*-

from simple_aws_redshift.redshift.model import (
    RedshiftCluster,
)

from simple_aws_redshift.tests.test_property_helpers import verify_all_properties

from rich import print as rprint


class TestRedshiftCluster:
    def test(self):
        raw_data = {}
        redshift_cluster = RedshiftCluster(raw_data=raw_data)
        verify_all_properties(RedshiftCluster, redshift_cluster)

        _ = redshift_cluster.endpoint_address
        _ = redshift_cluster.endpoint_port


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.redshift.model.py",
        preview=False,
    )
