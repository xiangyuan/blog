public: yes
tags: [Ubuntu,Linux,Internet]

Pidgin MSN - "Zertifikat omega.contacts.msn.com konnte nicht validiert werden"
==============================================================================

(English: To fix Pidgin, update it.
`Ubuntu <http://pidgin.im/download/ubuntu/>`_ /
`Windows <http://pidgin.im/download/windows/>`_.)

Seit ein paar Tagen kann man sich mit Pidgin nicht mehr im MSN
einloggen, stattdessen kommt die folgende Meldung:

    Kann Zertifikat nicht validieren Das Zertifikat für
    omega.contacts.msn.com konnte nicht validiert werden. Die
    präsentierte Zertifizierungskette ist ungültig.

Um dieses Problem zu beheben muss man entweder manuell das aktualisierte
Zertifikat installieren, oder Pidgin updaten. Leider wird Pidgin unter
Ubuntu nur bei Sicherheitsupdates aktualisiert. Abhilfe schafft
folgendes Vorgehen:

Ubuntu
~~~~~~

#. Das `Pidgin
   PPA <https://launchpad.net/~pidgin-developers/+archive/ppa/+files/pidgin-ppa_0.0.3_all.deb>`_
   herunterladen
#. .deb-Datei öffnen und mit dem GDebi Installier installieren
#. Eine Konsole öffnen und
   ``sudo apt-get update && sudo apt-get upgrade`` eingeben

Daraufhin wird Pidgin aktualisiert und sollte wieder funktionieren.

Windows
~~~~~~~

Unter Windows kann man Pidgin wie gewohnt
`herunterladen <http://pidgin.im/download/windows/>`_ und
installieren/updaten.

