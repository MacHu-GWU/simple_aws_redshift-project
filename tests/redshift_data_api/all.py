# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.redshift_data_api",
        is_folder=True,
        preview=False,
    )
