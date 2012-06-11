public: yes
tags: [Webdesign,Serveradministration,Programmieren]

Change MySQL Database Encoding
==============================

After `getting the MySQL Database
encoding </2009/08/show-mysql-database-encoding/>`_, you might want to
change it.

To change table column encoding:

::

    ALTER TABLE artists
    CHANGE [fieldname] [fieldname] [fieldtype]
    CHARACTER SET [encoding]
    COLLATE [collation];

To change table encoding:

::

    ALTER TABLE [tablename]
    CONVERT TO CHARACTER SET [encoding]
    COLLATE [collation];

To change database encoding:

::

    ALTER DATABASE [dbname]
    CHARACTER SET [encoding]
    COLLATE [collation];


