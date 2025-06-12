# -*- coding: utf-8 -*-

import textwrap
from simple_aws_redshift.client_redshift_data_api import (
    run_sql,
)
from simple_aws_redshift.tests.settings import settings

from simple_aws_redshift.tests.bsm import bsm

from rich import print as rprint


def test_run_sql():
    sql = "SELECT 1;"
    sql = textwrap.dedent(
        """
    SELECT 
    -- String/VARCHAR
    'Hello World' AS test_string,
    -- Integer (INT4)
    42 AS test_integer,
    -- Float/REAL
    3.14159 AS test_float,
    -- Boolean
    TRUE AS test_boolean,
    -- NULL value
    NULL AS test_null,
    -- Double precision (FLOAT8/DOUBLE PRECISION)
    CAST(123.456789012345 AS REAL) AS test_double,
    -- Long integer (BIGINT/INT8) 
    CAST(9223372036854775807 AS BIGINT) AS test_long,
    -- BLOB/BYTEA (binary data)
    'abc'::VARBYTE AS test_blob,
    -- Date types
    CAST('2024-06-12' AS DATE) AS test_date,
    -- Timestamp without timezone
    CAST('2024-06-12 14:30:45.123456' AS TIMESTAMP) AS test_timestamp,
    -- Timestamp with timezone (TIMESTAMPTZ)
    CAST('2024-06-12 14:30:45.123456-05:00' AS TIMESTAMPTZ) AS test_timestamptz,
    -- Time
    CAST('14:30:45' AS TIME) AS test_time,
    -- Additional numeric types for completeness
    CAST(123.45 AS DECIMAL(10,2)) AS test_decimal,
    CAST(123.45 AS NUMERIC(10,2)) AS test_numeric,
    -- Small integer
    CAST(32767 AS SMALLINT) AS test_smallint
    ;
    """
    ).strip()
    run_sql_result = run_sql(
        redshift_data_api_client=bsm.redshiftdataapiservice_client,
        sql=sql,
        database=settings.db_name,
        workgroup_name=settings.workgroup_name,
        result_format="JSON",
        verbose=True,
    )
    # rprint(result)

    for statement_result in run_sql_result.statement_result_list:
        rprint(statement_result.raw_data)
    #     rprint(statement_result.column_metadata)
    #     for record in statement_result.records:
    #         rprint(record)


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.client_redshift_data_api.py",
        preview=False,
    )
