public: yes
tags: [Linux]

Ubuntu 9.10 "Karmic Koala" watch encrypted DVD
==============================================

In my Ubuntu 9.10 "Karmic Koala" installation, I wasn't able to watch a
DVD, even though libdvdcss was installed. The player windows just closed
themselves immediately after the beginning. After some searching, I
found the solution.

To solve that problem, first install the package
ubuntu-restricted-extras from the universe repository...

::

    sudo apt-get install ubuntu-restricted-extras

...and then execute the following script.

::

    sudo /usr/share/doc/libdvdread4/install-css.sh

(Via
`everflux.de <http://everflux.de/ubuntu-dvd-wiedergabe-libdvdcss-mit-karmic-1430/>`_)

