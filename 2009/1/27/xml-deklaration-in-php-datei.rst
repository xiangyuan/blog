public: yes
tags: [PHP, XML]

XML Deklaration in PHP Datei
============================

Wer schonmal eine XML-Deklaration in einer PHP-Datei *ausserhalb* der PHP Tags (``<?php ?>``)
gemacht hat, weiss, dass es damit Probleme geben kann. Wenn nämlich die PHP Short Tags (``<? ?>``)
auf dem Server aktiviert sind, dann interpretiert der Parser die ersten zwei Zeichen der
XML-Deklaration als Parse-Startpunkt. Und gibt einen Syntax Error aus.

.. sourcecode:: xml

    <?xml version="1.0" encoding="utf-8"?>

Um dies zu verhindern, muss man lediglich die Zeichenfolge ``<??>`` zwischen öffnende Klammer und
Fragezeichen einfügen, und schon wird es vom Parser korrekt behandelt.

.. sourcecode:: php

    <<??>?xml version="1.0" encoding="utf-8"?>
