public: yes
tags: [webdev]

Website Checkliste
==================

Eine kleine, spontane Checkliste, damit man nicht nach der Fertigstellung einer Website einige
dieser häufig übersehenen Punkte vergisst:

Valides (X)HTML und CSS
^^^^^^^^^^^^^^^^^^^^^^^

Der Quellcode kann mit dem `HTML-Validator <http://validator.w3.org/>`_ / `CSS-Validator
<http://jigsaw.w3.org/css-validator/>`_ des W3C Konsortiums überprüft werden.

Einheitliches Design
^^^^^^^^^^^^^^^^^^^^

Verwenden alle Überschriften den selben Tag? Ist CSS sinnvoll eingesetzt? Sehen alle Seiten etwa
gleich aus?

Browserkompatibilität
^^^^^^^^^^^^^^^^^^^^^

Seite in mehreren Browsern testen. Eine Hilfe dazu kann der Onlinedienst `browsershots.org
<http://browsershots.org/>`_ sein.

Lesbarkeit / Skalierbarkeit
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ist die Seite auch auf kleineren Bildschirmen gut lesbar? Wie sieht das Ganze bei einer Auflösung
von 800x600 aus? Wie sieht das Layout aus wenn die Schriftgrösse skaliert wird?

Impressum
^^^^^^^^^

Ist ein Impressum vorhanden? In Deutschland und der Schweiz gilt Impressumspflicht.

Rechtschreibung
^^^^^^^^^^^^^^^

Inkorrekte Rechtschreibung macht einen schlechten Eindruck.

Reintextlayout
^^^^^^^^^^^^^^

Wie sieht die Seite in einem Text-Only-Browser wie `lynx
<http://de.wikipedia.org/wiki/Lynx_(Browser)>`_ oder `links
<http://de.wikipedia.org/wiki/Links_(Browser)>`_ aus? Wie sieht sie aus wenn alle Bilder deaktiviert
wurden? (Ist nicht direkt relevant, aber kann ein Rolle spielen wenn die Seite maschinell analysiert
wird, zB von einem screenreader. Siehe auch nächsten Abschnitt zu Accessibility.)

Accessibility
^^^^^^^^^^^^^

Sind alle Bilder mit Alt-Tags versehen? Ist die Seite ohne JavaScript nutzbar? Wie stehts für
Analog-Modemnutzer? Weitere Infos z.B. auf der Seite der `Web Accessibility Initiative
<http://www.w3.org/WAI/>`_ oder auf der `Checkliste zu barrierefreien Webseiten
<http://www.ch.ch/hilfe/01696/01698/>`_ von ch.ch.

Drucklayout
^^^^^^^^^^^

Wie sehen die Seiten aus wenn sie ausgedruckt werden? Evt.  `CSS-Drucklayout
<http://aktuell.de.selfhtml.org/artikel/css/drucklayout/>`_ erstellen.

Mobiles Layout
^^^^^^^^^^^^^^

Ist die Seite von mobilen Geräten aus nutzbar? Der `W3C mobileOK Checker
<http://validator.w3.org/mobile/>`_ könnte bei diesem Punkt eine Hilfe sein.

Links überprüfen
^^^^^^^^^^^^^^^^

Sind links aussagekräftig? Texte wie "hier klicken" `sind nicht besonders aussagekräftig
<http://d135-1r43.de/2005/12/14/klicken-sie-hier/>`_ und sollten vermieden werden. Zudem sollten
alle Links `überprüft <http://validator.w3.org/checklink>`_ werden.

Hineweis auf Autor / Kontaktmöglichkeit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es ist für den Nutzer sehr mühsam, wenn er keine Möglichkeit findet, den Autor einer Website zu
kontaktieren. Abhilfe schafft z.B. ein Impressum mit Kontaktadresse, ein Kontaktformular, oder
sonstige Kontakthinweise.

Newsfeed
^^^^^^^^

Falls die Seite regelmässig aktualisierten Inhalt hat, ist ein RSS/Atom-Newsfeed empfehlenswert.

Speedtest
^^^^^^^^^

Wie schnell ist die Seite? Wo gibt es Blocker? Dies kann man z.B. mit dem "Netzwerk"-Tab von
`Firebug <http://getfirebug.com/>`_ oder über die Firebug-Erweiterung `Google Page Speed
<http://code.google.com/intl/de-DE/speed/page-speed/>`_ oder `YSlow
<http://developer.yahoo.com/yslow/>`_.
