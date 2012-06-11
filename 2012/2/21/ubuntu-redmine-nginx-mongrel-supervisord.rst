public: yes
tags: [sysadmin, nginx]
summary: How to install Redmine on Ubuntu with Nginx, Mongrel and Supervisord.

Ubuntu / Redmine / Nginx / Mongrel / Supervisord
================================================

This is a howto to install Redmine on Ubuntu Natty (probably works on Debian too) with Nginx,
Mongrel and Supervisord. The listed commands usually assume root permissions.

Involved software:

:Redmine: Duh, the software you want to install :)
:Nginx: A fast webserver/proxy from Russia
:Mongrel: The software used to serve redmine
:Supervisor: A supervisor daemon written in Python, it automatically restarts the Mongrel process in case it dies.

First, add the PPA for the currently stable Nginx version (the Ubuntu version is outdated).

.. sourcecode:: bash

    $ add-apt-repository ppa:nginx/stable

Then install redmine using your desired backend (e.g. ``redmine-sqlite``), and the supervisor and nginx
packages.

.. sourcecode:: bash

    $ aptitude install redmine redmine-sqlite nginx supervisor

Install the mongrel gem.

.. sourcecode:: bash

    $ gem install mongrel

Set up redmine...

.. sourcecode:: bash

    $ cd /usr/share/redmine
    $ touch log/production.log
    $ chmod 777 log log/production.log

Then add the mongrel initializer to redmine (see `this bug
<http://www.redmine.org/boards/2/topics/24305>`_):

.. sourcecode:: bash

    $ cd config/initializers
    $ wget 'https://gist.github.com/raw/826692/cb0dcf784c30e6a6d00c631f350de99ab99e389d/mongrel.rb'

Configure nginx:

.. sourcecode:: bash

    $ cd /etc/nginx/sites-enabled
    $ touch ../sites-available/redmine
    $ ln -s ../sites-available/redmine
    $ vim redmine

Add the following configuration (adjust to your likings):

.. sourcecode:: nginx

    upstream redmine_server {
            server localhost:3000 fail_timeout=0;
    }

    server {
            listen 80;
            server_name domain.example.com;

            root /usr/share/redmine/public;

            access_log /var/log/nginx/redmine.access.log;
            error_log /var/log/nginx/redmine.error.log info;

            keepalive_timeout 5;

            location / {
                    try_files $uri/index.html $uri.html $uri @mongrel;
            }

            location @mongrel {
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header Host $http_host;
                    proxy_redirect off;
                    proxy_pass http://redmine_server;
            }
    }

Then edit /etc/supervisord/supervisord.conf and add the following
program definition at the end:

.. sourcecode:: ini

    [program:redmine]
    command=ruby /usr/share/redmine/script/server -e production
    directory=/usr/share/redmine/public/
    user=www-data
    autostart=true
    autorestart=true
    redirect_stderr=True

Now restart nginx and supervisord:

.. sourcecode:: bash

    $ /etc/init.d/supervisord stop
    $ /etc/init.d/supervisord start
    $ /etc/init.d/nginx restart

(The supervisord restart command is broken in current Ubuntu and Debian
versions)

That's it, now your redmine installation should be up and running. In
case of questions, feel free to comment.
