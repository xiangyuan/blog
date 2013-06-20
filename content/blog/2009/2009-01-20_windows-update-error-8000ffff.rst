public: yes
tags: [windows]
language: de

Windows Update Error 8000FFFF
=============================

Nach zwei Tagen Kampf mit der Installation des neuen Visual Studio 2008 unter Windows Vista (x86)
dachte ich mir, es wäre vielleicht mal gut wenn ich alle Updates installieren würde – vielleicht
krieg ich dann VS2008 endlich auf meinen Computer. Und als ich mal den Update-Verlauf ansah,
bemerkte ich dass Vista seit November keine Updates mehr gemacht hatte... Wollte ich dies manuell
machen, dann kam immer die Fehlermeldung "Windows Updates konnten nicht installiert werden", und der
Fehlercode ``8000FFFF``... Nach einigem Suchen im Internet fand ich in einem `Technet-Forum
<http://social.technet.microsoft.com/forums/en-US/itprovistasecurity/thread/6b9f6a7c-1b91-422f-a803-11440418008f/>`_
eine Lösung die bei mir funktionierte:

#. REGEDIT mit Administratorrechten ausführen
#. Unter HKLM\\COMPONENTS prüfen, ob die folgenden Werte existieren:

   -  PendingXmldentifier
   -  NextQueueEntryIndex
   -  AdvancedInstallersNeedResolving

#. Falls sie existieren, zuerst den Schlüssel sichern, und die Werte dann löschen.
#. Computer neu starten, und das Update sollte funktionieren.

Sollte dies nicht funktionieren, gibt es auch noch die in Foren viel erwähnte Methode, den Patch
``KB922750`` – falls installiert – zu deinstallieren, und manuell von der Update-Seite wieder zu
installieren.  Bei mir war das betreffende Update jedoch gar nicht installiert.
