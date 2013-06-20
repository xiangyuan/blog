public: yes
tags: [sysadmin]

Change Linux UID/GID
====================

Log in with another user than the one to be edited or reboot into
recovery mode and enter the following commands:

.. sourcecode:: bash

    $ usermod -u  
    $ groupmod -g  
    $ find / -user <user> -exec chown <user> {} \;
    $ find / -group <group> -exec chgrp <group> {} \;

Warning: Use on your own risk. This change should only be done by users
that know what they're doing.
