public: yes
tags: [Webdesign,Serveradministration]

Netbeans Communications Link Failure
====================================

Are you getting the following error message when trying to connect to
your local mysql server from Netbeans?

::

    Unable to connect to the MySQL server:

    org.netbeans.api.db.explorer.DatabaseException: org.netbeans.api.db.explorer.DatabaseException:
    com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure

    Last packet sent to the server was 0 ms ago..

    The server may not be running or your MySQL connection properties may not be set correctly. Do you want to edit your MySQL connectino properties?

First try to connect to the server with other tools like
``/usr/bin/mysql-administrator`` or ``mysql -u user -p``. If that
doesn't work, your MySQL server is probably down. If it does, try
commenting out the ``skip-networking`` option in your /etc/mysql/my.cnf
file.

