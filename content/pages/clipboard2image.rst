Clipboard2Image
===============

:slug: clipboard2image
:comments: yes

Wer häufig beispielsweise Bilder aus Word-Dokus oder ähnlichen Quellen in
Dateien abspeichern muss, kennt den mühsamen Workflow: *Kopieren > Win+R >
mspaint+Enter > Ctrl+V > Datei > Speichern > Dateityp ändern > Done*. Ich
dachte, das müsse doch einfacher gehen. Basierend auf diesem Artikel habe ich
mir daher ein Tool in C# geschrieben.

Das Tool speichert Bilddaten aus der Zwischenablage direkt auf den Desktop oder
in einen gewählten Ordner. Unterstützte Dateitypen: png, jpg, gif, bmp.

Bestandteile
------------

- **Clipboard2Image.exe** – GUI-Version des Programms mit Vorschaufunktion
- **c2i.exe** – Kommandozeilenversion des Programms

Voraussetzungen
---------------

- Microsoft Windows
- Microsoft .NET Framework 2.0 oder höher

Installation
------------

Herunterladen, in einen beliebigen Ordner kopieren, Verknüpfung auf Desktop oder
Schnellstartleiste erstellen, bei Bedarf Tastenkombination zuweisen, fertig.

Um die Kommandozeilenversion des Programms einfacher aufrufen zu können, einfach
den Ordnerpfad von c2i.exe zur PATH-Systemvariable hinzufügen.

Screenshots
-----------

Clipboard2Image.exe:

.. image:: /static/img/pages/clipboard2image_v1.4.png
    :alt: Screenshot Clipboard2Image

c2i.exe:

.. image:: /static/img/pages/c2i_v1.1.png
    :alt: Screenshot c2i.exe

Hinweise
--------

Das Ganze funktioniert auch prima um Screenshots zu speichern.

Download
--------

https://github.com/downloads/dbrgn/Clipboard2Image/Clipboard2Image_v1.4.zip

Lizenz
------

Der Sourcecode dieses Tools steht unter der GPLv3 Lizenz. Bei Nutzung würde ich
mich über einen Kommentar oder ein Feedback freuen.

Sourcecode
----------

Der Sourcecode kann jederzeit auf Github eingesehen werden. Wer will darf
natürlich auch gerne Verbesserungen daran vornehmen, und mir auf Github einen
Pull Request senden.

https://github.com/dbrgn/Clipboard2Image
