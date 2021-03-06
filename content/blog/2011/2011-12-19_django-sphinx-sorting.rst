django-sphinx sorting
=====================

:tags: django
:summary: How to sort a SphinxSearch instance.

Unfortunately, the `django-sphinx <https://github.com/dcramer/django-sphinx>`_ module is not very
thoroughly documented. One thing which I could not figure out is how to do sorting. I thought that I
had to set some kind of keyword argument on the SphinxSearch instance... (I have to admit though
that the sorting is indeed demonstrated in the project `README.rst`, I simply overlooked it...)

But the solution was much simpler – you can use ``order_by`` directly on the SphinxSearch instance.

.. sourcecode:: python

    Model.search.query('spam').order_by('-amount')

Make sure that the selected sorting key is marked as a sortable attribute (e.g.  ``sql_attr_uint``
or ``sql_attr_str2ordinal``) in your sphinx.conf.
