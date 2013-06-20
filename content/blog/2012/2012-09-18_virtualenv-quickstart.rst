public: yes
tags: [python, pip, virtualenv]
summary: A short virtualenv quickstart guide.

Virtualenv Quickstart Guide
===========================

I was searching for a nice `virtualenv` quickstart guide today, but couldn't find
one that I liked. Either they were outdated and still relied on
`easy_install`, or they were too complicated. So here's my own.

Why use virtualenv?
-------------------

Virtualenv (http://www.virtualenv.org/) basically provides you with a full
Python environment (and/or versions) inside a single folder. This way, you can
have multiple Python environments next to each other (usually one per project),
each with its own binaries and packages.

I really recommend using virtualenv for *all* Python projects. Tools like
`virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_
and `requirements files
<http://www.pip-installer.org/en/latest/requirements.html>`_ make setting up a
new virtual environment a breeze.

Setup
-----

In case you're still using `easy_install` to install Python packages, you
should `switch to pip immediately
<http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`__::

    $ sudo easy_install pip

Then install virtualenv itself::

    $ sudo pip install virtualenv

Those are usually the only two Python packages that you should install to your
systemwide `PYTHONPATH`.

Creating a virtualenv
---------------------

Now you need to initialize your virtual environment. This can be located
anywhere. I'd recommend either creating it into a folder called `VIRTUAL` inside
your project directory, or creating a folder called `.virtualenv` in your home
directory and placing it in there, named like your project. ::

    $ virtualenv --no-site-packages VIRTUAL
    New python executable in VIRTUAL/bin/python
    Installing setuptools............done.
    Installing pip...............done.

Enabling a virtualenv
---------------------

To actually work inside a virtualenv, you need to enable it first. This is done
by sourcing `bin/activate` inside your virtualenv folder. ::

    $ source VIRTUAL/bin/activate

This step needs to be done each time you start a new bash prompt. Now every time
you call a Python-related binary (e.g. `python` or  `pip`), the version from
your virtualenv instead of the system version will be used.

You can also use your virtual python without sourcing the mentioned file first,
but then you need to specify the full path to the desired binary (e.g.
`VIRTUAL/bin/python manage.py runserver`). This can be useful for bash scripts.

Installing packages, tracking requirements
-------------------------------------------

Installing Python packages is as simple as ``pip install <packagename>`` after
enabling your virtualenv. When having worked inside a virtualenv for a while,
you've probably installed a few packages and want to document those dependencies
somehow. This is where the `pip freeze` command and `requirements.txt` files can
and should be used. ::

    $ pip install Django
    ...
    $ pip freeze > requirements.txt
    $ cat requirements.txt
    Django==1.4.1
    wsgiref==0.1.2

(**Note:** The `wsgiref` package is a part of the Python standard library.
Currently it is the only standard library package that includes package
metadata, so it is the only standard library package whose presence pip
reports.)

The `requirements.txt` file is a very good convention, as it allows you or
another developer to quickly replicate the environment you're currently working
in. After creating an empty virtualenv, you can simply install all necessary
packages with::

    $ pip install -r requirements.txt

For more information, please refer to the `pip docs
<http://www.pip-installer.org/en/latest/requirements.html>`__.

Next steps
----------

To simplify your life with virtualenv, you should start using
`virtualenvwrapper`_, which gives you nice shortcut functions like
`mkvirtualenv` to create a new environment, `workon` to enable a specific
virtual environment, `rmvirtualenv` to remove an environment and more.

This should be enough to get you started. In case some parts of this quickstart
guide are difficult to understand or if you have any questions, please leave a
comment below.
