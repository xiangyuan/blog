public: yes
tags: [python, heroku]
language: en
summary: |
    I created a buildpack that brings support for Numpy, Scipy and Scikit-learn
    to Heroku.

Heroku Buildpack for Numpy, Scipy and Scikit-Learn
==================================================

(TLDR: https://github.com/dbrgn/heroku-buildpack-python-sklearn) 

Background
----------

At Webrepublic_ we just launched a Python based system that among other things
does comparison of large texts using tf-idf vectors in a multi-dimensional
vector space and measuring the cosine similarity between them (see
http://stackoverflow.com/a/8897648/284318). For this, we needed `scikit-learn`_.

During the deployment process, I discovered that *one does not simply deploy
scikit-learn on Heroku*. There were different issues with it. First of all,
Scipy needs Numpy to be available at ``setup.py`` parse time. If you just
install Numpy and Scipy using requirements.txt, Numpy won't yet be installed at
the time the Scipy ``setup.py`` is processed. (Note that this has been fixed in
`current versions of Scipy <https://github.com/scipy/scipy/pull/453>`__.)

Another issue was that a Fortran compiler and different libraries are needed to
build Scipy, all of which are not available on Heroku.

Problem Solving Attempts
------------------------

The first thing I found while looking for a solution was
`wyn/heroku-buildpack-python`_, but I couldn't quite get it to work. The second
thing I found was `ToonTimbermont/heroku-buildpack-python`_, a fork of wyn's
fork that solves some of the issues.

(I also played around with Kenneth Reitz's `anaconda buildpack`_, but didn't
really get it to work the way I wanted it.)

By combining the work of both developers, using the `precompiled binaries by
wyn`_ and adding some code I managed to rebase all the changes on top of
Heroku's current buildpack. This solves some issues/bugs with older versions of
Pip.

Another change I made was that the dependencies can be stated in
``requirements.txt`` as usual, instead of requiring a ``setup.py`` file.

You can find the buildpack at
https://github.com/dbrgn/heroku-buildpack-python-sklearn. All the changes
against the official Heroku buildpack have been condensed in a `single commit
<https://github.com/dbrgn/heroku-buildpack-python-sklearn/commit/87cf7b24a358b916deaf26b784ea95be42590efe>`__.


Usage
-----

The process to use the buildpack is as straightforward as with any other
buildpack. For a new app::

    heroku create --buildpack https://github.com/dbrgn/heroku-buildpack-python-sklearn/

For an existing app::

    heroku config:set BUILDPACK_URL=https://github.com/dbrgn/heroku-buildpack-python-sklearn/

If you have any questions or problems, feel free to leave a comment or `open an
issue on Github <https://github.com/dbrgn/heroku-buildpack-python-sklearn/issues>`__.

.. _webrepublic: https://www.webrepublic.ch/
.. _scikit-learn: http://scikit-learn.org/stable/
.. _wyn/heroku-buildpack-python: https://github.com/wyn/heroku-buildpack-python
.. _toontimbermont/heroku-buildpack-python: https://github.com/ToonTimbermont/heroku-buildpack-python
.. _precompiled binaries by wyn: https://github.com/wyn/npscipy-binaries
.. _anaconda buildpack: https://github.com/kennethreitz/anaconda-buildpack
