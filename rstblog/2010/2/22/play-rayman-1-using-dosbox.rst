public: yes
tags: [gaming]

Play Rayman 1 on Linux using DosBox
===================================

.. image:: /static/img/2010/2/22/rayman1.jpg

This is a tutorial to install and play Rayman 1 (the greatest jump'n'run game ever) using `DosBox
<http://www.dosbox.com/>`_ on Ubuntu.

1. Copy the contents of the Rayman CD to a folder on your computer, e.g.

 .. sourcecode:: bash
    
    $ cp -Rv /media/cdrom /opt/games/RaymanCD

2. Install DosBox

 .. sourcecode:: bash

    $ sudo apt-get install dosbox

3. In your `dosbox.conf` (Usually in `~/.dosbox/dosbox-<version>.conf`)
   set the `keyboard layout` option to your `keyboard layout
   code <http://www.dosbox.com/wiki/Keyboard>`_ (e.g. ``sg`` for swiss
   german layout)

4. Create a new folder for the Rayman installation, e.g.

 .. sourcecode:: bash

    $ mkdir /opt/games/Rayman

5. Issue the following command in your terminal:

 .. sourcecode:: bash

     dosbox -noautoexec \
     -c 'mount c /opt/games/Rayman -freesize 100' \
     -c 'mount -t cdrom r /opt/games/RaymanCD' \
     -c 'r:' \
     -c 'install.bat'

6. Install Rayman (don't forget to let the setup auto-recognize your soundcard).
   After the setup, don't play the game, just exit the menu and close the
   DosBox window.

7. Put a new file called ``rayman.sh`` somewhere on your computer (e.g.
   on your Desktop)

8. Add the following lines to the freshly created file:

 .. sourcecode:: bash
 
     #!/bin/bash
     dosbox -noautoexec \
     -c 'mount c /opt/games/Rayman -freesize 100' \
     -c 'mount -t cdrom r /opt/games/RaymanCD' \
     -c 'c:' \
     -c 'rayman.bat'

9. Make the file executable:
   
 .. sourcecode:: bash

    $ chmod +x rayman.sh

Done, now you can start Rayman at any time by executing the
``rayman.sh`` file. If the gameplay is too fast, change the frequency to
50.
