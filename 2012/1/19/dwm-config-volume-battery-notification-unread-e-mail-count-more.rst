public: yes
tags: [Arch Linux,Linux]

dwm config - volume, battery notification, unread e-mail count & more
=====================================================================

As many other `dwm <http://dwm.suckless.org/>`_ users do, I customized
my .xinitrc file and the dwm status bar in to display some useful
information. Here is my configuration:

.xinitrc
~~~~~~~~

This is what my .xinitrc looks like:

::

    # set keyboard layout to Swiss German
    setxkbmap ch

    # Load .Xresources file
    xrdb -merge ~/.Xresources

    # Start xbindkeys
    xbindkeys &

    # Set some defaults
    export BROWSER=chromium &
    export EDITOR=vim &
    xdg-mime default evince.desktop application/pdf &

    # Loop
    while true
    do
        # Set root title
        sh .xsetroot.sh

        # Check battery level
        BATT=$( acpi -b | sed 's/.*[charging|unknown], \([0-9]*\)%.*/\1/gi' )
        STATUS=$( acpi -b | sed 's/.*: \([a-zA-Z]*\),.*/\1/gi' )
        if ([ $BATT -le 5 ] && [ $STATUS == 'Discharging' ]); then
            # Beep
            echo -e "\007" >/dev/tty10 && sleep 0.2 
            echo -e "\007" >/dev/tty10 && sleep 0.2 
            echo -e "\007" >/dev/tty10 && sleep 0.2 
            # Blink
            echo 'on' > /proc/acpi/ibm/light && sleep 1
            echo 'off' > /proc/acpi/ibm/light
        fi  

        # Update every 10s
        sleep 10s
    done &

    # Set up rotated dual screen without touching my xorg.conf
    xrandr --output DVI-1 --auto --rotate left --pos 0x0 --output DVI-0 --auto --pos 1080x720 --rotate normal

    # Read .xsessionrc
    sh ~/.xsessionrc &

    # Set wallpaper
    feh --bg-scale ~/.xwallpaper-dwm.png
        
    # Set WM name (for Java apps)
    wmname LG3D

    # Run dwm
    exec dwm 

.Xresources
~~~~~~~~~~~

In my .Xresources, I'm setting the UXTerm color to white on black, as
well as fixing a bug with the ``Alt`` key in SSH sessions. The last line
is to set the window URGENT flag when the window uses the system bell.

::

    UXTerm*eightBitInput: false
    UXTerm*metaSendsEscape: true
    UXTerm*reverseVideo: true
    UXTerm*bellIsUrgent: true

.xsetroot.sh
~~~~~~~~~~~~

As you've seen in my .xinitrc file, I didn't want to keep my xsetroot
commands in the .xinitrc file. The main reason for this is that now I
can update the status information from an external script, e.g. when
pushing some volume buttons on my notebook.

::

    DATETIME=`date`
    UPTIME=`uptime | sed 's/.*up\s*//' | sed 's/,\s*[0-9]* user.*//' | sed 's/  / /g'`
    VOLUME=$( amixer sget Master | grep -e 'Front Left:' | sed 's/[^\[]*\[\([0-9]\{1,3\}%\).*\(on\|off\).*/\2 \1/' | sed 's/off/M/' | sed 's/on //' )
    UNREADMAIL=`cat .unreadmail`
    BATTERYSTATE=$( acpi -b | awk '{ split($5,a,":"); print substr($3,0,2), $4, "["a[1]":"a[2]"]" }' | tr -d ',' )
    if [ `date +%S` == 30 -o `date +%S` == 00 ]; then python imap_check_unread.py > .unreadmail; fi
    xsetroot -name "Unread ${UNREADMAIL} | ${VOLUME} | ${DATETIME} | Up ${UPTIME}h | ${BATTERYSTATE}"

The uptime value doesn't look perfect, there are bugs if the uptime is
<1h. But that doesn't bug me :)

In summary, my status bar displays the following things:

-  Unread e-mail count
-  Volume
-  Date and time
-  Uptime
-  Battery status

imap\_check\_unread.py
~~~~~~~~~~~~~~~~~~~~~~

To check the unread mail count in my IMAP account, I created a little
Python script. But because I don't want to query the server every
second, I'm caching the value in a file and updating it every 30
seconds. Create a cronjob or similar to update the file.

::

    #!/usr/bin/env python

    import imaplib

    obj = imaplib.IMAP4_SSL('xxx.xxx.xxx.xxx', '993')
    obj.login('user', 'password')
    obj.select()
    print len(obj.search(None, 'UnSeen')[1][0].split())


