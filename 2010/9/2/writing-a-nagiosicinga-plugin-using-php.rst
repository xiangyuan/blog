public: yes
tags: [Arbeitsalltag,Linux,Internet]

Writing a Nagios/Icinga Plugin using PHP
========================================

Note to self: If you want to write a check plugin for Nagios / Icinga
using PHP, remember the following things:

-  Start the first line of the script with ``#!/usr/bin/php -q``
-  Don't put any empty lines between the
   `shebang <http://en.wikipedia.org/wiki/Shebang_(Unix)>`_ and the
   opening php tag (``<?php``)
-  Return values are either 0 (OK), 1 (WARNING) or 2 (CRITICAL)
-  Return those values using ``exit()``, not using ``return()``
-  Before the exit statement, return some info using ``echo``. Nagios /
   Icinga will only display the first line of the output.


