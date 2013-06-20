Change MySQL Database Encoding
==============================

:tags: databases

To change MySQL table column encoding:

.. sourcecode:: mysql

    ALTER TABLE artists
    CHANGE [fieldname] [fieldname] [fieldtype]
    CHARACTER SET [encoding]
    COLLATE [collation];

To change table encoding:

.. sourcecode:: mysql

    ALTER TABLE [tablename]
    CONVERT TO CHARACTER SET [encoding]
    COLLATE [collation];

To change database encoding:

.. sourcecode:: mysql

    ALTER DATABASE [dbname]
    CHARACTER SET [encoding]
    COLLATE [collation];
