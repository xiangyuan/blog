Install Brother DCP-7010 under Arch Linux
=========================================

:tags: sysadmin

This how-to will enable you to print and scan with a Brother DCP-7010 printer under Arch Linux. (For
deb- and rpm-based Distributions, there are `drivers available
<http://welcome.solutions.brother.com/bsc/public_s/id/linux/en/index.html>`_.)

#. Install `brother-dcp7010 <https://aur.archlinux.org/packages.php?ID=39170>`_ and `brscan2
   <https://aur.archlinux.org/packages.php?ID=19122>`_ via `AUR
   <https://wiki.archlinux.org/index.php/Arch_User_Repository>`_
#. Install ``sane`` and a frontend for it, e.g. ``xsane``
#. Add your user to the scanner-Group: ``gpasswd -a username scanner``
#. Add the keyword ``brother2`` to `/etc/sane.d/dll.conf`
#. Log out and back in

You should now be able to print and scan.
