Improving Firefox SSL/TLS Security
==================================

:tags: firefox, tls, security
:language: en
:summary: How to improve Firefox SSL/TLS security by enabling TLS 1.2 and
          disabling insecure ciphersuites.

Even though Firefox supports TLS 1.2 `since version 24
<https://support.mozilla.org/de/questions/959936#answer-453166>`__, it is not
enabled by default. Even in the current stable version (Firefox 26), only TLS
1.0 and lower are supported. Which is a shame.

I recently discovered a nice website to test your TLS client capabilities:
`https://www.howsmyssl.com/ <https://www.howsmyssl.com/>`_. In the current
Chromium versions all tests pass, but the site doesn't seem to like Firefox 26
too much:

.. image:: /images/2014/1/ssl_bad.png
   :alt: Screenshot of the website saying "Your SSL client is Bad"
   :align: center

There are two issues here that we have to address. The first one is the missing
TLS 1.2 support. The highest supported version is TLS 1.0.

.. image:: /images/2014/1/tlsv1.png
   :alt: Firefox 26 only supports TLS 1.0 and lower.
   :align: center

Support for TLS 1.2 is implemented in Firefox 26 though and can be enabled in
the configuration. Type ``about:config`` in your address bar, skip the warning
and then search for ``security.tls.version``. Change
``security.tls.version.max`` to 3 (TLS 1.2) and ``security.tls.version.min`` to
1 (require at least TLS 1.0). Note that this means you won't be able to connect
to webpages where the server doesn't support TLS. But you don't want to connect
to these websites anyways.

.. image:: /images/2014/1/tls_config.png
   :alt: The resulting Firefox configuration.
   :align: center

The second issue is the support for the ``SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA``
cipher, which is known to be insecure.

.. image:: /images/2014/1/insecure_cyphers.png
   :alt: Firefox 26 supports cipher suites that are known to be insecure.
   :align: center

This setting can also be disabled in the Firefox configuration. In the
``about:config`` screen, search for ``security.ssl3.rsa_fips_des_ede3_sha`` and
disable it.

.. image:: /images/2014/1/disable_rsa_fips.png
   :alt: The resulting Firefox configuration.
   :align: center

That's it, your Firefox (at least version 26) should now pass the test!

.. image:: /images/2014/1/ssl_ok.png
    :alt: The test passes now.
    :align: center

For more background information, see `https://www.howsmyssl.com/s/about.html
<https://www.howsmyssl.com/s/about.html>`__.
