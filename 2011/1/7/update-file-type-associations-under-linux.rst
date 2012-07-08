public: yes
tags: [Linux]

Update file type associations under Linux
=========================================

To update a file type (or rather a mime type) association under Linux, you can use the ``xdg-mime``
command.

.. sourcecode:: bash

    $ xdg-mime default desktop-file mimetype

E.g. to open pdf files with evince, issue

.. sourcecode:: bash

    $ xdg-mime default evince.desktop application/pdf
