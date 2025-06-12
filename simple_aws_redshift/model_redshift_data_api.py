# -*- coding: utf-8 -*-

"""
Redshift Serverless Data Models.
"""

import typing as T
import enum
import base64
import dataclasses
from datetime import date, time, datetime, timezone

from func_args.api import T_KWARGS, REQ
from iterproxy import IterProxy

from .model import Base

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_data.type_defs import (
        GetStatementResultResponseTypeDef,
        ColumnMetadataTypeDef,
        FieldTypeDef,
    )


class RedshiftDataType(str, enum.Enum):
    """Enumeration of Redshift data types as returned by the Data API"""

    # String types
    VARCHAR = "varchar"
    CHAR = "char"
    TEXT = "text"

    # Integer types
    INT2 = "int2"  # SMALLINT
    INT4 = "int4"  # INTEGER
    INT8 = "int8"  # BIGINT

    # Floating point types
    FLOAT4 = "float4"  # REAL
    FLOAT8 = "float8"  # DOUBLE PRECISION

    # Numeric/Decimal types
    NUMERIC = "numeric"
    DECIMAL = "decimal"

    # Boolean type
    BOOL = "bool"

    # Date/Time types
    DATE = "date"
    TIME = "time"
    TIMESTAMP = "timestamp"
    TIMESTAMPTZ = "timestamptz"

    # Binary types
    VARBYTE = "varbyte"

    # Other types that might be encountered
    UUID = "uuid"
    JSON = "json"
    JSONB = "jsonb"


type_to_field_mapping = {
    RedshiftDataType.BOOL.value: "booleanValue",
    RedshiftDataType.CHAR.value: "stringValue",
    RedshiftDataType.DATE.value: "stringValue",
    RedshiftDataType.DECIMAL.value: "doubleValue",
    RedshiftDataType.FLOAT4.value: "doubleValue",
    RedshiftDataType.FLOAT8.value: "doubleValue",
    RedshiftDataType.INT2.value: "longValue",
    RedshiftDataType.INT4.value: "longValue",
    RedshiftDataType.INT8.value: "longValue",
    RedshiftDataType.JSON.value: "stringValue",
    RedshiftDataType.JSONB.value: "stringValue",
    RedshiftDataType.NUMERIC.value: "stringValue",
    RedshiftDataType.TEXT.value: "stringValue",
    RedshiftDataType.TIME.value: "stringValue",
    RedshiftDataType.TIMESTAMP.value: "stringValue",
    RedshiftDataType.TIMESTAMPTZ.value: "stringValue",
    RedshiftDataType.UUID.value: "stringValue",
    RedshiftDataType.VARBYTE.value: "stringValue",
    RedshiftDataType.VARCHAR.value: "stringValue",
}


def extract_field_value(
    column_metadata: "ColumnMetadataTypeDef",
    field: "FieldTypeDef",
) -> T.Any:
    type_name = column_metadata["typeName"]
    key = type_to_field_mapping[type_name]
    try:
        raw_value = field[key]
    except KeyError:
        if field.get("isNull", False):
            return None
        else:  # pragma: no cover
            return None
    if type_name in [
        RedshiftDataType.TIMESTAMP.value,
        RedshiftDataType.TIMESTAMPTZ.value,
    ]:
        return datetime.fromisoformat(raw_value)
    elif type_name == RedshiftDataType.DATE.value:
        return date.fromisoformat(raw_value)
    elif type_name == RedshiftDataType.TIME.value:
        return time.fromisoformat(raw_value)
    elif type_name == RedshiftDataType.VARBYTE.value:
        return base64.b64decode(raw_value)
    else:
        return raw_value


@dataclasses.dataclass
class StatementResult(Base):
    """
    Ref:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResult.html
    """

    raw_data: "GetStatementResultResponseTypeDef" = dataclasses.field(default=REQ)

    @property
    def column_metadata(self) -> list["ColumnMetadataTypeDef"]:
        return self.raw_data.get("ColumnMetadata", [])

    @property
    def records(self) -> list[list["FieldTypeDef"]]:
        return self.raw_data.get("Records", [])

    @property
    def core_data(self) -> T_KWARGS:
        return {
            "column_metadata": self.column_metadata,
            "records": self.records,
        }

    def to_column_oriented_data(self) -> dict[str, list[T.Any]]:
        """
        Convert the records to a column-oriented format.
        """
        data = {column_metadata["name"]: [] for column_metadata in self.column_metadata}
        for record in self.records:
            for column_meta, field in zip(self.column_metadata, record):
                value = extract_field_value(column_meta, field)
                data[column_meta["name"]].append(value)
        return data


class StatementResultIterProxy(IterProxy[StatementResult]):
    pass
