public: yes
tags: [python]
language: en
summary: Python 3.4 will introduce a builtin enumeration type. But you can already
    start using it right now.

Enums in Python
===============

Until now, if you wanted to use enumeration types in Python you had to fall back
to a class-attribute approach:

.. sourcecode:: python

    >>> class Color(object):
    ...    RED = 1
    ...    GREEN = 2
    ...    BLUE = 3
    ...
    >>> print(Color.RED)
    1

This has different downsides, for example with representation (``Color.RED`` is
represented as an integer, not as a color type) and comparability (``Color.RED``
will be equal to ``HttpResponses.INTERNAL_SERVER_ERROR`` if both have the value
1).

Enter `PEP 435`_, which was accepted by Guido_ today. It specifies a new base
class which can be subclassed to create a custom enumeration.

Quickstart
----------

**Declaration:**

.. sourcecode:: python

    >>> from enum import Enum
    >>> class Color(Enum):
    ...     red = 1
    ...     green = 2
    ...     blue = 3

**Representation:**

.. sourcecode:: python

    >>> print(Color.red)
    Color.red
    >>> print(repr(Color.red))
    <Color.red: 1>

**Iteration:**

.. sourcecode:: python

    >>> for color in Color:
    ...   print(color)
    ...
    Color.red
    Color.green
    Color.blue

**Programmatic access:**

.. sourcecode:: python

    >>> Color(1)
    Color.red
    >>> Color['blue']
    Color.blue

There's even more awesome stuff you can do with those enums. For more
information, refer to `the proposal`_.

Can I already use this?
-----------------------

Yes and no. The PEP will be included in Python 3.4. But if you want to start
using it right now, you can use the flufl.enum_ library which is the base
implementation for PEP 435 and works for Python ≥2.7 and ≥3.2.


.. _pep 435: http://www.python.org/dev/peps/pep-0435/
.. _the proposal: http://www.python.org/dev/peps/pep-0435/
.. _guido: http://www.python.org/~guido/
.. _flufl.enum: http://pythonhosted.org/flufl.enum/
