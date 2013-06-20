public: yes
tags: [sysadmin, android]

Install Android Development Environment under Arch Linux
========================================================

How to install Eclipse and the Android Developer Tools under ArchLinux
x64:

#. ``sudo pacman -S eclipse``
#. ``yaourt -S android-sdk eclipse-android``
#. ``sudo usermod --groups android <user>``
#. Log out and back in (to update your permissions)
#. Open Eclipse, select *Window > Preferences*, select *Android* on the
   left side.
#. Choose ``/opt/android-sdk`` as your SDK location and click on *Apply*
#. Select *Window > Android SDK and AVD Manager*
#. Choose *Available Packages* on the left side
#. Install at least the *Android SDK Platform-tools* and your desired
   Platform

That's it, the Android developer tools should now be usable.
