public: yes
tags: [Webdesign,php,Programmieren]

PHP Magische Methoden
=====================

Zusammenfassung der magischen Methoden (magic methods) von PHP:

-  **\_\_construct():** Konstruktor
-  **\_\_destruct():** Destruktor
-  **\_\_call(string name, array argumente):** Aufruf bei unbekannter
   Objektmethode
-  **\_\_callStatic(string name, array argumente):** Aufruf bei
   unbekannter Klassenmethode
-  **\_\_get(string name):** Lesender Aufruf bei unbekannter Eigenschaft
-  **\_\_set(string name, mixed wert):** Schreiender Aufruf bei
   unbekannter Eigenschaft
-  **\_\_isset(string name):** Aufruf bei Verwendung von isset()
-  **\_\_unset(string name):** Aufruf bei Verwendung von unset()
-  **\_\_sleep():** Aufruf bei Verwendung von serialize()
-  **\_\_wakeup():** Aufruf bei Verwendung von unserialize()
-  **\_\_toString():** Aufruf bei echo
-  **\_\_clone():** Aufruf bei Klon-Vorgang

*Quelle: PHP Kurzreferenz von Comelio GmbH*

