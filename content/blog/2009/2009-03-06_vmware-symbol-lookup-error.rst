Vmware Symbol Lookup Error
==========================

:tags: gentoo

Despite the fact that the Vmware Player was working two weeks ago, today it didn't. The following
error message was displayed:

.. sourcecode:: plain

    /opt/vmware/player/lib/vmware/bin/vmplayer: symbol lookup error:
    /opt/vmware/player/lib/vmware/lib/libvmwareui.so.0/libvmwareui.so.0:
    undefined symbol:
    \_ZThn12\_N4view10FieldEntry17delete\_text\_vfuncEii

The solution on Gentoo (thanks to `scherbaum.info
<http://blog.scherbaum.info/2008/02/21/libvmwareuiso0libvmwareuiso0-undefined-symbol/>`_ and
`discretia.org <http://blog.discretia.org/?p=12#comments>`_) is to rebuild ``x11-libs/libview`` (and
possibly also ``x11-libs/libsexy``). The problem occurs after you rebuild gtkmm with the USE-flag
``accessibility``.
