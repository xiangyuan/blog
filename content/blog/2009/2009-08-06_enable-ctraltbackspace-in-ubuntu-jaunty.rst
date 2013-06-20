Enable Ctr+Alt+Backspace in Ubuntu Jaunty
=========================================

:tags: ubuntu

To re-enable the `ctrl+alt+backspace` key combination in Ubuntu Jaunty, add this code to
`/etc/X11/xorg.conf`:

.. sourcecode:: plain

    Section "ServerFlags"
        Option "DontZap" "false"
    EndSection
