public: yes
tags: [Webdesign]

No code was created for this art in this category
=================================================

Heute tauchte bei der Arbeit mit dem CMS
`Contenido <http://www.contenido.org/>`_ (mit welchem ich schon so oft
meine Probleme hatte) nach dem Einrichten eines neuen Mandanten immer
wieder die Fehlermeldung "*No code was created for this art in this
category*\ " auf. Die Lösung habe ich dann glücklicherweise auf der
`Website der TU
Darmstadt <https://wcms.tu-darmstadt.de/test/contenido.html>`_ gefunden:

    Der Fehler "No code was created for this art in this category."
    tritt immer wieder auf Hierbei hat - aufgrund von internen
    Verwicklungen - Contenido die falsche ID des Clients (Mandanten) in
    die Konfigurationsdatei des Mandaten (in dem Verzeichnis des
    Mandaten) namens "config.php" gelegt: $load\_client = "12345";.
    Diese Mandantenzahl einfach anhand der Datenbanktabelle
    "con\_clients" händisch ermitteln in in die Konfigurationsdatei
    eintragen.

Und damit war das Problem gelöst.

