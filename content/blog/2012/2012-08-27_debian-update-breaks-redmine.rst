Debian Squeeze Update breaks Redmine 1.1.2
==========================================

:tags: redmine, debian, ruby
:language: en
:summary: How to fix Redmine breakage due to updates on Debian Squeeze.

I'm running a Debian Squeeze box with Redmine 1.1.2, Apache and Passenger. After
a system update that upgraded the `rubygems` package to version 1.8.x, Redmine
was broken with the following error message::

    undefined method `name' for "rubygems-update":String

This is due to an incompatibility between Redmine and recent Rubygems versions.
The problem can be fixed by downgrading `rubygems` to a lower version, in my
case 1.3.7. You can check the current version with

.. sourcecode:: bash

    $ gem --version
    1.8.15

To downgrade `rubygems`, you need to make `gem` install an older version of
`rubygems-update`. As root, run:

.. sourcecode:: bash

    $ gem install rubygems-update --version=1.3.7
    ...
    $ REALLY_GEM_UPDATE_SYSTEM=1 gem update --system 1.3.7
    ...
    $ gem --version
    1.3.7

That's it, after restarting Apache (or whatever your webserver is), Redmine
should work again.

(Of course, a better alternative would be to set up a more recent version of
Redmine on a more up-to-date operating sytem. See my
`Ubuntu / Redmine / Nginx / Mongrel / Supervisord
</2012/2/21/ubuntu-redmine-nginx-mongrel-supervisord/>`_
blogpost for a howto on setting up Redmine on Ubuntu.)
