public: yes
tags: [Ubuntu,Internet]

Tips for using Ubuntu with dwm
==============================

Some useful tips for using the `dwm <http://dwm.suckless.org/>`_ window manager on Ubuntu:

GDM / Booting
-------------

- To disable the automatic start of gdm, add "text" to the ``GRUB_CMDLINE_LINUX_DEFAULT``-line in
  ``/etc/defaults/grub``.

Network / WLAN
--------------

- If you want easier network configuration, use `wicd <http://wicd.sourceforge.net/>`_ instead of
  the `gnome network manager <http://projects.gnome.org/NetworkManager/>`_ (``sudo aptitude install
  network-manager- network-manager-gnome- wicd+``).  You can start it with ``wicd-client -n``. Or if
  you prefer console-based configuration, try ``wicd-curses``.

Audio / Sound
-------------

- In order for the sound to work, add ``start-pulseaudio-x11 &`` to your ``-/.xinitrc`` file, add
  your user to the audio group and reboot. You can configure your sound devices using ``alsamixer``.
- As a replacement for your usual audio player software, you can use `herrie
  <http://herrie.info/>`_.

Communication / Chat
--------------------

- Use `centerim <http://www.centerim.org/>`_ or `bitlbee <http://www.bitlbee.org/>`_ for instant
  messaging to replace pidgin. Or use `finch <http://developer.pidgin.im/wiki/Using%20Finch>`_, a
  console-based frontend for pidgin.
