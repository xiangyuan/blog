public: yes
tags: [Serveradministration,Linux]

Change Linux UID/GID
====================

Log in with another user than the one to be edited or reboot into
recovery mode and enter the following commands:

::

    usermod -u  
    groupmod -g  
    find / -user  -exec chown  {} \;
    find / -group  -exec chgrp  {} \;

Warning: Use on your own risk. This change should only be done by users
that know what they're doing.

