Setting A Static IP with iproute2
=================================

:tags: network, ip
:language: en
:summary: How to set a static IP in Linux with the "ip" command.

If you want to quickly configure a static IP without authentication on Linux,
you don't need any network manager tool like Wicd_, NetworkManager_ or netctl_.
You can just use the ``ip`` command provided by the iproute2_ package.

(Quick sidenote: If you still use the ``ifconfig``, ``ifup/ifdown`` and
``route`` commands, you should consider switching to iproute2_.)

Check the current configuration::

    $ sudo ip addr show dev eth0
    2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
        link/ether f0:de:f1:13:97:47 brd ff:ff:ff:ff:ff:ff

Set a static IP::

    $ sudo ip addr add 10.10.0.3/24 dev eth0

Verify the new configuration::

    $ ip addr show dev eth0
    2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
        link/ether f0:de:f1:13:97:47 brd ff:ff:ff:ff:ff:ff
        inet 10.10.0.3/24 scope global eth0
           valid_lft forever preferred_lft forever

Here's the entire ``ip addr`` command grammar::

    Usage: ip addr {add|change|replace} IFADDR dev STRING [ LIFETIME ]
                                                          [ CONFFLAG-LIST ]
           ip addr del IFADDR dev STRING
           ip addr {show|save|flush} [ dev STRING ] [ scope SCOPE-ID ]
                                [ to PREFIX ] [ FLAG-LIST ] [ label PATTERN ] [up]
           ip addr {showdump|restore}
    IFADDR := PREFIX | ADDR peer PREFIX
              [ broadcast ADDR ] [ anycast ADDR ]
              [ label STRING ] [ scope SCOPE-ID ]
    SCOPE-ID := [ host | link | global | NUMBER ]
    FLAG-LIST := [ FLAG-LIST ] FLAG
    FLAG  := [ permanent | dynamic | secondary | primary |
               tentative | deprecated | dadfailed | temporary |
               CONFFLAG-LIST ]
    CONFFLAG-LIST := [ CONFFLAG-LIST ] CONFFLAG
    CONFFLAG  := [ home | nodad ]
    LIFETIME := [ valid_lft LFT ] [ preferred_lft LFT ]
    LFT := forever | SECONDS

.. _wicd: https://launchpad.net/wicd
.. _networkmanager: https://wiki.gnome.org/Projects/NetworkManager
.. _netctl: https://wiki.archlinux.org/index.php/Netctl
.. _iproute2: http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2
