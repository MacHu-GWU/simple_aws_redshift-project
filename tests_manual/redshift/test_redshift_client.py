# -*- coding: utf-8 -*-

from simple_aws_redshift.tests.settings import settings
from simple_aws_redshift.redshift.client import (
    list_redshift_clusters,
    get_redshift_cluster,
)

from simple_aws_redshift.tests.bsm import bsm

from rich import print as rprint


def test_list_redshift_clusters():
    redshift_clusters = list_redshift_clusters(bsm.redshift_client)
    rprint(redshift_clusters.all())


def test_get_redshift_cluster():
    redshift_cluster = get_redshift_cluster(
        redshift_client=bsm.redshift_client,
        cluster_identifier="invalid-cluster",
    )
    assert redshift_cluster is None


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.redshift.client.py",
        preview=False,
    )
