List Outdated Dependencies with Pip
===================================

:tags: pip, python
:language: en
:summary: Version 1.3 of pip makes it possible to list outdated packages.

In the past, if you wanted to review your installed pip packages to see if there
are updates available, you either had to use tools like `pip-tools`_ or check
all of them manually.

But since version 1.3 (released on 2013-03-07), pip supports the checking of
dependencies with the new ``list`` command. In contrast to ``pip freeze``, the
primary idea of the ``list`` command is to list and analyze installed packages
in a human readable (instead of machine parseable) format.

::

    $ pip freeze
    django-unchained==1.0.1
    requests==1.1.0
    wsgiref==0.1.2

::

    $ pip list
    django-unchained (1.0.1)
    requests (1.1.0)
    wsgiref (0.1.2)

The best thing about the new command is that you can check packages for updates
and list only specific packages::

    List Options:
      -o, --outdated     List outdated packages (excluding editables)
      -u, --uptodate     List uptodate packages (excluding editables)
      -e, --editable     List editable projects.
      -l, --local        If in a virtualenv that has global access, do not list globally-installed packages.

In summary, you can now show outdated dependencies with a single pip command::

    $ pip list --outdated
    requests (Current: 1.1.0 Latest: 1.2.0)

Awesome!

.. _pip-tools: https://github.com/nvie/pip-tools
