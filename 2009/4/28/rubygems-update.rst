public: yes
tags: [Serveradministration,Linux]

RubyGems Update
===============

Getting the following error message when trying to use *rake*?

::

    undefined method `loaded_specs' for Gem:Module

Try updating RubyGems:

::

    gem update --system

Getting the following error message when trying to update?

::

    Installing RubyGems 1.3.2
    ERROR:  While executing gem ... (Errno::ENOMEM)
        Cannot allocate memory

You're out of RAM. To see how much memory you got left, issue the
command:

::

    free -m

And to see which process eats up most memory space:

::

    ps -eo pmem,pcpu,rss,vsize,args | sort -k 1 -r -n | more

I temporarily shut down mysql and apache, that was just enough to be
able to update RubyGems successfully.

