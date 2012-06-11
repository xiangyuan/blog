public: yes
tags: [sysadmin]

Platzfresser in der Linux Shell finden
======================================

Um in der Linux Shell die 10 grössten Platzfresser im aktuellen Verzeichnis zu finden, füge
folgenden Alias deiner `~/.bashrc` hinzu:

.. sourcecode:: bash

    alias ducks='du -cks * | sort -rn | head -11'

Resultat: Eine schöne, übersichtliche Liste, die den
Total-Platzverbrauch wie auch die zehn grössten Speicherfresser
auflistet.

.. sourcecode:: bash

    danilo@srv:/bin$ ducks
    3768    insgesamt
    692     bash
    236     tar
    196     ip
    152     nano
    112     cpio
    108     netstat
    104     grep
    96      vdir
    96      ls
    96      egrep

**Quelle:** Linux Server Hacks, O'Reilly, 2003, ISBN 3-89721-361-3
