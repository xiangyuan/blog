public: yes
tags: [Mysql]

Show MySQL Database Encoding
============================

To get the current mysql database encoding, issue the following sql
query:

.. sourcecode:: mysql

    SHOW VARIABLES LIKE "character_set_database";
