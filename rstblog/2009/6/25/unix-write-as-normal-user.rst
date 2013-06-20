public: yes
tags: [sysadmin]

Unix `write` as normal user
===========================

In case you get a "Permission denied" when trying to use the ``write`` command as a normal user on
Unix, the setuid bit is probably missing. Apparently this is the default setting on Debian Etch.
Set it with:

.. sourcecode:: bash

    $ chmod u+s /usr/bin/write
