.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.4.1 (2025-09-09)
------------------------------------------------------------------------------
**Features and Improvements**

- Add ``SqlCommand`` class implementing Command pattern for Redshift Data API workflow management:
    - ``simple_aws_redshift.api.redshift_data_api.SqlCommand`` - encapsulates SQL execution parameters and provides both automatic (``run()``) and manual workflow control
    - Replaces deprecated ``run_sql()`` function with better error handling and more intuitive API
    - Supports both JSON and CSV result formats
    - Provides consolidated result access and iterator proxy for streaming large result sets

**Minor Improvements**

- Add lazy imports system for better performance and reduced memory footprint
- Add ``soft-deps`` as core dependency for better optional dependency management
- Improve Redshift Data API documentation with updated examples and notebooks
- Add deprecation warnings for ``run_sql()`` function and ``RunSqlResult`` class

**Bugfixes**

- Fix property access in ``SqlCommand`` with better error messages indicating required method calls


0.3.1 (2025-06-15)
------------------------------------------------------------------------------
**Features and Improvements**

- Add the following public APIs:
    - ``simple_aws_redshift.api.RedshiftClusterConnectionParams``
    - ``simple_aws_redshift.api.redshift.RedshiftCluster``
    - ``simple_aws_redshift.api.redshift.RedshiftClusterIterProxy``
    - ``simple_aws_redshift.api.redshift.list_redshift_clusters``
    - ``simple_aws_redshift.api.redshift.get_redshift_cluster``

**Minor Improvements**

- Improve Documentation Website.


0.2.1 (2025-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Add the following public APIs:
    - ``simple_aws_redshift.api.RedshiftServerlessConnectionParams``
    - ``simple_aws_redshift.api.redshift_data_api.DescribeStatementResponse``
    - ``simple_aws_redshift.api.redshift_data_api.RedshiftDataType``
    - ``simple_aws_redshift.api.redshift_data_api.type_to_field_mapping``
    - ``simple_aws_redshift.api.redshift_data_api.extract_field_raw_value``
    - ``simple_aws_redshift.api.redshift_data_api.extract_field_python_native_value``
    - ``simple_aws_redshift.api.redshift_data_api.GetStatementResultResponse``
    - ``simple_aws_redshift.api.redshift_data_api.GetStatementResultResponseIterProxy``
    - ``simple_aws_redshift.api.redshift_data_api.RunSqlResult``
    - ``simple_aws_redshift.api.redshift_data_api.run_sql``
    - ``simple_aws_redshift.api.redshift_data_api.get_statement_result``


0.1.1 (2025-06-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add the following public APIs:
    - ``simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespace``
    - ``simple_aws_redshift.api.redshift_serverless.RedshiftServerlessNamespaceIterProxy``
    - ``simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroup``
    - ``simple_aws_redshift.api.redshift_serverless.RedshiftServerlessWorkgroupIterProxy``
    - ``simple_aws_redshift.api.redshift_serverless.list_namespaces``
    - ``simple_aws_redshift.api.redshift_serverless.get_namespace``
    - ``simple_aws_redshift.api.redshift_serverless.delete_namespace``
    - ``simple_aws_redshift.api.redshift_serverless.list_workgroups``
    - ``simple_aws_redshift.api.redshift_serverless.get_workgroup``
    - ``simple_aws_redshift.api.redshift_serverless.delete_workgroup``
