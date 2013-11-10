Fetch Current Bitcoin Price with Python
=======================================

:tags: python, bitcoin, mtgox
:language: en
:summary: How to get the current Bitcoin price from MtGox using Python.


Using the MtGox_ API, you can easily fetch the current Bitcoin_ price using a
very small Python script.

.. sourcecode:: python

    import requests
    url = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker'
    r = requests.get(url, headers={'Accept': 'application/json'})
    print r.json()['data']['avg']['display_short']

If you want to support for multiple currencies and more information, here's an
extended version:

.. sourcecode:: python

    # -*- coding: utf-8 -*-
    from __future__ import print_function, unicode_literals
    import requests

    currencies = [
        ('BTCUSD', '$'),
        ('BTCEUR', '€'),
    ]

    print('---')
    for currency, symbol in currencies:
        r = requests.get('http://data.mtgox.com/api/2/{}/money/ticker'.format(currency))
        data = r.json()['data']
        avg = float(data['avg']['value'])
        high = float(data['high']['value'])
        low = float(data['low']['value'])
        last = float(data['last']['value'])
        
        print(currency.encode('utf8'))
        print('Low: {} {:.2f}'.format(symbol, low).encode('utf8'))
        print('Average: {} {:.2f}'.format(symbol, avg).encode('utf8'))
        print('High: {} {:.2f}'.format(symbol, high).encode('utf8'))
        print('Last: {} {:.2f}'.format(symbol, last).encode('utf8'))
        print('---')

Usage::

    $ python bitcoin.py
    ---
    BTCUSD
    Low: $ 305.00
    Average: $ 362.75
    High: $ 395.00
    Last: $ 342.00
    ---
    BTCEUR
    Low: € 221.85
    Average: € 272.07
    High: € 298.00
    Last: € 253.01
    ---

Credits: Inspiration by `https://coderwall.com/p/ksrula <https://coderwall.com/p/ksrula>`__.


.. _bitcoin: https://en.wikipedia.org/wiki/Bitcoin
.. _mtgox: https://www.mtgox.com/
