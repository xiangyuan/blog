public: yes
tags: [Linux]

XBindKeys und Amarok - Zusätzliche Mausbuttons unter Linux
==========================================================

Ich habe mich schon öfters mit dem Thema "Zusätzliche Mausbuttons unter
Linux" (genauer gesagt ein Tiltwheel einer Logitech RX250 Maus) befasst,
da ich gerne die Play/Pause Taste auf nach-links-kippen und das nächste
Lied auf nach-rechts-kippen gemappt habe. Bei Windows geht das über das
mitgelieferte Logitech-Tool, Linux findet von denen allerdings nicht
allzugrosse Beachtung.

In meinem neu installierten Fedora wurden zu meiner grossen Freude die
Tiltwheel-Actions von Anfang an richtig erkannt; unter openSUSE war das
immer ein grosses Gebastel. Deshalb werde ich nicht genauer auf die
Treiberkonfiguration etc eingehen, wer Hilfe braucht wird am besten auf
`Google <http://google.ch/>`_ fündig. Nun denn, um die Button-ID
herauszufinden benutzt man am besten das Tool
`xev <http://www.xfree86.org/current/xev.1.html>`_. Bei mir waren
Button-IDs 6 und 7.

``ButtonRelease event, serial 30, synthetic NO, window 0x4a00001,     root 0x13b, subw 0x0, time 2501157, (129,75), root:(132,121),     state 0x10, button 6, same_screen YES``
``ButtonPress event, serial 30, synthetic NO, window 0x4a00001,     root 0x13b, subw 0x0, time 2503789, (129,75), root:(132,121),     state 0x10, button 7, same_screen YES``

Mithilfe dieser Button-Codes kann man jetzt den Event auf einen
Shell-Befehl mappen. Dies geht am besten mithilfe des Pakets
`XBindKeys <http://http://hocwp.free.fr/xbindkeys/xbindkeys.html>`_,
welches vermutlich in den jeweiligen Distro-Repos bereits enthalten ist.
Bei Fedora und openSUSE war das jedenfalls der Fall...

Bevor man das Tool zum ersten mal startet sollte man noch eine
Konfigurationsdatei anlegen. Dies geht ganz einfach mit dem Befehl
``xbindkeys --defaults > ~/.xbindkeysrc``. Dann muss die
Konfigurationsdatei noch an die persönlichen Bedürfnisse angepasst
werden. Öffne die neu erstellte Datei ~/.xbindkeysrc mit dem Editor
deiner Wahl (am besten mit `vim <http://www.vim.org/>`_, alle andern
sind böse... :evil: :wink: ).

``vim ~/.xbindkeysrc``

Die Konfigurationsdatei ist recht gut dokumentiert, somit sollte es kein
Problem sein die Mausbuttons zu konfigurieren. Als erstes sollten mal
alle vorhandenen Konfigurationen auskommentiert werden um unerwartete
Dinge zu vermeiden (wie z.B. dass control+f plötzlich auf eine konsole
gemappt ist... :roll: ). Um `amarok <http://amarok.kde.org/>`_
anzusteuern habe ich `dcop <http://http://en.wikipedia.org/wiki/DCOP>`_
verwendet. Um alle Möglichkeiten von dcop + amarok zu sehen am besten in
der Konsole einfach ``dcop amarok`` eintippen.

Ich habe meiner .xbindkeysrc folgende Zeilen angehängt:

``# Amarok Next and Pause/Play "dcop amarok player playPause" b:6 "dcop amarok player next" b:7``
``# Amarok Volume Control "dcop amarok player volumeDown" Control + b:6 + Release "dcop amarok player volumeUp" Control + b:7 + Release``

Nach dem Speichern in der Konsole ``xbindkeys`` eingeben und schon gehts
los! Jetzt muss xbindkeys nur noch automatisch gestartet werden. Unter
Gnome geht das unter System->Einstellungen->Persönlich->Sitzungen, unter
KDE muss man dazu einen Symlink nach ~./kde/Autostart/ erstellen. Dies
geht ganz einfach mit
``ln -s /usr/bin/xbindkeys ~./kde/Autostart/xbindkeys``.

Viel Spass, für Kommentare und/oder Anregungen bitte Kommentarfunktion
nutzen :)

