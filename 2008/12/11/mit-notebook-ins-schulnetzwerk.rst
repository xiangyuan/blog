public: yes
tags: [Internet]

Mit Notebook ins Schulnetzwerk
==============================

Im Wahlpflichtfach Fotografie, an welchem ich teilnehme, arbeiten wir
zwei Drittel der Zeit selbständig am Computer (digitale
Bildbearbeitung). Ich habe jeweils mein Notebook dabei, damit ich mit
Photoshop statt Gimp arbeiten kann. Nur leider konnte ich nie eine
Netzwerkverbindung aufbauen, wenn ich das Ethernet-Kabel des PCs im
Laptop eingesteckt habe - mir wurde vom DHCP keine IP zugewiesen. Mein
Verdacht fiel auf eine MAC-Filterung, was ich dann prompt mal
ausprobiert habe. Nach kurzer Recherche im Internet habe ich
herausgefunden, wie ich auf meinem Ubuntu-Notebook die MAC-Adresse des
PCs vortäuschen kann (MAC-Spoofing). Zuerst muss man den
Ethernet-Adapter deaktivieren. Vorausgesetzt die Netwerkkarte ist eth0:

::

    ifconfig eth0 down

Dann kann man mittels ifconfig die neue MAC-Adresse setzen (zur
Sicherheit die alte Identifikation irgendwo noch zwischenspeichern, ich
weiss nicht ob man die resetten kann.)

::

    ifconfig eth0 hw ether 01:23:45:67:89:ab

Dann die Netzwerkkarte wieder starten.

::

    ifconfig eth0 up

Um die Hardwareadresse des PCs herauszufinden, bin ich mit dem Windows
Explorer bis ins c:\\windows\\system32 Verzeichnis navigiert, und habe
command.com gestartet (Start-Ausführen war gesperrt). Als ich die
Netzwerkkarte unter Linux gestartet habe, konnte ich nach etwa 20
Sekunden tatsächlich eine Verbindung herstellen, und mir wurde die selbe
IP zugewiesen wie vorher dem stationären PC. Der Verdacht hat sich also
bestätigt.

Auf Google konnte ich jetzt ein Ping absetzen, Surfen konnte ich jedoch
noch nicht, da anscheinend der Internetzugang vom Proxy auf den Internet
Explorer eingeschränkt war. Ich hätte jetzt vermutlich meinem Firefox
den Useragent-String des Internet Explorers zuweisen können, aber dann
hätte ich immer noch den filternden Proxy dazischen gehabt. Deshalb habe
ich mich für einen (hier schon mehrmals erwähnten) SSH Tunnel
entschieden. Mit folgendem Shell-Befehl erstellt man einen SOCKS-Proxy
auf dem Port 1119 (beliebig wählbar), welcher verschlüsselt über einen
SSH-Server getunnelt wird.

::

    ssh -D 1119 user@server.tld

In den Firefox-Netwerkeinstellungen kann man dann localhost:1119 als
SOCKS5-Proxy einsetzen, und voilà, ich hab freie Bahn ins Internet.

