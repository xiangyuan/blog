public: yes
tags: [Internet]

VLC mit SSH Tunnel
==================

Heute wollte ich mich im Büro ein wenig mit
`Longplayer <http://longplayer.org/>`_ beschallen lassen. Seite öffnen,
m3u-File herunterladen, abspielen!...
 ...dachte ich. Port 8010 für Streaming war gesperrt.

Nun ja, es gibt fast kein Problem welches sich nicht mit einem SSH
Tunnel lösen lässt. Da ich ja für `andere
Anwendungsbereiche </2008/03/firewall-umgehen-mit-ssh/>`_ bereits eine
SSH Verbindung auf meinen Server laufen habe, sollte das keine
schwierige Sache sein.

Und tatsächlich. Ich hatte bereits einen SOCKS-Port offen
(*Putty->SSH->Tunnels->Source Port angeben, Dynamic, Auto*), welchen man
auch für VLC benutzen kann.

`|image0| <http://blog.ich-wars-nicht.ch/wp-content/uploads/2008/09/putty-dynamic-port.jpg>`_

Jetzt noch den SOCKS-Server in VLC auf localhost:port setzen, und schon
lässt sich alles streamen was das Herz begehrt!

`|image1| <http://blog.ich-wars-nicht.ch/wp-content/uploads/2008/09/vlc-socks.jpg>`_

Achja, ein SOCKS-Server lässt sich auch bei Firefox(-portable) setzen,
und zwar unter
*Extras->Einstellungen->Erweitert->Netzwerk->Einstellungen->Manuell->SOCKS-Host*.
Und schon kann man ohne Firewall-Einschränkungen durchs Web flitzen,
z.B. in der Schulbibliothek ;)

Viel Spass

.. |image0| image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2008/09/putty-dynamic-port.jpg
.. |image1| image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2008/09/vlc-socks.jpg

