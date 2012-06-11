public: yes
tags: [Webdesign,Wordpress]

Bugfix for Wordpress "Landing Sites" plugin
===========================================

Today I was googling one of my own blogposts, and found the link I
looked for. When I was forwarded to my blog, I became aware that I had
enabled the `landing sites
plugin <http://wordpress.org/extend/plugins/landing-sites/>`_, which
should to displays a nice list with related posts.

`|image0| <http://blog.ich-wars-nicht.ch/wp-content/uploads/2010/04/landingsites.png>`_

As you may have noticed, I wrote "should". Although the search string
was exactly the same as the title of the blogpost that I was looking
for, there was no match.

I echoed the issued SQL query from the plugin and queried it directly in
the database. Unfortunately, I got the following SQL error:

::

    ERROR 1191 (HY000): Can't find FULLTEXT index matching the column list

Apparently there was some index missing. After some googling, I was able
to fix the problem by issueing this query:

::

    alter table wp_posts add fulltext(post_title, post_content);

I'm not sure if that's the right way to solve the problem, but the
plugin seems to be working again.

.. |image0| image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2010/04/landingsites-300x81.png

