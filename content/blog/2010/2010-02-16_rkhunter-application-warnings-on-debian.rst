Rkhunter Application Warnings on Debian
=======================================

:tags: sysadmin

On my (up to date) Debian Lenny installation, `rkhunter <http://rkhunter.sourceforge.net/>`_
regularly complains that various applications are out of date. This happens if the developer has
released a new version of an application, but the Debian security team hasn't added it to the repos
yet.

    Warning: Application 'gpg', version 'xxx', is out of date, and
    possibly a security risk. Warning: Application 'named', version
    'xxx', is out of date, and possibly a security risk. Warning:
    Application 'openssl', version 'xxx', is out of date, and possibly a
    security risk. (...)

As I have enough trust in the Debian security team, I wanted to disable the app version checks. That
is possible by adding the "apps" test to the `DISABLE_TESTS` option in `/etc/rkhunter.conf`:

.. sourcecode:: plain

    199 DISABLE_TESTS="suspscan hidden_procs deleted_files packet_cap_apps apps"

If you're also getting false warnings about possible promiscuous interfaces (e.g. on a virtual
server), add the "promisc" option to the `DISABLE_TESTS` option.

.. sourcecode:: plain

    199 DISABLE_TESTS="suspscan hidden_procs deleted_files packet_cap_apps apps promisc"

Another hint: Set the `PKGMGR` option to `DPKG` in order to check the hashes of binaries against the
hashes provided by the Debian package manager, instead of just observing changes in the binary,
which will report false positives on each system package update.

.. sourcecode:: plain

    257 PKGMGR=DPKG
