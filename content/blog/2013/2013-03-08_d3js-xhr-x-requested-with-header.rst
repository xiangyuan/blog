d3.js and X-Requested-With
==========================

:tags: d3.js, ajax, django, flask
:language: en
:summary: How to make AJAX detection used by Django and Flask work with d3.js.

Most JavaScript frameworks set the `X-Requested-With` HTTP Header to
`XMLHttpRequest` when sending non-cross-domain XHR requests. Many web
frameworks like `Django <http://djangoproject.com/>`_ or `Flask
<http://flask.pocoo.org/>`_ use this to detect AJAX requests.

Because of issues with `X-Requested-With` and cross-domain XHR requests, d3.js
`does not set that header by default <https://github.com/mbostock/d3/pull/592>`__.
Therefore Django's `request.is_ajax()` and Flask's `request.is_xhr()` break.

In order to make d3 work with those AJAX detection functions, you need to
manually add the header to the request. Instead of

.. sourcecode:: javascript

    d3.json("/path", function(error, data) {
        // Process data
    });

you would write

.. sourcecode:: javascript

    d3.json("/path").header("X-Requested-With", "XMLHttpRequest").get(function(error, data) {
        // Process data
    });

**Warning:** Never use the `X-Requested-With` header as a security feature. It
provides no security whatsoever and can always be faked.
