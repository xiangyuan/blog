public: yes
tags: [Linux]

DWM ssh/screen/irssi notifications 
===================================

I always keep an irssi session open inside a screen session on my server
via ssh. I always thought that notifications aren't possible for such a
setup. But they are.

1. In your irssi session, issue the following commands:

::

    /set beep_msg_level NOTICE MSGS HILIGHT
    /set bell_beeps OFF

You can save this configuration permanently by issueing ``/save``.

2. In your ~/.screenrc, add the following lines:

::

    vbell off
    bell_msg 'Bell in window %n^G'

3. Tell your terminal to set the URGENT flag when beeping. Add one of
the following lines to your .Xresources:

::

    # For UXterm users:
    UXTerm*bellIsUrgent: true

    # For (u)rxvt users:
    Rxvt.urgentOnBell: true


