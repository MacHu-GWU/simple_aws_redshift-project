.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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
