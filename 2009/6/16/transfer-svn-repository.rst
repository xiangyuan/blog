public: yes
tags: [Serveradministration,Linux]

Transfer SVN Repository
=======================

To transfer an SVN repository from one server to another one, first dump
the repo and then load it into the new repo using ``svnadmin``.

Dump on server 1:

::

    $ svnadmin dump /var/svn/repos/repo > ~/repo_svn.dump

Load on server 2:

::

    $ svnadmin load/var/svn/repos/repo < ~/repo_svn.dump


