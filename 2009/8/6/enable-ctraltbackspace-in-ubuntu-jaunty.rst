public: yes
tags: [Linux]

Enable Ctr+Alt+Backspace in Ubuntu Jaunty
=========================================

To re-enable the ctrl+alt+backspace combination in Ubuntu Jaunty, add
this code to /etc/X11/xorg.conf:

::

    Section "ServerFlags"
        Option "DontZap" "false"
    EndSection


