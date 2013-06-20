Fix Ubuntu user directories (Desktop/Music/Templates etc)
=========================================================

:tags: ubuntu

If you accidentally deleted one of your Ubuntu user directories (like *Desktop*, *Music*,
*Pictures*, *Templates* etc), you can fix them by editing the file `~/.config/user-dirs.dirs`.

.. sourcecode:: bash

    # This file is written by xdg-user-dirs-update
    # If you want to change or add directories, just edit the line you're
    # interested in. All local changes will be retained on the next run
    # Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
    # homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
    # absolute path. No other format is supported.
    # 
    XDG_DESKTOP_DIR="$HOME/Desktop"
    XDG_DOWNLOAD_DIR="$HOME/Downloads"
    XDG_TEMPLATES_DIR="$HOME/Templates"
    XDG_PUBLICSHARE_DIR="$HOME/Public"
    XDG_DOCUMENTS_DIR="$HOME/Documents"
    XDG_MUSIC_DIR="$HOME/Music"
    XDG_PICTURES_DIR="$HOME/Pictures"
    XDG_VIDEOS_DIR="$HOME/Videos"

For more information about those "xdg user dirs", see
`http://www.freedesktop.org/wiki/Software/xdg-user-dirs
<http://www.freedesktop.org/wiki/Software/xdg-user-dirs>`_.
