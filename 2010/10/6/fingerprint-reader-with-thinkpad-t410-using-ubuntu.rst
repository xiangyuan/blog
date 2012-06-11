public: yes
tags: [Ubuntu,Linux]

Fingerprint Reader with Thinkpad T410 using Ubuntu
==================================================

How to add fingerprint reader support to your Ubuntu installation (yes,
it does work):

#. Add fingerprint-gui ppa to your sources:

   ::

       sudo add-apt-repository ppa:fingerprint/fingerprint-gui
       sudo apt-get update

#. Install fingerprint-gui

   ::

       sudo apt-get install fingerprint-gui

#. Install UPEK library libbsapi

   ::

       sudo apt-get install libbsapi

#. Log out and back in
#. Play with settings in *System > Preferences > Fingerprint GUI*

For more and more detailed information, see
`https://launchpad.net/~fingerprint/+archive/fingerprint-gui <https://launchpad.net/~fingerprint/+archive/fingerprint-gui>`_.

