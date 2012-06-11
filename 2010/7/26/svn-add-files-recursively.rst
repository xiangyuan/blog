public: yes
tags: [Linux]

SVN add files recursively
=========================

By default, the svn command adds new files and folders recursively, but
skips over already added folders. So new files in already added folders
won't get added.

The solution is to list all new files with the following command:

::

    svn status | grep ?

...and then add each folder separately.

