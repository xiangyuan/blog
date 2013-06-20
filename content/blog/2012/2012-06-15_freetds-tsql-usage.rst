public: yes
tags: [sysadmin, databases]
summary: How to use the tsql command.

Using tsql
==========

Today I had to connect to a MSSQL database from a Linux box. A library to do this is `FreeTDS
<http://www.freetds.org/>`_. It also provides an interactive ``tsql`` command. Install it from your
distro repositories or compile it by hand.

Unfortunately the command provides no ``--help`` or ``-h`` option, but there are manpages. Here are
some of the relevant options:

.. sourcecode:: plain

    -H hostname
          the DNS hostname of the server

    -p port
          the port at which SQL Server is listening

    -U username
          database login name. If username is not provided, a domain login is attempted for TDS 7+ connections.

    -P password
          database password.

After successfully connecting to a database server, there was another issue for me. The SQL queries
were not submitted simply by ending them with a semicolon, unlike the ``mysql`` and ``psql``
tools. It took me a while to figure out that the keyword to submit a query was ``go``...

.. sourcecode:: plain

    $ tsql -H host -p 1433 -U username -P passwd
    locale is "en_US.UTF-8"
    locale charset is "UTF-8"
    using default charset "UTF-8"
    1> use MyDatabase
    2> go
    1> EXEC sp_tables "Security%"
    2> go
    TABLE_QUALIFIER TABLE_OWNER     TABLE_NAME      TABLE_TYPE      REMARKS
    mdPROJECTTIMER  dbo     SecurityLanguages       TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityRightGroups     TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityRightGroupTranslations  TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityRights  TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityRights2UserGroups       TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityRightTranslations       TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityUserGroups      TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityUserGroups2Users        TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityUsers   TABLE   NULL
    mdPROJECTTIMER  dbo     SecurityVersion TABLE   NULL
    (10 rows affected)
    (return status = 0)
