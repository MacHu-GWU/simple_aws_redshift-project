Public API Reference
===============================================================================
This page provides a curated list of all public APIs available in the ``simple_aws_redshift`` package. Click on any item to jump to its detailed documentation.


Connection Management
-------------------------------------------------------------------------------
- :class:`simple_aws_redshift.api.RedshiftClusterConnectionParams <simple_aws_redshift.connect.RedshiftClusterConnectionParams>`
- :class:`simple_aws_redshift.api.RedshiftServerlessConnectionParams <simple_aws_redshift.connect.RedshiftServerlessConnectionParams>`

Redshift APIs
-------------------------------------------------------------------------------

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift.RedshiftCluster <simple_aws_redshift.redshift.model.RedshiftCluster>`
- :class:`simple_aws_redshift.api.redshift.RedshiftClusterIterProxy <simple_aws_redshift.redshift.model.RedshiftClusterIterProxy>`

Client Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift.list_redshift_clusters <simple_aws_redshift.redshift.client.list_redshift_clusters>`
- :func:`simple_aws_redshift.api.redshift.get_redshift_cluster <simple_aws_redshift.redshift.client.get_redshift_cluster>`

Redshift Serverless APIs
-------------------------------------------------------------------------------

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespace <simple_aws_redshift.redshift_serverless.model.RedshiftServerlessNamespace>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespaceIterProxy <simple_aws_redshift.redshift_serverless.model.RedshiftServerlessNamespaceIterProxy>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroup <simple_aws_redshift.redshift_serverless.model.RedshiftServerlessWorkgroup>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroupIterProxy <simple_aws_redshift.redshift_serverless.model.RedshiftServerlessWorkgroupIterProxy>`

Client Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift_serverless.list_namespaces <simple_aws_redshift.redshift_serverless.client.list_namespaces>`
- :func:`simple_aws_redshift.api.redshift_serverless.get_namespace <simple_aws_redshift.redshift_serverless.client.get_namespace>`
- :func:`simple_aws_redshift.api.redshift_serverless.delete_namespace <simple_aws_redshift.redshift_serverless.client.delete_namespace>`
- :func:`simple_aws_redshift.api.redshift_serverless.list_workgroups <simple_aws_redshift.redshift_serverless.client.list_workgroups>`
- :func:`simple_aws_redshift.api.redshift_serverless.get_workgroup <simple_aws_redshift.redshift_serverless.client.get_workgroup>`
- :func:`simple_aws_redshift.api.redshift_serverless.delete_workgroup <simple_aws_redshift.redshift_serverless.client.delete_workgroup>`


Redshift Data API
-------------------------------------------------------------------------------

High-Level Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift_data_api.run_sql <simple_aws_redshift.redshift_data_api.client.run_sql>`
- :func:`simple_aws_redshift.api.redshift_data_api.get_statement_result <simple_aws_redshift.redshift_data_api.client.get_statement_result>`
- :func:`simple_aws_redshift.api.redshift_data_api.SqlCommandKeyEnum <simple_aws_redshift.redshift_data_api.client.SqlCommandKeyEnum>`
- :func:`simple_aws_redshift.api.redshift_data_api.SqlCommand <simple_aws_redshift.redshift_data_api.client.SqlCommand>`

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_data_api.RunSqlResult <simple_aws_redshift.redshift_data_api.client.RunSqlResult>`
- :class:`simple_aws_redshift.api.redshift_data_api.DescribeStatementResponse <simple_aws_redshift.redshift_data_api.model.DescribeStatementResponse>`
- :class:`simple_aws_redshift.api.redshift_data_api.GetStatementResultResponse <simple_aws_redshift.redshift_data_api.model.GetStatementResultResponse>`
- :class:`simple_aws_redshift.api.redshift_data_api.GetStatementResultResponseIterProxy <simple_aws_redshift.redshift_data_api.model.GetStatementResultResponseIterProxy>`
- :class:`simple_aws_redshift.api.redshift_data_api.VirtualDataFrame <simple_aws_redshift.redshift_data_api.model.VirtualDataFrame>`
- :class:`simple_aws_redshift.api.redshift_data_api.ConsolidatedStatementResult <simple_aws_redshift.redshift_data_api.model.ConsolidatedStatementResult>`

Data Type Utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_data_api.RedshiftDataType <simple_aws_redshift.redshift_data_api.model.RedshiftDataType>`
- :func:`simple_aws_redshift.api.redshift_data_api.type_to_field_mapping <simple_aws_redshift.redshift_data_api.model.type_to_field_mapping>`
- :func:`simple_aws_redshift.api.redshift_data_api.extract_field_raw_value <simple_aws_redshift.redshift_data_api.model.extract_field_raw_value>`
- :func:`simple_aws_redshift.api.redshift_data_api.extract_field_python_native_value <simple_aws_redshift.redshift_data_api.model.extract_field_python_native_value>`
