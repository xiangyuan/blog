public: yes
tags: [Mysql]

Storing an IP in MySQL
======================

Summary
-------

:Datatype: ``int(4) unsigned``
:Storing IP: ``INET_ATON('192.168.1.39')``
:Getting IP: ``INET_NTOA(3232235815)``

Practical example
-----------------

Schema

.. sourcecode:: plain

    mysql> SHOW COLUMNS FROM clickcounter_clicks;
    +---------+-----------------+------+-----+---------+----------------+
    | Field   | Type            | Null | Key | Default | Extra          |
    +---------+-----------------+------+-----+---------+----------------+
    | id      | int(11)         | NO   | PRI | NULL    | auto_increment |
    | link_id | int(11)         | NO   |     |         |                |
    | date    | date            | NO   |     |         |                |
    | ip      | int(4) unsigned | NO   |     |         |                |
    +---------+-----------------+------+-----+---------+----------------+
    4 rows in set (0.00 sec)

Storing

.. sourcecode:: plain

    mysql> INSERT INTO clickcounter_clicks(`date`, `ip`)
         > VALUES (NOW(), INET_ATON('192.168.1.39'));
    Query OK, 1 row affected, 1 warning (0.00 sec)

Retrieving

.. sourcecode:: plain

    mysql> SELECT date, INET_NTOA(ip) AS ip FROM clickcounter_clicks;
    +------------+--------------+
    | date       | ip           |
    +------------+--------------+
    | 2009-06-16 | 192.168.1.39 |
    +------------+--------------+
    1 row in set (0.00 sec)
