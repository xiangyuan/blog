RubyGems Update Problems
========================

:tags: sysadmin

Getting the following error message when trying to use `rake`?

.. sourcecode:: plain

    undefined method `loaded_specs' for Gem:Module

Try updating RubyGems:

.. sourcecode:: bash

    $ gem update --system

Getting the following error message when trying to update?

.. sourcecode:: plain

    Installing RubyGems 1.3.2
    ERROR:  While executing gem ... (Errno::ENOMEM)
        Cannot allocate memory

You're out of RAM. To see how much memory you got left, issue the
command:

.. sourcecode:: bash

    $ free -m

And to see which process eats up most memory space:

.. sourcecode:: bash

    $ ps -eo pmem,pcpu,rss,vsize,args | sort -k 1 -r -n | more

I temporarily shut down mysql and apache, that was just enough to be
able to update RubyGems successfully.
