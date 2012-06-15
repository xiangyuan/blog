public: yes
tags: [Gentoo, Linux, Xorg]

Unvollständiges CH-Tastaturlayout
=================================

Seit Tagen hatte ich unter Gentoo einen nervigen Bug - das Schweizer Tastaturlayout unter Xorg
funktionierte zwar teilweise, aber Tasten wie AltGr, die Klammern, oder die Umlaute blieben tot.
Nach einigem Basteln habe ich dann dank `Junya
<http://blog.h2o.ch/archives/10-Deutschweizer-Tastatur-Umlaute-unter-Ubuntu.html>`_ das Problem
gefunden: Die `xorg.conf`-Option ``XkbVariant`` war bei mir nicht richtig konfiguriert. Das Ganze
sollte am Schluss so aussehen:

.. sourcecode:: xorg

    Section "InputDevice"
      Identifier     "Keyboard0"
      Option         "XkbModel" "pc105"
      Option         "XkbLayout" "ch"
      Option         "XkbVariant" "de"
      Driver         "kbd"
    EndSection
