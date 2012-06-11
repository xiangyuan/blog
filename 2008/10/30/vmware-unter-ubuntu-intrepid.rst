public: yes
tags: [Linux]

VmWare unter Ubuntu Intrepid
============================

Ubuntu Intrepid Ibex 8.10 ist draussen. Und bringt den neuen Kernel
2.6.27-7 mit, welcher meiner Wlan-Karte den Lebensatem einhaucht. Leider
funktioniert damit VmWare nicht mehr... Bei der re-kompilierung der
Kernel-Module spuckte mir der PC jedes mal einen Fehler aus. Dies hat
zum Glück - pünktlich vor dem morgigen Schulbeginn - mit einem
`Patch <http://www.insecure.ws/2008/10/20/vmware-specific-specific-55x-and-kernel-2627>`_
ein Ende. Auf
`simplylinux.ch <http://www.simplylinux.ch/vmware-server-auf-ubuntu-810-intrepid-ibex/>`_
gibt es zudem ein deutsches Howto für Leute welche in Sachen Linux noch
nicht so bewandert sind.

Kleiner Wermutstropfen: Die Mappings einiger Funktionstasten (wie
Pfeiltasten, Ctrl, und Shift) werden aus unerfindlichen Gründen sowohl
in der Virtuellen Maschine als auch auf dem Hostsystem deaktiviert. Ich
hoffe dass ich dafür auch bald eine Lösung finde...

Ein Post zu Ubuntu Ibex und Linux allgemein folgt wohl später mal.

Nachtrag:
~~~~~~~~~

Mit der aktuellen VmWare-Player-Version 2.5.1-126130 und
`dieser <http://nthrbldyblg.blogspot.com/2008/06/vmware-and-fubar-keyboard-effect.html>`_
Anleitung (Solution 3), hats bei mir endlich auch geklappt. Hinweis: Ich
musste vorher die aktuell installierte VmWare-Version deinstallieren,
und alle Konfigurationsdateien unter /etc/vmware löschen. Dann habe ich
den Player installiert und /etc/vmware/config angepasst, und dann
funktionierte das Ganze.

