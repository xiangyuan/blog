public: yes
tags: [linux]

tutorial: How to use MPX to control several mouse pointers at the same time
===========================================================================

The `MPX project <http://www.x.org/wiki/Development/Documentation/MPX>`_ is a Xorg extension to
allow several mouse pointers and keyboards in an X session to be used at the same time. This is
especially useful when using touch-sensitive screens (multitouch).

Watch the following Youtube video to see a demo:

.. youtube:: 0MUOn_nJmRA

In the Xorg version shipped with a current installation of Ubuntu, this extension is already
included. This how-to will show you how to control two pointers and keyboards at the same time with
the "xinput" tool.

First, call the xinput tool to list all available devices.

.. sourcecode:: bash

    $ xinput list
    ⎡ Virtual core pointer                      id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ Tangtop Generic USBPS2                    id=14   [slave  pointer  (2)]
    ⎜   ↳ SynPS/2 Synaptics TouchPad                id=16   [slave  pointer  (2)]
    ⎜   ↳ Macintosh mouse button emulation          id=17   [slave  pointer  (2)]
    ⎜   ↳ PS/2 Generic Mouse                        id=18   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Fujitsu FUJ02E3                           id=7    [slave  keyboard (3)]
        ↳ Video Bus                                 id=8    [slave  keyboard (3)]
        ↳ Fujitsu FUJ02B1                           id=9    [slave  keyboard (3)]
        ↳ Power Button                              id=10   [slave  keyboard (3)]
        ↳ Sleep Button                              id=11   [slave  keyboard (3)]
        ↳ Tangtop Generic USBPS2                    id=13   [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=15   [slave  keyboard (3)]
        ↳ USB Audio                                 id=12   [slave  keyboard (3)]

In my case, I want to use the following four devices:

-  Internal mouse: SynPS/2 Synaptics TouchPad (id=16)
-  Internal keyboard: AT Translated Set 2 keyboard (id=15)
-  External mouse: Tangtop Generic USBPS2 (id=14)
-  External keyboard: Tangtop Generic USBPS2 (id=13)

Now, create a new master.

.. sourcecode:: bash

    $ xinput create-master secondary

You may hve noticed now that a second mouse pointer appears. This is because a new master called
"secondary" has been created. Issue "xinput list" to see the new entries.

.. sourcecode:: bash

    ⎡ secondary pointer                        id=19   [master pointer  (20)]
    ⎜   ↳ secondary XTEST pointer                   id=21   [slave  pointer  (19)]
    ⎣ secondary keyboard                        id=20   [master keyboard (19)]
        ↳ secondary XTEST keyboard                  id=22   [slave  keyboard (20)]

The next step is to reattach my two external input devices to the newly created master.

.. sourcecode:: bash

    $ xinput reattach 14 19
    $ xinput reattach 13 20

This will attach the pointer with the id 14 to the secondary pointer master with the id 19, and the
keyboard with the id 13 to the keyboard master with the id 19.

Done! The device list now looks like this:

.. sourcecode:: bash

    $ xinput list
    ⎡ Virtual core pointer                      id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ SynPS/2 Synaptics TouchPad                id=16   [slave  pointer  (2)]
    ⎜   ↳ Macintosh mouse button emulation          id=17   [slave  pointer  (2)]
    ⎜   ↳ PS/2 Generic Mouse                        id=18   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Fujitsu FUJ02E3                           id=7    [slave  keyboard (3)]
        ↳ Video Bus                                 id=8    [slave  keyboard (3)]
        ↳ Fujitsu FUJ02B1                           id=9    [slave  keyboard (3)]
        ↳ Power Button                              id=10   [slave  keyboard (3)]
        ↳ Sleep Button                              id=11   [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=15   [slave  keyboard (3)]
        ↳ USB Audio                                 id=12   [slave  keyboard (3)]
    ⎡ secondary pointer                         id=19   [master pointer  (20)]
    ⎜   ↳ Tangtop Generic USBPS2                    id=14   [slave  pointer  (19)]
    ⎜   ↳ secondary XTEST pointer                   id=21   [slave  pointer  (19)]
    ⎣ secondary keyboard                        id=20   [master keyboard (19)]
        ↳ Tangtop Generic USBPS2                    id=13   [slave  keyboard (20)]
        ↳ secondary XTEST keyboard                  id=22   [slave  keyboard (20)]

Now someone can work in one window using the first keyboard, and another person can work in a second
window with another keyboard at the same time! Unfortunately I am not able to make a screenshot of
this, as the printscreen utility seems to capture only the first pointer.

**Notes:** There are still a few things that are not very clear to me, e.g. with the second mouse
pointer i can't move any windows (even though i can focus them). Probably Xorg does not give the
second pointer those permissions. Or maybe it has to do with the window manager. I haven't taken a
very deep look into these things yet, so I can't tell you, but I will when I know more :)

**PS:** In case you want to remove the newly created pointers, issue the following commands:

.. sourcecode:: bash

    $ xinput reattach 14 2
    $ xinput reattach 13 3
    $ xinput remove-master 19
