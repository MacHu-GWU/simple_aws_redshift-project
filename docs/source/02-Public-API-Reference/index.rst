Public API Reference
===============================================================================
This page provides a curated list of all public APIs available in the ``simple_aws_redshift`` package. Click on any item to jump to its detailed documentation.


Connection Management
-------------------------------------------------------------------------------
- :class:`simple_aws_redshift.api.RedshiftServerlessConnectionParams <simple_aws_redshift.connect.RedshiftServerlessConnectionParams>`

Redshift APIs
-------------------------------------------------------------------------------

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift.RedshiftCluster <simple_aws_redshift.model_redshift_serverless.RedshiftCluster>`
- :class:`simple_aws_redshift.api.redshift.RedshiftClusterIterProxy <simple_aws_redshift.model_redshift_serverless.RedshiftClusterIterProxy>`

Client Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift.list_redshift_clusters <simple_aws_redshift.client_redshift_serverless.list_redshift_clusters>`
- :func:`simple_aws_redshift.api.redshift.get_redshift_cluster <simple_aws_redshift.client_redshift_serverless.get_redshift_cluster>`

Redshift Serverless APIs
-------------------------------------------------------------------------------

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespace <simple_aws_redshift.model_redshift_serverless.RedshiftServerlessNamespace>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespaceIterProxy <simple_aws_redshift.model_redshift_serverless.RedshiftServerlessNamespaceIterProxy>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroup <simple_aws_redshift.model_redshift_serverless.RedshiftServerlessWorkgroup>`
- :class:`simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroupIterProxy <simple_aws_redshift.model_redshift_serverless.RedshiftServerlessWorkgroupIterProxy>`

Client Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift_serverless.list_namespaces <simple_aws_redshift.client_redshift_serverless.list_namespaces>`
- :func:`simple_aws_redshift.api.redshift_serverless.get_namespace <simple_aws_redshift.client_redshift_serverless.get_namespace>`
- :func:`simple_aws_redshift.api.redshift_serverless.delete_namespace <simple_aws_redshift.client_redshift_serverless.delete_namespace>`
- :func:`simple_aws_redshift.api.redshift_serverless.list_workgroups <simple_aws_redshift.client_redshift_serverless.list_workgroups>`
- :func:`simple_aws_redshift.api.redshift_serverless.get_workgroup <simple_aws_redshift.client_redshift_serverless.get_workgroup>`
- :func:`simple_aws_redshift.api.redshift_serverless.delete_workgroup <simple_aws_redshift.client_redshift_serverless.delete_workgroup>`


Redshift Data API
-------------------------------------------------------------------------------

High-Level Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :func:`simple_aws_redshift.api.redshift_data_api.run_sql <simple_aws_redshift.client_redshift_data_api.run_sql>`
- :func:`simple_aws_redshift.api.redshift_data_api.get_statement_result <simple_aws_redshift.client_redshift_data_api.get_statement_result>`

Data Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_data_api.RunSqlResult <simple_aws_redshift.client_redshift_data_api.RunSqlResult>`
- :class:`simple_aws_redshift.api.redshift_data_api.DescribeStatementResponse <simple_aws_redshift.model_redshift_data_api.DescribeStatementResponse>`
- :class:`simple_aws_redshift.api.redshift_data_api.GetStatementResultResponse <simple_aws_redshift.model_redshift_data_api.GetStatementResultResponse>`
- :class:`simple_aws_redshift.api.redshift_data_api.GetStatementResultResponseIterProxy <simple_aws_redshift.model_redshift_data_api.GetStatementResultResponseIterProxy>`

Data Type Utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :class:`simple_aws_redshift.api.redshift_data_api.RedshiftDataType <simple_aws_redshift.model_redshift_data_api.RedshiftDataType>`
- :func:`simple_aws_redshift.api.redshift_data_api.type_to_field_mapping <simple_aws_redshift.model_redshift_data_api.type_to_field_mapping>`
- :func:`simple_aws_redshift.api.redshift_data_api.extract_field_raw_value <simple_aws_redshift.model_redshift_data_api.extract_field_raw_value>`
- :func:`simple_aws_redshift.api.redshift_data_api.extract_field_python_native_value <simple_aws_redshift.model_redshift_data_api.extract_field_python_native_value>`
