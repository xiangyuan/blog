public: yes
tags: [Freizeit,Linux]

Play Rayman 1 using DosBox
==========================

This is a tutorial to install and play Rayman 1 (the greatest jump'n'run
game ever) using `DosBox <http://www.dosbox.com/>`_ on Ubuntu.

.. figure:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2010/02/rayman1-300x209.jpg
   :align: center
   :alt: rayman1

#. Copy the contents of the Rayman CD to a folder on your computer, e.g.
   ``/home/<user>/Games/RaymanCD``
#. Install DosBox (``sudo apt-get install dosbox``)
#. In your dosbox.conf (Usually in ``~/.dosbox/dosbox-<version>.conf``)
   set the ``keyboard layout`` option to your `keyboard layout
   code <http://www.dosbox.com/wiki/Keyboard>`_ (e.g. ``sg`` for swiss
   german layout)
#. Create a new folder for the Rayman installation, e.g.
   ``/home/<user>/Games/Rayman``
#. Issue the following command in your terminal:

   ::

       dosbox -noautoexec -c 'mount c /home//Games/Rayman -freesize 100' -c 'mount -t cdrom r /home//Games/RaymanCD' -c 'r:' -c 'install.bat'

#. Install Rayman (Don't forget to auto-recognize your soundcard). After
   the setup, don't play the game, just exit the menu and close the
   DosBox window.
#. Put a new file called ``rayman.sh`` somewhere on your computer (e.g.
   on your Desktop)
#. Add the following lines to the freshly created file:

   ::

       #!/bin/bash

       dosbox -noautoexec -c 'mount c /home//Games/Rayman -freesize 100' -c 'mount -t cdrom r /home//Games/RaymanCD' -c 'c:' -c 'rayman.bat'

#. Make the file executable: ``chmod +x rayman.sh``

Done, now you can start Rayman at any time by executing the
``rayman.sh`` file. If the gameplay is too fast, change the frequency to
50.

