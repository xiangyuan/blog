dwm ssh/screen/irssi notifications 
===================================

:tags: sysadmin, dwm
:summary: Show notifications for irssi mentions inside a ssh screen session on dwm.

I always keep an irssi session open inside a screen session on my server
via ssh. I always thought that notifications aren't possible for such a
setup. But they are.

1. In your irssi session, issue the following commands:

.. sourcecode:: plain

    /set beep_msg_level NOTICE MSGS HILIGHT
    /set bell_beeps OFF

You can save this configuration permanently by issueing ``/save``.

2. In your ~/.screenrc, add the following lines:

.. sourcecode:: plain

    vbell off
    bell_msg 'Bell in window %n^G'

3. Tell your terminal to set the URGENT flag when beeping. Add one of
the following lines to your .Xresources:

.. sourcecode:: plain

    # For UXterm users:
    UXTerm*bellIsUrgent: true

    # For (u)rxvt users:
    Rxvt.urgentOnBell: true


