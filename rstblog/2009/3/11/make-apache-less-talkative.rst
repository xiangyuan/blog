public: yes
tags: [sysadmin]

Make Apache Less Talkative
==========================

On a standard installation of Apache, the webserver sends a lot of information about installed
software to the client. This would provide a hypothetical attacker with a lot of information of how
to attack your server. To see how verbose your Apache installation actually is, open a non-existing
website on your webserver. In the signature of the 404-error-message, you'll see something like
this:

::

    Apache/2.0.55 (Debian) PHP/5.1.2-1+b1 mod_ssl/2.0.55 OpenSSL/0.9.8b

If you don't want that information to be shown, change the
``ServerTokens`` and ``ServerSignature`` directives in your
Apache-configfile (`/etc/apache2/apache2.conf`) to the values shown below:

.. sourcecode:: apache

    # ServerTokens
    # This directive configures what you return as the Server HTTP response
    # Header. The default is 'Full' which sends information about the OS-Type
    # and compiled in modules.
    # Set to one of:  Full | OS | Minor | Minimal | Major | Prod
    # where Full conveys the most information, and Prod the least.
    #
    ServerTokens Prod

    #
    # Optionally add a line containing the server version and virtual host
    # name to server-generated pages (internal error documents, FTP directory
    # listings, mod_status and mod_info output etc., but not CGI generated
    # documents or custom error documents).
    # Set to "EMail" to also include a mailto: link to the ServerAdmin.
    # Set to one of:  On | Off | EMail
    #
    ServerSignature Off

To also hide information about the installed PHP version, change the ``expose_php`` option in your
PHP-configfile (`/etc/php5/apache2/php.ini`) to `Off`.

.. sourcecode:: ini

    ; Decides whether PHP may expose the fact that it is installed on the server
    ; (e.g. by adding its signature to the Web server header).  It is no security
    ; threat in any way, but it makes it possible to determine whether you use PHP
    ; on your server or not.
    expose_php = Off

Finally, restart Apache.

.. sourcecode:: bash

    $ /etc/init.d/apache2 force-reload

Voilà, the server-information on your error pages should now be gone.

**Update:** Under Debian Lenny, those directives are stored in the file
`/etc/apache2/conf.d/security`.
