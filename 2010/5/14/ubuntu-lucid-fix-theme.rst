public: yes
tags: [Linux]

Ubuntu Lucid - fix theme
========================

After upgrading to Ubuntu Lucid, I didn't like some aspects of the new
theme (Ambiance). Here the fixes for the two of those things.

Move minimize/maximize/close buttons to the right side
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the new theme, the three buttons to minimize, maximize and close
the window have been moved to the left side of the window. To fix this,
issue this command:

::

    gconftool-2 --type string --set /apps/metacity/general/button_layout ":minimize,maximize,close"

A panel wider than 24px looks ugly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another thing is, that the background image for the panels doesn't scale
(See Launchpad Bug
`532309 <https://bugs.launchpad.net/ubuntu/+source/light-themes/+bug/532309>`_).
To fix this, edit the file ``/usr/share/themes/Ambiance/gtk-2.0/gtkrc``
and comment out the line ``bg_pixmap[NORMAL] = "panel_bg.png"``.

::

    #bg_pixmap[NORMAL] = "panel_bg.png"

As an alternative, if your panel is exactly 30px wide, you can also
replace ``panel_bg.png`` with ``panel_bg_30.png``.

::

    bg_pixmap[NORMAL] = "panel_bg_30.png"

After that, log out and then log in again, and the panels should be
fixed.

