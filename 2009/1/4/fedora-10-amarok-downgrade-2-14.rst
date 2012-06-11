public: yes
tags: [Musik,Linux]

Fedora 10 Amarok Downgrade (2 > 1.4)
====================================

Geht es anderen auch so wie mir? Monatelang habe ich mich auf die
Version 2 des genialen Musikplayers `Amarok <http://amarok.kde.org/>`_
gefreut. Jetzt mit `Fedora 10 <http://fedoraproject.org/>`_ ist sie da,
und sie - vorsicht: subjektive Meinung - stinkt. Ich finde die neue
Oberfläche unübersichtlich, hässlich, das Mysql-Backend wurde zugunsten
eines Mysql-Embedded-Backends gekippt... Eine kleine Odysee begann, ich
hab mich durch diverse Musikplayer durchprobiert, aber
`Rhythmbox <http://projects.gnome.org/rhythmbox/>`_ war mir zu simpel,
`Listen <http://www.listen-project.org/>`_ konnte innerhalb eines Liedes
nicht vorspulen,
`mpd <http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki>`_ +
`ncmpc <http://mpd.wikia.com/wiki/Client:Ncmpc>`_ boten zu wenig
Features, `mplayer <http://www.mplayerhq.hu/>`_ beinhaltet keine
Verwaltungsmöglichkeiten,
`LAMIP <http://fondriest.frederic.free.fr/realisations/lamip/>`_ ist
noch zu 'alpha', `Quod Libet <http://code.google.com/p/quodlibet/>`_
gefällt mir irgendwie nicht... Schlussendlich entschloss ich mich, zu
Amarok 1.4.10 zurück zu wechseln. Doch das war leichter gesagt als
getan... In den offiziellen Repos war nur noch die neue Version
enthalten. Schlussendlich bin ich über einen
`Thread <http://www.fedoraforum.de/viewtopic.php?f=9&t=16782>`_ im
Fedoraforum gestossen, welcher mir weitergeholfen hat.

Downgrade
~~~~~~~~~

Zuerst sollte man eine allfällig installierte Version von Amarok 2
deinstallieren.

::

    sudo yum remove amarok*

Dann die neusten RPMs von
`deadbabylon <http://www.deadbabylon.de/fedora/amarok/>`_ herunterladen
(i386 oder x86\_64). Für mich waren das *amarok-1.4.10-1.fc10.i386.rpm*
und *amarok-visualisation-1.4.10-1.fc10.i386.rpm* vom 14.12.2008.

::

    wget http://www.deadbabylon.de/fedora/amarok/amarok-1.4.10-1.fc10.i386.rpm
    wget http://www.deadbabylon.de/fedora/amarok/amarok-visualisation-1.4.10-1.fc10.i386.rpm

Bevor man diese Version installiert, sollte man Amarok 1.9 und 2 aus den
Repos excluden, dazu *exclude=paketname* an die yum.conf-Datei anhängen.
Dann mit *yum localinstall* installieren.

::

    su -c "echo 'exclude=amarok-1.9* amarok-2*' >> /etc/yum.conf"
    sudo yum --nogpgcheck localinstall amarok-1.* amarok-visualisation-1.*

Damit Amarok auch MP3-Files abspielen kann, benötigt es noch die
nicht-freien Xine-Pakete.

::

    sudo yum install xine-lib-extras xine-lib-extras-freeworld

Jetzt sollte alles soweit funktionieren.

Weitere Tipps
~~~~~~~~~~~~~

-  Ich speichere meine Amarok-Datenbank nicht in einer
   SQLight-Datenbank, sondern auf einem lokalen MySQL-Server. Somit kann
   ich mir z.B. eine lokale PHP-Seite mit diversen Abfragen erstellen,
   z.B. für eine Liste der Alben, die ich auf dem PC habe.
-  Wer Amarok fernsteuern will, kann dies mithilfe von dcop tun. Ein
   Artikel dazu `gab es hier
   schonmal </2008/06/xbindkeys-und-amarok-zusatzliche-mausbuttons-unter-linux/>`_...

Fazit
~~~~~

Ich warte immer noch auf einen Linux-Port von
`foobar2000 <http://www.foobar2000.org/>`_. Oder einem Gnome-Musikplayer
mit ähnlichem Funktionsumfang wie Amarok.

**Update 08.11.2011:** Seit einigen Monaten benutze ich
`Clementine <http://www.clementine-player.org/>`_. Coole Alternative,
inspiriert von Amarok 1.4. Wenn man die Konsole mag, kann man auch gut
`Herrie <http://herrie.info/>`_ benutzen.

