public: yes
tags: [Arch Linux, Ubuntu, Linux]

Use easy_install under Arch Linux or Ubuntu
===========================================

If you want to use Python's ``easy_install``, you need to install an
additional package. Under Arch Linux, you need ``python2-distribute``.

.. sourcecode:: bash

    $ pacman -S python2-distribute

If you're an Ubuntu user, install ``python-setuptools``.

.. sourcecode:: bash

    $ apt-get install python-setuptools
