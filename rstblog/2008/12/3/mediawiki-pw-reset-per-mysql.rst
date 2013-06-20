public: yes
tags: [sysadmin]
language: de

Mediawiki PW-Reset per MySQL
============================

Soeben musste ich mein Mediawiki Passwort resetten, hatte aber im Profil keine Mailadresse
angegeben. Dank einem `Blogeintrag <http://e-huned.com/2006/08/15/reset-a-mediawiki-password/>`_
habe ich es dann aber geschafft, das Passwort per MySQL zu resetten:

.. sourcecode:: mysql

    UPDATE user SET user_password = MD5(CONCAT(user_id, '-', MD5('new_password'))) WHERE user_name = someone;
