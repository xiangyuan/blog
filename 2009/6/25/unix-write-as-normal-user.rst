public: yes
tags: [Serveradministration,Debian,Linux]

Unix "write" as normal user
===========================

In case you get a "Permission denied" when trying to use the ``write``
command as a normal user on Unix, possibly the setuid bit is missing.
Apparently this is the default setting on Debian Etch. Set it with:

::

    # chmod u+s /usr/bin/write


