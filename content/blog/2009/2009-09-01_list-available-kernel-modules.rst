List Available Kernel Modules
=============================

:tags: sysadmin

To list all available linux kernel modules, issue as root:

.. sourcecode:: linux

    $ find /lib/modules// -type f -iname '*.o' -or -iname '*.ko'
