Integrate Dokuwiki with SMF
===========================

:tags: php

I recently needed an integration of Dokuwiki with SMF (Simple Machines Forum). After some research i
managed to get it done. Inspired by `this thread
<http://forum.dokuwiki.org/thread/2161;nocount#postlistbottom>`_.

I tested this with SMF 2.0 RC1.2 and DokuWiki 2009-02-14b.

- Download and install both SMF and Dokuwiki. I separated them using a `/forum` and a `/wiki`
  directory.
- Get the file `smfauth.class.php` (version 0.3) from `here
  <http://blog.ticktag.org/addons/smfauth.class.zip>`_ and put it inside your `wiki/inc/auth/`
  directory
- Do the following changes in your `smfauth.class.php` file:

 .. sourcecode:: plain

     find all instances of memberName and change to member_name
     find all instances of realName and change to real_name
     find all instances of emailAddress and change to email_address
     find all instances of groupName and change to group_name
     find all instances of additionalGroups and change to additional_groups
     find all instances of dateRegistered and change to date_registered
     find all instances of posterEmail and change to poster_email
     find all instances of ID_GROUP and change to id_group
     find all instances of ID_MEMBER and change to id_member

- Edit the line in your `smfauth.class.php` file where it says ``MODIFICATION REQUIRED`` (line 32),
  and include the absolute path to your `forum/Settings.php` file
- Edit the file `wiki/conf/local.php` and change the setting for ``$conf['authtype']`` to `smfauth`
- Edit line 78 in `smfauth.class.php` and do the following change:

 .. sourcecode:: plain

       change
       AND (concat(',',u.additionalGroups,',') LIKE concat('%,',g.id_group,',%') OR u.id_group = g.id_group)";
       to
       AND (concat(',',u.additional_groups,',') LIKE concat('%,',g.id_group,',%') OR u.id_group = g.id_group OR u.id_post_group = g.id_group)";

- Edit the file `wiki/conf/local.php` and change the setting for ``$conf['superuser']`` to the name of the
  superuser group in SMF (@Administrator in German, i'd guess it'd be @Admin in the English version)
- Add the following line to your wiki/conf/local.php file:

 .. sourcecode:: php

       $conf['auth']['mysql']['charset'] = 'utf8';

- You should now be able to log in using your SMF superuser. Now add correct permissions for the
  group 'Newbie' (case sensitive) in your Dokuwiki access control

I think that's it, i hope i didn't forget anything. If you have any
questions, feel free to comment.
