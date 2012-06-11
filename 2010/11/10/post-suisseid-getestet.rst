public: yes
tags: [Hacking,Internet]

Post SuisseID – getestet
========================

[`Trigami-Review <http://www.trigami.com/?blog=http://blog.ich-wars-nicht.ch/>`_\ ]

`|Logo Post| <http://www.postsuisseid.ch/de>`_\ Schon lange gibt es
Versuche, im Zeitalter des Internets eine Art digitale Unterschrift
einzuführen. Einige Versuche sind dabei gescheitert. Jetzt gibt es eine
neue, sogar subventionierte Variante, `die
SuisseID <http://postsuisseid.ch/de/suisseid>`_.

Die SuisseID ist sozusagen ein elektronischer Identitätsausweis im
Internet. Herausgegeben wird sie für Privatpersonen entweder von der
Post, oder von der Quo Vadis AG. Mit der SuisseID unterzeichnete
Dokumente verfügen in der Schweiz über eine rechtsgültige Unterschrift.
Man kann also damit übers Internet einen Strafregisterauszug bestellen
oder die Steuererklärung ausfüllen. Geschützt wird sie durch gängige
kryptographische Massnahmen. Mehr zur Sicherheit später im Artikel.

Ich hatte die Gelegenheit, so eine SuisseID zu testen und beschreibe
hier meine Eindrücke davon.

Inhaltsverzeichnis
~~~~~~~~~~~~~~~~~~

-  `Der
   Bestellvorgang </2010/11/post-suisseid-getestet/#bestellvorgang>`_
-  `Erster Eindruck </2010/11/post-suisseid-getestet/#eindruck>`_
-  `Installation </2010/11/post-suisseid-getestet/#bestellvorgang>`_
-  `SwissStick Menu </2010/11/post-suisseid-getestet/#menu>`_
-  `Die SuisseID und die Online-Services der
   Post </2010/11/post-suisseid-getestet/#online-post>`_
-  `Die SuisseID im restlichen
   Internet </2010/11/post-suisseid-getestet/#online-other>`_
-  `SwissSigner </2010/11/post-suisseid-getestet/#swisssigner>`_
-  `Sicherheit </2010/11/post-suisseid-getestet/#sicherheit>`_
-  `Fazit </2010/11/post-suisseid-getestet/#fazit>`_

Der Bestellvorgang
~~~~~~~~~~~~~~~~~~

Zu Beginn habe ich per E-Mail ein PDF-Antragsformular erhalten. Mit
diesem Formular bin ich auf die nächste Postfiliale gegangen und habe
mir mit einem amtlichen Ausweis meine Identität offiziell bestätigen
lassen. Das Formular wird dann an die SuisseID-Abteilung der Post
gesendet. Ein paar Tage später kommt dann die bestellte Version der
SuisseID (in meinem Fall der SwissStick) und nochmal ein paar Tage
später der PIN (und die Revozionsnummer) um den Chip zu entsperren.

[youtube]http://www.youtube.com/watch?v=ZWOeDoMmPJI[/youtube]

Erster Eindruck
~~~~~~~~~~~~~~~

Der SwissStick ist eine von drei Varianten, wie man die SuisseID bei der
Post bestellen kann: Als SmartCard, als Class 1 USB Reader oder eben in
einem "SwissStick" genannten USB Stick inklusive Anwendungssoftware.

Wenn man den SwissStick öffnet, sieht man die Chipkarte in
SIM-Karten-Grösse. Diese Chipkarte könnte man nun wohl auch entfernen
und in ein anderes Lesegerät stecken, ausprobiert habe ich dies jedoch
nicht.

`|SwissStick| </wp-content/uploads/2010/11/swissStick.jpg>`_
`|SwissStick
Geöffnet| </wp-content/uploads/2010/11/swissStick_offen.jpg>`_

Installation
~~~~~~~~~~~~

Vorgängig habe ich mich natürlich nach der Systemkompatibilität der
SuisseID erkundigt und folgendes gefunden:

`|SuisseID
Linuxkompatibilität| </wp-content/uploads/2010/11/0_linuxkompatibilität_1.png>`_

"Super", habe ich gedacht, die SuisseID wird mit Linux funktionieren.
Also hab ich den Stick mal an meinem Ubuntu-Desktop angeschlossen, aber
passiert ist nichts. Und wenn man auf die Homepage geht um die
Treiber/Software herunterzuladen, wird man bei der Auswahl des
SwissSticks darauf hingewiesen, dass dieser nur unter Windows und Mac
funktioniert. Sehr enttäuschend, vor allem da ich meiner
Linux-Installation bedeutend mehr vertraue als der Windows-Installation.
Leider fällt eine regelmässige Nutzung der SuisseID unter diesen
Umständen für mich schonmal weg. (Bleibt zu erwähnen dass die SuisseID
in anderer Form, wie z.B. die SmartCard, unter Linux lauffähig wäre.)

Also habe ich halt widerwillig Windows gebootet um die SuisseID zu
installieren. Der Stick wird unter Windows 7 sofort erkannt.

`|SwissStick
Installation| </wp-content/uploads/2010/11/1_swissstick_install.png>`_

Danach muss man den Stick im Explorer öffnen und das einzige sich darauf
befindliche .exe ausführen. Beim ersten Start erscheint der
CertificateAssistant, mit welchem man den Chip initialisieren kann.

`|image5| </wp-content/uploads/2010/11/2_swissstick_initialisierung.png>`_

Was mich hier irritiert hat, ist, dass der PIN zwischen 6 und 12 Zeichen
lang sein muss. Wieso zum Geier ist hier ein Limit von 12 Zeichen? Die
Sicherheit der Verschlüsselung steigt ja (je nach
Verschlüsselungsmethode) mit der Länge des PINs. Ist aber wohl nicht
extrem tragisch, da der Chip nach dreifacher falscher Eingabe sowieso
endgültig gesperrt wird, was eine BruteForce-Attacke unsinnig macht.

Das war eigentlich schon alles, eine Installation von Software auf dem
PC ist beim SwissStick nicht notwendig (ausser evt. die neusten
Sicherheitsupdates für den Adobe Reader).

SwissStick Menu
~~~~~~~~~~~~~~~

Nachdem die SuisseID entsperrt wurde, kann man das SwissStick Menu
starten. Dieses sieht folgendermassen aus:

`|SwissStick Menu| </wp-content/uploads/2010/11/3_swissstick_menu.png>`_

Zur Auswahl stehen hier die SwissSigner Signatursoftware, ein SuisseID
Internet Browser, die E-Mail-Applikation IncaMail sowie ein paar andere
Dienste der Post.

Die Signatursoftware wird benutzt um PDFs mit der SuisseID zu signieren.
Dazu später mehr.

Der integrierte Browser ist sozusagen eine kastrierte Firefox-Version.
Will heissen: Eine Version von Firefox 3.x, bei welcher alle unnötigen
Features entfernt wurden. Zudem speichert der Browser keinerlei
Browserhistorie und vermutlich auch keine temporären Daten und Cookies.
Dies erhöht die Sicherheit beim surfen, ich bin jedoch gespannt, wie
lange es nach der Entdeckung irgendwelcher Firefox-Sicherheitslücken
dauert, bis eine aktualisierte Version per (manuellem und nicht
offensichtlich verfügbarem) Update nachgeschoben wird.

`|SwissStick
Browser| </wp-content/uploads/2010/11/4_swissstick_browser.png>`_

Die SuisseID und die Online-Services der Post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zuerst versuchte ich, die IncaMail Applikation zu starten. Dies war
jedoch nicht von Erfolg gekrönt, da die Registration für neue Kunden
temporär deaktiviert war.

`|IncaMail
Fehlermeldung| </wp-content/uploads/2010/11/5_incamail_a.png>`_
`|IncaMail Information| </wp-content/uploads/2010/11/5_incamail_b.png>`_

Dann wollte ich mich mithilfe des Zertifikats im Post WebStamp
einloggen. Im Hilfe-Menu neben dem Login wird erwähnt, dass das
PostZertifikat fürs Login verwendet werden kann, wenn man auf den Link
klickt, wird man darüber informiert, dass die SuisseID der Nachfolger
des PostZertifikats ist.

`|Webstamp| </wp-content/uploads/2010/11/11_webstamp_firefox1.png>`_

Also sollte das Login mit der SuisseID funktionieren. Dies tat es jedoch
nicht. Webstamp hat das Zertifikat nach Eingabe des PINs nicht
akzeptiert.

`|Webstamp Firefox
Fehler| </wp-content/uploads/2010/11/11_webstamp_firefox_fehler1.png>`_

Da es mit dem mitgelieferten Browser nicht zu funktionieren schien, habe
ich es noch mit Chrome und dem Internet Explorer versucht, welche beide
laut `Homepage <http://postsuisseid.ch/de/support/support-downloads>`_
unterstützt werden. Die Beiden haben jedoch mit folgender Fehlermeldung
abgebrochen:

`|Webstamp Fehler
Chrome| </wp-content/uploads/2010/11/11_webstamp_chrome.png>`_
`|Webstamp Fehler IE| </wp-content/uploads/2010/11/11_webstamp_ie.png>`_

Irgendwie wird also das Zertifikat nicht gefunden. Ich weiss auch nicht
genau wie das ohne Zertifikatsinstallation funktionieren soll, aber
seitens der Post wurde merhfach wiederholt, dass mit dem SwissStick
keine Software-, Treiber- oder Zertifikationsinstallation notwendig ist.

Auch auf der Seite der Swiss Post Box konnte ich mich – obwohl auf
`suisseid.ch <http://suisseid.ch/>`_ aufgelistet – mit der SuisseID auch
im mitgelieferten Browser nicht registrieren.

`|Swiss Post Box| </wp-content/uploads/2010/11/14_swisspostbox.png>`_

Die SuisseID im restlichen Internet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nun wollte ich die SuisseID noch im restlichen Internet ausprobieren.
Dafür bin ich zuerst mal auf die Website von
`Amazee <http://www.amazee.com/>`_ gegangen und habe versucht, mich mit
der SuisseID einzulogen. Im mitgelieferten Browser wurde jedoch eine
SSL-Fehlermeldung angezeigt und im Chrome wurde die SuisseID gar nicht
gefunden (wohl das selbe Problem wie schon zuvor).

`|Amazee Firefox| </wp-content/uploads/2010/11/10_amazee_firefox.png>`_
`|Amazee Chrome| </wp-content/uploads/2010/11/10_amazee_chrome.png>`_

Glücklicherweise hat es dann doch noch irgendwo geklappt. Auf der
Website zur Bestellung eines Strafregisterauszuges konnte ich mich mit
der SuisseID authentifizieren und ihnen meine Daten übermitteln. Dies
hat relativ problemlos geklappt.

`|Bestellung
Strafregisterauszug| </wp-content/uploads/2010/11/13_strafregisterauszug_a.png>`_
`|image18| </wp-content/uploads/2010/11/13_strafregisterauszug_b.png>`_

SwissSigner
~~~~~~~~~~~

Nun zur Signier-Software SwissSigner welche beim SwissStick gratis dabei
ist. Die Software ist relativ einfach aufgebaut. Sie kann PDF-Dokumente
öffnen oder diverse Bildformate automatisch ins PDF-Format konvertieren
und anschliessend öffnen. Ich hab mal ein Foto konvertiert und geöffnet:

`|SwissSigner| </wp-content/uploads/2010/11/7_swisssigner.png>`_

Anschliessend kann man mit wenigen Klicks eine neue Signatur einfügen,
entweder sichtbar oder unsichtbar. Ich habe mich für eine sichtbare
Einzelsignatur entschieden.

`|SwissSigner
Signatur| </wp-content/uploads/2010/11/8_swisssigner.png>`_

SwissSigner hat mich nach dem PIN gefragt und dann das unterschriebene
Dokument in einer neuen Datei abgespeichert. Sowohl mit der SwissSigner
Software wie auch direkt mit dem Adobe Reader sieht die Unterschrift nun
gültig aus.

`|Signatur
Acrobat| </wp-content/uploads/2010/11/9_swisssigner_acrobat.png>`_
`|Signatur
SwissSigner| </wp-content/uploads/2010/11/9_swisssigner.png>`_

Wer will, kann das signierte PDF zum Testen herunterladen:
`burgdorferbier\_signiert.pdf </wp-content/uploads/2010/11/burgdorferbier_signiert.pdf>`_
:)

Sicherheit
~~~~~~~~~~

Noch kurz ein paar Worte zur vieldiskutierten Sicherheit. Die SuisseID
wird von Post und SECO als `sehr sicher und praktisch unknackbar
dargestellt <http://postsuisseid.ch/de/suisseid/sicherheit>`_. Dies ist
jedoch eine grosse Unwahrheit. Eines der Risikofaktoren ist (wie die
Post und das SECO `inzwischen
schreiben <http://postsuisseid.ch/de/suisseid/sicherheit>`_) der User.
Wenn der Benutzer z.B. auf einer gefälschten Website den PIN eingibt,
kann diese alle benötigten Daten abrufen. Der zweite Risikofaktor ist
der Computer. Ist der Computer mit Malware verseucht, ist es – entgegen
den anfänglichen Aussagen der SuisseID-Herausgeber – für einen Angreifer
absolut kein Problem die SuisseID zu übernehmen und damit rechtsgültige
Unterschriften zu erstellen. Dagegen hilft auch kein Ausstecken des
Sticks bei Nichtgebrauch - eine Sekunde reicht völlig aus um
automatisiert einige dutzend Verträge zu unterzeichnen. Und dann hat man
den Salat, da man vor Gericht zuerst mal beweisen muss dass man diese
Unterschrift nicht selber gemacht hat, obwohl man das angeblich sichere
Zertifikat nie aus den Händen gegeben hat. Die Anweisung der Post ist in
diesem Fall: "Halte den Computer malwarefrei". Jedoch kann niemand, auch
kein Sicherheitsexperte, mit 100%iger Sicherheit behaupten dass sein
System malwarefrei ist, eine minime Chance gibt es immer (ausser er hat
das Betriebssystem selbst geschrieben ;)).

Eine grosse Hilfe ist in diesem Punkt ein alternatives Betriebssystem
wie OS X oder Linux, für welche es wesentlich weniger Malware gibt. Nur
schade funktioniert der SwissStick unter Linux nicht. FAIL. Eine weitere
Möglichkeit, höhere Sicherheit zu erlangen, ist der Einsatz eines
Class3-Lesegerätes, welches über ein eigenes Eingabefeld für den PIN
verfügt. So kann ein Angreifer wenigstens die PIN-Hürde nicht
überwinden, was eine signifikant höhere Sicherheit bedeutet.

Es gibt noch weitere Sicherheitstechnische Probleme bezüglich der
SuisseID. Ich werde hier nicht weiter darauf eingehen, dies haben andere
schon genug getan. Nachfolgend ein paar 3rd-Party-Links, um sich über
die Sicherheit der SuisseID zu informieren:

-  `remote-exploit.org: SuisseID und nPA
   Schwachstellen <http://www.remote-exploit.org/?page_id=673>`_
-  `chaos computer club: Praktische Demonstration erheblicher
   Sicherheitsprobleme bei Schweizer SuisseID
   (...) <http://www.ccc.de/de/updates/2010/sicherheitsprobleme-bei-suisseid-und-epa>`_
-  `Denis Simonet: Wie sehr hängst du an deiner
   Identität? <http://www.denissimonet.ch/2010/08/22/wie-sehr-hangst-du-an-deiner-identitat/>`_
-  `Denis Simonet: SuisseID - Wo bleibt das
   SECO? <http://www.denissimonet.ch/2010/09/03/suisseid-wo-bleibt-das-seco/>`_
-  `nzz.ch:
   Identitätskrise <http://www.nzz.ch/nachrichten/digital/identitaetskrise_1.7572142.html>`_
-  `computerworld.ch: Fragwürdige Sicherheit der
   SuisseID <http://www.computerworld.ch/aktuell/news/52384/>`_
-  `Twitter: 3rd party Infos über die
   SuisseID <http://twitter.com/suisseid>`_

Fazit
~~~~~

Im Ansatz ist die Idee definitiv gut. Jedoch müssen die
SuisseID-Herausgeber betreffend Sicherheit (z.B. standardmässige
Class3-Lesegeräte), Kommunikation (z.B. ein Infoblatt zur Sicherheit wie
sie die ZKB zum Ebanking versendet) und Usability noch etwas
nachbessern. Wenn in Zukunft vermehrt mit den bestehenden Experten auf
diesem Gebiet (z.B. den Banken) zusammengearbeitet wird, könnte daraus
schon eine ziemlich gute Lösung entstehen. Es ist jedoch eine Illusion,
an die 100%ige Sicherheit zu glauben.

Auch bin ich nicht ganz sicher, was mir die SuisseID als Privatperson
gross bringt. Die Post hat zu diesem Thema eine eigene `Unterseite mit
Anwendungsbeispielen <http://postsuisseid.ch/de/anwendungen>`_
aufgeschaltet. Na klar, man spart vielleicht 1 oder 2 Gänge zu einem
Amt, aber mir persönlich wäre so etwas nicht 104CHF (plus Lesegerät)
wert. Auch verstehe ich nicht, warum man sich bei
`buch.ch <http://buch.ch/>`_ mit der SuisseID anstatt mit dem Login
authentifizieren soll (mal abgesehen von der Altersverifikation). Im
Business-Sektor denke ich allerdings, das eine standardisierte und
einfach nutzbare Zertifikats- und Signier-Lösung potential hat –
jedenfalls wenn an der Sicherheit noch etwas nachgebessert wird.

Ich bin gespannt, was sich in den nächsten Jahren daraus noch ergeben
wird. Erwerben kann man die SuisseID unter
`http://postsuisseid.ch/de/kaufen <http://postsuisseid.ch/de/kaufen>`_.

` <http://www.postsuisseid.ch/de>`_\ |SuisseID Smartcard|

.. |Logo Post| image:: /wp-content/uploads/2010/11/Logo_post2.gif
.. |SwissStick| image:: /wp-content/uploads/2010/11/swissStick-300x199.jpg
.. |SwissStick
Geöffnet| image:: /wp-content/uploads/2010/11/swissStick_offen-300x199.jpg
.. |SuisseID
Linuxkompatibilität| image:: /wp-content/uploads/2010/11/0_linuxkompatibilität_1.png
.. |SwissStick
Installation| image:: /wp-content/uploads/2010/11/1_swissstick_install.png
.. |image5| image:: /wp-content/uploads/2010/11/2_swissstick_initialisierung-287x300.png
.. |SwissStick
Menu| image:: /wp-content/uploads/2010/11/3_swissstick_menu-300x182.png
.. |SwissStick
Browser| image:: /wp-content/uploads/2010/11/4_swissstick_browser-300x265.png
.. |IncaMail
Fehlermeldung| image:: /wp-content/uploads/2010/11/5_incamail_a.png
.. |IncaMail
Information| image:: /wp-content/uploads/2010/11/5_incamail_b.png
.. |Webstamp| image:: /wp-content/uploads/2010/11/11_webstamp_firefox1-300x127.png
.. |Webstamp Firefox
Fehler| image:: /wp-content/uploads/2010/11/11_webstamp_firefox_fehler1.png
.. |Webstamp Fehler
Chrome| image:: /wp-content/uploads/2010/11/11_webstamp_chrome-300x108.png
.. |Webstamp Fehler
IE| image:: /wp-content/uploads/2010/11/11_webstamp_ie-300x121.png
.. |Swiss Post
Box| image:: /wp-content/uploads/2010/11/14_swisspostbox-300x182.png
.. |Amazee
Firefox| image:: /wp-content/uploads/2010/11/10_amazee_firefox-300x177.png
.. |Amazee
Chrome| image:: /wp-content/uploads/2010/11/10_amazee_chrome-300x87.png
.. |Bestellung
Strafregisterauszug| image:: /wp-content/uploads/2010/11/13_strafregisterauszug_a-300x204.png
.. |image18| image:: /wp-content/uploads/2010/11/13_strafregisterauszug_b-274x300.png
.. |SwissSigner| image:: /wp-content/uploads/2010/11/7_swisssigner-300x216.png
.. |SwissSigner
Signatur| image:: /wp-content/uploads/2010/11/8_swisssigner-300x133.png
.. |Signatur
Acrobat| image:: /wp-content/uploads/2010/11/9_swisssigner_acrobat-280x300.png
.. |Signatur
SwissSigner| image:: /wp-content/uploads/2010/11/9_swisssigner-300x216.png
.. |SuisseID
Smartcard| image:: /wp-content/uploads/2010/11/stick12_pngok1.png

