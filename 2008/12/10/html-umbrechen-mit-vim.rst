public: yes
tags: [vim]

HTML Umbrechen mit VIM
======================

Unser CMS am Arbeitsplatz hat irgend einen Bug, der bewirkt, dass die Codeansicht von Artikeln auf
unserer Webseite so ganz ohne Zeilenumbrüche daherkommt. Eine einzelne Zeile kann man leider nicht
gut bearbeiten, aber zum Glück kann man mit `VIM <http://www.vim.org/>`_ die Zeile jeweils nach
einem schliessenden HTML-Tag umbrechen:

.. sourcecode:: vim

    :%s/\(<\/\a*>\)/\1\r/g

Wiedermal etwas Regex gelernt :)
