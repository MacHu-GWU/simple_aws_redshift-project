# -*- coding: utf-8 -*-

import datetime
from simple_aws_redshift.model_redshift_data_api import (
    DescribeStatementResponse,
    GetStatementResultResponse,
)
from simple_aws_redshift.tests.test_property_helpers import verify_all_properties

from rich import print as rprint


class TestDescribeStatementResponse:
    def test(self):
        raw_data = {
            "status": "FINISHED",
        }
        response = DescribeStatementResponse(raw_data=raw_data)
        verify_all_properties(DescribeStatementResponse, response)

        rprint(f"{response.is_aborted = }")
        rprint(f"{response.is_all = }")
        rprint(f"{response.is_failed = }")
        rprint(f"{response.is_finished = }")
        rprint(f"{response.is_picked = }")
        rprint(f"{response.is_started = }")
        rprint(f"{response.is_submitted = }")


class TestStatementResult:
    def test(self):
        raw_data = {
            "ColumnMetadata": [
                {
                    "isCaseSensitive": True,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_string",
                    "length": 0,
                    "name": "test_string",
                    "nullable": 1,
                    "precision": 11,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "varchar",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_integer",
                    "length": 0,
                    "name": "test_integer",
                    "nullable": 1,
                    "precision": 10,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "int4",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_float",
                    "length": 0,
                    "name": "test_float",
                    "nullable": 1,
                    "precision": 6,
                    "scale": 5,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "numeric",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_boolean",
                    "length": 0,
                    "name": "test_boolean",
                    "nullable": 1,
                    "precision": 1,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "bool",
                },
                {
                    "isCaseSensitive": True,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_null",
                    "length": 0,
                    "name": "test_null",
                    "nullable": 1,
                    "precision": 65535,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "varchar",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_double",
                    "length": 0,
                    "name": "test_double",
                    "nullable": 1,
                    "precision": 8,
                    "scale": 8,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "float4",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_long",
                    "length": 0,
                    "name": "test_long",
                    "nullable": 1,
                    "precision": 19,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "int8",
                },
                {
                    "isCaseSensitive": True,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_blob",
                    "length": 0,
                    "name": "test_blob",
                    "nullable": 1,
                    "precision": 64000,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "varbyte",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_date",
                    "length": 0,
                    "name": "test_date",
                    "nullable": 1,
                    "precision": 13,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "date",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_timestamp",
                    "length": 0,
                    "name": "test_timestamp",
                    "nullable": 1,
                    "precision": 29,
                    "scale": 6,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "timestamp",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_timestamptz",
                    "length": 0,
                    "name": "test_timestamptz",
                    "nullable": 1,
                    "precision": 35,
                    "scale": 6,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "timestamptz",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": False,
                    "label": "test_time",
                    "length": 0,
                    "name": "test_time",
                    "nullable": 1,
                    "precision": 15,
                    "scale": 6,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "time",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_decimal",
                    "length": 0,
                    "name": "test_decimal",
                    "nullable": 1,
                    "precision": 10,
                    "scale": 2,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "numeric",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_numeric",
                    "length": 0,
                    "name": "test_numeric",
                    "nullable": 1,
                    "precision": 10,
                    "scale": 2,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "numeric",
                },
                {
                    "isCaseSensitive": False,
                    "isCurrency": False,
                    "isSigned": True,
                    "label": "test_smallint",
                    "length": 0,
                    "name": "test_smallint",
                    "nullable": 1,
                    "precision": 5,
                    "scale": 0,
                    "schemaName": "",
                    "tableName": "",
                    "typeName": "int2",
                },
            ],
            "Records": [
                [
                    {"stringValue": "Hello World"},
                    {"longValue": 42},
                    {"stringValue": "3.14159"},
                    {"booleanValue": True},
                    {"isNull": True},
                    {"doubleValue": 123.456787109375},
                    {"longValue": 9223372036854775807},
                    {"stringValue": "YWJj"},
                    {"stringValue": "2024-06-12"},
                    {"stringValue": "2024-06-12 14:30:45.123456"},
                    {"stringValue": "2024-06-12 19:30:45.123456+00"},
                    {"stringValue": "14:30:45"},
                    {"stringValue": "123.45"},
                    {"stringValue": "123.45"},
                    {"longValue": 32767},
                ]
            ],
            "TotalNumRows": 1,
        }
        statement_result = GetStatementResultResponse(raw_data=raw_data)
        verify_all_properties(GetStatementResultResponse, statement_result)

        data = statement_result.to_column_oriented_data()
        rprint(data)
        expected_data = {
            "test_string": ["Hello World"],
            "test_integer": [42],
            "test_float": ["3.14159"],
            "test_boolean": [True],
            "test_null": [None],
            "test_double": [123.456787109375],
            "test_long": [9223372036854775807],
            "test_blob": [b"abc"],
            "test_date": [datetime.date(2024, 6, 12)],
            "test_timestamp": [datetime.datetime(2024, 6, 12, 14, 30, 45, 123456)],
            "test_timestamptz": [
                datetime.datetime(
                    2024, 6, 12, 19, 30, 45, 123456, tzinfo=datetime.timezone.utc
                )
            ],
            "test_time": [datetime.time(14, 30, 45)],
            "test_decimal": ["123.45"],
            "test_numeric": ["123.45"],
            "test_smallint": [32767],
        }
        assert data == expected_data


if __name__ == "__main__":
    from simple_aws_redshift.tests import run_cov_test

    run_cov_test(
        __file__,
        "simple_aws_redshift.model_redshift_data_api.py",
        preview=False,
    )
