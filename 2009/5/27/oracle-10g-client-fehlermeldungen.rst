public: yes
tags: [sysadmin]

Oracle 10g Client Fehlermeldungen
=================================

Wenn folgende Fehlermeldung beim Verbinden auf die Datenbank erscheint:

.. sourcecode:: plain

    ORA-00604: Fehler auf rekursiver SQL-Ebene 1
    ORA-02248: Ungültige Option für ALTER SESSION

Dann muss folgende System-Umgebungsvariable gesetzt werden:

.. sourcecode:: bash

    NLS_NUMERIC_CHARACTERS=.,

(Bäh, ich hasse Oracle)
