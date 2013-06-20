phpBB Soundcloud Embed BBCode
=============================

:tags: internet
:summary: How to create a Soundcloud embed BBcode.

Um Soundcloud-Songs direkt in ein phpBB Forum einzubinden, einfach
folgenden BB-Code im Backend erstellen:

.. image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2012/01/2012-01-22-235418_1421x609_scrot-300x128.png
    :alt: Soundcloud BBCode Configuration Screenshot
    :target: http://blog.ich-wars-nicht.ch/wp-content/uploads/2012/01/2012-01-22-235418_1421x609_scrot.png

Benutzung
^^^^^^^^^

.. sourcecode:: bbcode

    [Soundcloud]{URL}[/Soundcloud]

HTML Ersetzung
^^^^^^^^^^^^^^

.. sourcecode:: html

    <object height="81" width="100%">
    <param name="movie"
    value="http://player.soundcloud.com/player.swf?url={URL}&amp;g=bb"></param>
    <param name="allowscriptaccess" value="always"></param>
    <embed allowscriptaccess="always" height="81"
    src="http://player.soundcloud.com/player.swf?url={URL}&amp;g=bb"
    type="application/x-shockwave-flash" width="100%"></embed>
    </object> <a href="{URL}">{URL}</a>

Tipp-Anzeige
^^^^^^^^^^^^

.. sourcecode:: bbcode

    [Soundcloud]http://soundcloud.com/user/track[/Soundcloud]
