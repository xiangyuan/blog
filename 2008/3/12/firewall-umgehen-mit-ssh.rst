public: yes
tags: [internet]

Firewall umgehen mit SSH
========================

Wer kennt das nicht? Im Büro, in der Schule, oder sonstwo sind bestimmte
Firewallports gesperrt, und man kann diverse Dienste nicht verwenden.  Bei uns
im Geschäft ist das neuerdings der Fall. Mit einer neuen Firewall wurden auch
neue Ports gesperrt. Kein MSN mehr, kein IMAP über Port 993 (Gmail)... Das hat
gewaltig genervt. Ich habe mich darum umgeschaut und eine Lösung gefunden: `SSH
Tunnelling <http://de.wikipedia.org/wiki/Tunnel_(Netzwerktechnik)>`_.

Als erstes braucht man Zugang zu einem beliebigen SSH Server ausserhalb der
Firewall. Dies kann z.B.  eine Linux-Workstation mit installiertem OpenSSH
sein... Auch einige Webhoster bieten SSH Zugang, teilweise muss man nur mal
freundlich nachfragen. Was man jedoch beachten sollte ist dass je tiefer die
Upload-Geschwindigkeit des SSH Servers desto langsamer wird das ganze sein (die
Daten die man downloadet müssen ja vom Server geuploadet werden...). Auf eine
allfällige SSH Konfiguration gehe ich hier nicht ein, eine Überprüfung der
Sicherheitseinstellungen ist bei einem eigenen Server aber unerlässlich.

Anschliessend braucht man einen SSH Client. In diesem Beispiel verwende ich
`PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_, ein
sehr empfehlenswertes Programm. Hinweis: PuTTY gibt es auch als `Portable
Edition <http://portableapps.com/apps/internet/putty_portable>`_ für den USB
Stick...

Als erstes muss man in PuTTY die Verbindungseinstellungen zum SSH Server
festlegen.

.. image:: /static/img/2008/3/12/putty_screenshot_1.png
    :alt: PuTTY Screenshot

Dann müssen die verschiedenen Tunnels definiert werden. Beispiel 1: Gmail IMAP
Zugang über Port 993.  Unter Connection>SSH>Tunnels als Source Port einen
beliebigen freien Port wählen (in meinem Beispiel Port 88).  In das
Destination-Feld kommt "imap.google.com:993", und die Optionen werden auf
"Local" und "Auto" gesetzt. Beispiel 2: Windows Live Messenger. Unter Source
Port einen beliebigen freien Port wählen (in meinem Beispiel Port 89). Das
Destination-Feld bleibt leer. Die Optionen werden auf "Dynamic" und "Auto"
gesetzt.

.. image:: /static/img/2008/3/12/putty_screenshot_2.png
    :alt: PuTTY Screenshot

Um die Verbindung aufzubauen muss man jetzt nur noch auf "Open" klicken und das
Passwort eingeben.  Das PuTTY Konsolenfenster muss die ganze Zeit geöffnet
bleiben um die Verbindung aufrechtzuerhalten.

Jetzt müssen nur noch die Programme konfiguriert werden. Für IMAP: Unter Outlook
in den Konteneinstellung als Postausgangs-Serverport den selben Port wie vorhin
wählen, in meinem Beispiel 88.

.. image:: /static/img/2008/3/12/outlook_screenshot_1.png
    :alt: Outlook Konfiguration 1

Dann den Postausgangsserver von `imap.gmail.com` zu `127.0.0.1` ändern (oder
alternativ "localhost").

.. image:: /static/img/2008/3/12/outlook_screenshot_1.png
    :alt: Outlook Konfiguration 1

Das wars, IMAP sollte jetzt funktionieren. Jetzt noch zu Windows Live Messenger:
In den Optionen unter Verbindung>Erweiterte Einstellungen den SOCKS Proxy auf
127.0.0.1 (bzw "localhost") und den Port auf den entsprechenden Wert setzen,
Messenger neu starten, und schon funzt die ganze Sache!  Speziell in Verbindung
mit der Transparenz-Funktion und dem Bosskey von `Messsenger Plus!
<http://www.msgpluslive.net/>`_ enorm nützlich! ;)

.. image:: /static/img/2008/3/12/livemessenger_screenshot_1.png
    :alt: Live Messenger Konfiguration

Ich hoffe mit diesem Post einigen Leuten helfen zu können. Für Feedback ist die
Comment-Funktion zuständig. Viel Spass!

**Nachtrag:** Auf `bylur.net <http://www.bylur.net/free/>`_ und `red-pill.eu
<http://www.red-pill.eu/freeunix.shtml>`_ gibt es grosse listen mit freien
Unix-Shell Servern. Es muss darauf geachtet werden dass der Server SSH
unterstützt. Meistens muss man aber für einen Account dem Besitzer des Servers
eine Postkarte senden (ja, per Post, das ist diese Firma die diese
handbeschriebenen Papiere transportiert...) oder etwas spenden, das erscheint
mir angebracht, ohne Gegenleistung würde ich auch niemandem einen Server
bereitstellen ;) Also sucht euch ein sympathisches Angebot aus und schickt ne
Postkarte... Dann sind alle glücklich ;)
