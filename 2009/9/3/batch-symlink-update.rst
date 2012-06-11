public: yes
tags: [Arbeitsalltag,Serveradministration,Linux]

Batch symlink update
====================

If you have a directory with a lot of wrong symlinks that you need to
update, you can use this bash script to partially replace strings in the
target path.

::

    #/bin/bash

    SEARCHPATH=/etc/alternatives #Directory containing wrong symlinks
    FILTERSTRING=openjdk #String to filter list of symlinks to update (using grep)
    SEARCHSTRING=java-6-openjdk #String to search in symlink target path
    REPLACESTRING=java-6-sun #String to replace in symlink target path

    find ${SEARCHPATH} -type l | while read LINK; do
        TARGET=$(readlink $LINK)
        if `echo ${TARGET} | grep "${FILTERSTRING}" 1>/dev/null 2>&1`; then
            TARGET=`echo ${TARGET} | sed "s#${SEARCHSTRING}#${REPLACESTRING}#g"`
            echo "executing: ln -sf \"${TARGET}\" \"${LINK}\""
            ln -sf "${TARGET}" "${LINK}"
        fi  
    done

Disclaimer: This is the first bash script I've ever written, use on your
own risk ;) But it worked on my computer.

