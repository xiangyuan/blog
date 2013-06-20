public: yes
tags: [sysadmin, firewall]
language: en
summary: |
    ufw is a very easy way to configure your firewall rules, without writing
    iptables scripts.

ufw – A Simple iptables Frontend
================================

If you're looking for a simple frontend to iptables, you might want to take a
look at ufw_.

ufw stands for *Uncomplicated Firewall* and has been developed for Ubuntu
Server, to simplify the firewall management process. It provides a fairly
simple but very powerful commandline interface to show, add and edit firewall
rules.

Getting started
---------------

On Debian Squeeze or Wheezy, you can install UFW directly from the main
repository::

    #> aptitude install ufw

Default behavior is to deny all incoming traffic and to allow all outgoing
traffic. First, if you're connected to the server via SSH, allow incoming SSH
traffic to avoid locking yourself out::

    #> ufw allow SSH
    Rules updated
    Rules updated (v6)

Then enable the firewall::

    #> ufw enable
    Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
    Firewall is active and enabled on system startup

Now ufw is enabled and will be started automatically at boot time. You can list
the enabled rules with the ``status`` command::

    #> ufw status verbose
    Status: active
    Logging: on (low)
    Default: deny (incoming), allow (outgoing)
    New profiles: skip

    To                         Action      From
    --                         ------      ----
    22/tcp (SSH)               ALLOW IN    Anywhere
    22/tcp (SSH (v6))          ALLOW IN    Anywhere (v6)

You can add further services with the ``allow`` command. ufw comes with some
preconfigured application profiles, you can list them using ``ufw app
list``::

    #> ufw app list
    Available applications:
      AIM
      Bind9
      Bonjour
      CIFS
      DNS
      ...

You can also use the aliases in `/etc/services`::

    #> cat /etc/services | grep -i amqp
    amqp            5672/tcp
    amqp            5672/udp
    amqp            5672/sctp

For example, allow all incoming DNS traffic::

    #> ufw allow DNS
    Rule added
    Rule added (v6)

To deny outgoing IRC traffic::

    #> ufw deny out ircd
    Rule added
    Rule added (v6)

The full syntax for the allow/deny function is as follows::

    ufw [--dry-run] [delete] [insert NUM] allow|deny|reject|limit [in|out]
    [log|log-all] PORT[/protocol]

    ufw [--dry-run] [delete] [insert NUM]  allow|deny|reject|limit  [in|out  on
    INTERFACE]  [log|log-all] [proto protocol] [from ADDRESS [port PORT]] [to
    ADDRESS [port PORT]]

The status output should now look like this::

    # ufw status
    Status: active

    To                         Action      From
    --                         ------      ----
    SSH                        ALLOW       Anywhere
    DNS                        ALLOW       Anywhere
    SSH (v6)                   ALLOW       Anywhere (v6)
    DNS (v6)                   ALLOW       Anywhere (v6)

    6667/tcp                   DENY OUT    Anywhere
    6667/tcp                   DENY OUT    Anywhere (v6)

Next Steps
----------

For a more in-depth introduction, including the removal of rules and the
configuration of rules with specific IPs or IP subnets, refer to the `Ubuntu
help pages`_.


.. _ufw: https://wiki.ubuntu.com/UncomplicatedFirewall
.. _ubuntu help pages: https://help.ubuntu.com/community/UFW
