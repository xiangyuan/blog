public: yes
tags: [Gentoo,Linux]

Eclipse + Xulrunner
===================

When emerging eclipse-sdk-3.2.1 under gentoo (or maybe also on other
distributions), you may notice the following error message when trying
to start it for the first time:

Popup:

::

    JVM terminated. Exit code=127
    /usr/bin/java
    -jar /usr/lib/eclipse-3.2/startup.jar
    -os linux
    -ws gtk
    -arch x86
    -launcher /usr/lib/eclipse-3.2/eclipse
    -name Eclipse
    -showsplash 600
    -exitdata ff002d
    -vm /usr/bin/java
    -vmargs
    -jar /usr/lib/eclipse-3.2/startup.jar

Shell output:

::

    /usr/lib/jvm/sun-jdk-1.6/bin/java: symbol lookup error:
    /home/danilo/.eclipse/org.eclipse.platform_3.2.0/configuration/org.eclipse.osgi/bundles/
    16/1/.cp/libswt-mozilla-gtk-3235.so: undefined symbol: _ZN4nsID5ParseEPKc

After some research in the internet, I finally found that the problem
(in my case) was xulrunner. I couldn't just remove xulrunner though, as
it is a dependency of mozilla-firefox. The solution was to remove
xulrunner, and to rebuild the mozilla-firefox package with the xulrunner
USE-flag turned off.

::

    emerge --unmerge xulrunner
    echo 'www-client/mozilla-firefox -xulrunner' >> /etc/portage/package.use
    emerge -av mozilla-firefox

After that, you should be able to start Eclipse without the previous
error messages.

**Update:** An even better solution to use eclipse is to unmask
eclipse-3.3 in your package.keywords, and to use that version instead of
3.2... Apparently the above error is a bug in the eclipse-3.2-ebuild.

