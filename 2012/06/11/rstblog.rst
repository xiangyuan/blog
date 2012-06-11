public: yes
tags: [rstblog, blog, rst, python]
summary: |
    I just replaced Wordpress with rstblog.

Goodbye Wordpress, hi rstblog!
==============================

Since having switched from the PHP world to the Python world about 2 years ago, I thought about
relaunching my Blog using Python instead of PHP. At first, I thought about creating an application
with Django and PostgreSQL, but never really had the time and motivation to finally implement it.
But today I stumbled over `rstblog <https://github.com/mitsuhiko/rstblog>`_ by `Armin Ronacher
<http://lucumr.pocoo.org/>`_.

And so on... Some sandbox playing here:

I also write code!

.. sourcecode:: ruby

    foo = 23
    def bar
        42
    end
    puts foo/bar

.. sourcecode:: python

    class Bar(object):
        def foo(bar):
            print 'I don\'t like spam!'

Yeah pygments!

And also LaTeX:

.. math::

    x = f(y) = \sum_{i=1}^{n^2} n + \frac{2}{3 \phi} + \delta
