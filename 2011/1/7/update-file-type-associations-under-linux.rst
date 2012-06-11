public: yes
tags: [Arch Linux,Linux]

Update file type associations under Linux
=========================================

To update a file type (or rather a mime type) association under Linux,
you can use the ``xdg-mime`` command.

::

    $ xdg-mime default desktop-file mimetype

E.g. to open pdf files with evince, issue

::

    $ xdg-mime default evince.desktop application/pdf


