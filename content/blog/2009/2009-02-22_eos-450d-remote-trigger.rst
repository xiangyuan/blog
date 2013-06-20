EOS 450D Remote Trigger
=======================

:tags: photography, hacking

On the left side of the Canon EOS 450D (and probably on any other EOS camera), there's a connector
for a remote shutter trigger. You can make your own remote trigger by sticking one side of a 2.5"
jack-jack cable into the connector, while bridging two of the pins on the other side of the cable.

.. image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2009/02/img_6945-300x172.jpg
    :target: http://blog.ich-wars-nicht.ch/wp-content/uploads/2009/02/img_6945.jpg

By connecting pin 1 + 3, you can focus and trigger the shutter; connecting pin 2 + 3 triggers
autofocus only. With that information, you can easily make yourself your own remote trigger, maybe
even an automatic trigger using the arduino and some sensors.

For high speed photography using the arduino and an external flash, i'd recommend the approaches by
`[nosmos.org] <http://projects.nosomos.org/arduino-controlled-flash-trigger>`_ and
`[glacialwanderer.com] <http://www.glacialwanderer.com/hobbyrobotics/?p=11>`_.
