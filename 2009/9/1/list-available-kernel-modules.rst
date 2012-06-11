public: yes
tags: [Gentoo,Linux]

List Available Kernel Modules
=============================

To list all available linux kernel modules, issue:

::

    # find /lib/modules// -type f -iname '*.o' -or -iname '*.ko'


