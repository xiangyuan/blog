public: yes
tags: [vim]

Einfügen in Vim
===============

Häufig finde ich auf einer Website Codestücke und will die in `Vim <http://vim.org/>`_ einfügen.
Jedoch passiert es mir dann immer wieder dass es jede neue Zeile um einen Tab weiter einrückt. Die
erste Zeile ist nicht eingerückt, die zweite Zeile hat ein Tab davor, die Dritte hat zwei, die 20ste
Zeile hat 19 vorangehende Tabs... Das ist sehr nervig. Die Lösung:

.. sourcecode:: vim

    :set paste

Und schon kann der Code ganz normal eingefügt werden. Wenn man mit Einfügen fertig ist kann das
normale Verhalten mit

.. sourcecode:: vim

    :set nopaste

wiederhergestellt werden.

(Quelle: `blog.exeko.com <http://blog.exeko.com/2007/12/23/debian-vi-disable-autoindent-when-pasting/>`_)
