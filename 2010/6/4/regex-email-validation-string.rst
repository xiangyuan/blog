public: yes
tags: [Webdesign,Programmieren]

RegEx Email Validation String
=============================

Wer denkt, dass das Erstellen eines RegEx-Strings zur Validierung von
E-Mail-Adressen keine grosse Sache ist, sollte sich mal diesen Link
ansehen:
`http://fightingforalostcause.net/misc/2006/compare-email-regex.php <http://fightingforalostcause.net/misc/2006/compare-email-regex.php>`_

Hier nochmal der "Gewinnerstring":

/^([\\w\\!\\#$\\%\\&\\'\\\*\\+\\-\\/\\=\\?\\^\\\`{\\\|\\}\\~]+\\.)\*[\\w\\!\\#$\\%\\&\\'\\\*\\+\\-\\/\\=\\?\\^\\\`{\\\|\\}\\~]+@((((([a-z0-9]{1}[a-z0-9\\-]{0,62}[a-z0-9]{1})\|[a-z])\\.)+[a-z]{2,6})\|(\\d{1,3}\\.){3}\\d{1,3}(\\:\\d{1,5})?)$/i

