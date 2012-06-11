public: yes
tags: [Webdesign]

Mediawiki PW-Reset per MySQL
============================

Soeben musste ich mein Mediawiki Passwort resetten, hatte aber im Profil
keine Mailadresse angegeben. Dank einem
`Blogeintrag <http://e-huned.com/2006/08/15/reset-a-mediawiki-password/>`_
habe ich es dann aber geschafft, das Passwort per MySQL zu resetten:

::

    update user set user_password = md5(concat(user_id,'-',md5('new_password'))) where user_name=someone


