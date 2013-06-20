public: yes
tags: [django, testing]
language: en
summary: How to test Dajaxice views using the Django test client.

Testing Dajaxice Views in Django
================================

If you want to test `Dajaxice <http://www.dajaxproject.com/>`_ views from the
Django test client, this might be your first approach:

.. sourcecode:: python

    url = '/dajaxice/apps.front.add_vote/'
    data = {'vote': 'yes', 'primary_key': '1'}
    response = self.client.post(url, data=data)

This doesn't work for several reasons.

First of all, we need to simulate an AJAX request. Therefore the
``HTTP_X_REQUESTED_WITH`` header needs to be set. We can do this by simply
passing it as a kwarg to the ``client.post`` method.

Furthermore, the default data encoding is ``multipart/form-data``, which is not
what we want. Dajax uses ``application/x-www-form-urlencoded`` encoding. We can
solve this by setting the ``content_type`` kwarg.

The third problem is that we can't simply urlencode the data dictionary
directly. The JSON formatted payload should be the value of a key called
``argv``.

Here's a solution that works:

.. sourcecode:: python

    import urllib
    import json

    url = '/dajaxice/apps.front.add_vote/'
    payload = {'vote': 'yes', 'primary_key': 1}
    data = {'argv': json.dumps(payload)}

    response = self.client.post(url,
        data=urllib.urlencode(data),
        content_type='application/x-www-form-urlencoded',
        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
