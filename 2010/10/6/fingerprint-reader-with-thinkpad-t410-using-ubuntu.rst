public: yes
tags: [Ubuntu,Linux]

Fingerprint Reader with Thinkpad T410 using Ubuntu
==================================================

How to add fingerprint reader support to your Ubuntu installation (yes, it does work):

1. Add fingerprint-gui ppa to your sources:

.. sourcecode:: bash

   $ sudo add-apt-repository ppa:fingerprint/fingerprint-gui
   $ sudo apt-get update

2. Install fingerprint-gui

.. sourcecode:: bash

   $ sudo apt-get install fingerprint-gui

3. Install UPEK library libbsapi

.. sourcecode:: bash

   $ sudo apt-get install libbsapi

4. Log out and back in
5. Play with settings in *System > Preferences > Fingerprint GUI*

For more and more detailed information, see
`https://launchpad.net/~fingerprint/+archive/fingerprint-gui
<https://launchpad.net/~fingerprint/+archive/fingerprint-gui>`_.
