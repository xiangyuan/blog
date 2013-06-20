PHP-FPM and Nginx Upstream Configuration
========================================

:tags: sysadmin, php, nginx
:language: en
:summary: Current versions of php5-fpm from dotdeb listen on a unix domain socket by default, instead of using port 9000.

Most nginx_ / php-fpm_ tutorials you'll find nowadays recommend to create an
nginx upstream configuration that listens on localhost port 9000. ::

    upstream php {
        server 127.0.0.1:9000;
    }

If you're using a current version of Debian and php5-fpm from dotdeb_, this
won't work though and you'll see the following error message in your nginx log::

   2013/05/25 00:12:04 [error] 17672#0: *76 connect() failed (111: Connection refused) while connecting to
   upstream, client: 2a02:1205:5050:8530:c5f6:250c:ffa0:4d49, server: example.com, request: "GET /index.php
   HTTP/1.1", upstream: "fastcgi://127.0.0.1:9000", host: "example.com" 

This is because the dotdeb version seems to have changed the default
configuration from the IP based version to a unix domain socket. You can grep
for the important line in your configuration::

    danilo@server:~$ grep -ri "listen = " /etc/php5/fpm/
    /etc/php5/fpm/pool.d/www.conf:listen = /var/run/php5-fpm.sock

To be on the safe side, you can also test whether any process is listening on
port 9000::

    danilo@server:~$ sudo lsof -i tcp:9000
    danilo@server:~$

It's trivial to adjust the nginx configuration accordingly::

    upstream php {
        server unix:/var/run/php5-fpm.sock;
    }

Simply restart nginx and everything should be working.

.. _dotdeb: http://www.dotdeb.org/
.. _nginx: http://nginx.org/
.. _php-fpm: http://php-fpm.org/
