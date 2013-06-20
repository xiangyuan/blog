Marking South migrations as new
===============================

:tags: django, south, databases
:language: en
:summary: How to mark some South migrations as new.

Sometimes you might get to the point where you accidentally faked all `South
<http://south.aeracode.org/>`_ migrations for a specific app using the
``‑‑fake`` option, but the database is missing the last change.

In my case, I faked three migrations, but the database state was still at 0002.
If you list the migrations, however, all migrations are marked as run. ::

    $ ./manage.py migrate cmsplugin_mailchimp --list

     cmsplugin_mailchimp
      (*) 0001_initial
      (*) 0002_thankyou_field
      (*) 0003_redirect_url

So what you want to do here is to mark the 0003 migration as new. There's no
extra option to do this, but there is a different, quite obvious solution::

    $ ./manage.py migrate cmsplugin_mailchimp 0002 --fake

     - Soft matched migration 0002 to 0002_thankyou_field.
    Running migrations for cmsplugin_mailchimp:
     - Migrating backwards to just after 0002_thankyou_field.
     < cmsplugin_mailchimp:0003_redirect_url
       (faked)

    $ ./manage.py migrate cmsplugin_mailchimp --list

     cmsplugin_mailchimp
      (*) 0001_initial
      (*) 0002_thankyou_field
      ( ) 0003_redirect_url

Now the state of South matches the state of the database, and I can actually
run the last migration::

    $ ./manage.py migrate cmsplugin_mailchimp

    Running migrations for cmsplugin_mailchimp:
     - Migrating forwards to 0003_redirect_url.
     > cmsplugin_mailchimp:0003_redirect_url
     - Loading initial data for cmsplugin_mailchimp.
    Installed 0 object(s) from 0 fixture(s)
