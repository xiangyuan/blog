public: yes
tags: [Ubuntu, Linux]

Enable Ctr+Alt+Backspace in Ubuntu Jaunty
=========================================

To re-enable the `ctrl+alt+backspace` key combination in Ubuntu Jaunty, add this code to
`/etc/X11/xorg.conf`:

.. sourcecode:: plain

    Section "ServerFlags"
        Option "DontZap" "false"
    EndSection
