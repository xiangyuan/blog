public: yes
tags: [rstblog, blog, rst, python]
summary: I just replaced Wordpress with rstblog.

Goodbye Wordpress, hi rstblog!
==============================

Since having switched from the PHP world to the Python world about 2 years ago, I thought about
relaunching my Blog using Python instead of PHP. At first, I thought about creating an application
with Django and PostgreSQL, but never really had the time and motivation to finally implement it.
But today I stumbled over `rstblog <https://github.com/mitsuhiko/rstblog>`_ by `Armin Ronacher
<http://lucumr.pocoo.org/>`_.

It is basically a static `reStructuredText
<http://docutils.sourceforge.net/rst.html>`_ to HTML converter. You create a
`year/month/day` folder structure, create `.rst` files in there, add metadata
to them in `YAML <http://www.yaml.org/>`_ format and run the generator-script.

Because it's static, you don't need any dynamic webserver or interpreter, it's just plain HTML files
that you can serve practically everywhere. You can even track them using a source control system.
And last but not least – you'll never have to update your Wordpress installation again, yay!

rstblog supports everything a blog needs: detail pages, archive pages, tags,
atom feeds and comments (using `Disqus <http://disqus.com/>`_). You can create
custom stylesheets and templates.

You can also embed syntax highlighted code using `pygments <http://pygments.org/>`_:

.. sourcecode:: python

    class Bar(object):
        def foo(bar):
            print 'I don\'t like spam!'

And `LaTeX <http://www.latex-project.org/>`_ formulas:

.. math::

    f(x) = a_0 + \sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi x}{L} + b_n \sin \frac{n \pi x}{L}\right)

There's even more to like. If you want to know more, take a look at the
`repository and the sourcecode <https://github.com/mitsuhiko/rstblog>`_. That's
also one of the downsides – there's no official documentation and the project
seems pretty inactive, pull requests aren't being merged.

To get started, here are some related blogposts:

- http://codesymphony.net/2011/09/10/setting-up-rstblog/
- http://nblock.org/2011/08/31/1st-blogpost/
- http://mattdeboard.net/2011/05/09/more-tips-on-rstblog/

Besides the blog-related technical details, this blog will from now on focus on
technical content, usually written in English about Python/Django related
things.
