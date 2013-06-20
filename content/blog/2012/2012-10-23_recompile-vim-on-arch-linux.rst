public: yes
tags: [vim, python, ruby, archlinux]
language: en
summary: |
    Recompile Vim with Python and Ruby support under Arch Linux.

Recompile Vim with Python/Ruby Support on Arch Linux
====================================================

For my `vim configuration <https://github.com/dbrgn/dotfiles>`__, I need a
version of Vim that was built with Python and Ruby support. Unfortunately, the
default version of Vim that is installed with `pacman` doesn't support
Python/Ruby.

The easiest way to solve this problem is to install the `gvim` package instead
of `vim` (don't worry, the `gvim` package also includes a `vim` binary). But
this brings along a huge amount of dependencies that I didn't want on my
system, so there's no way around a package recompilation.

To ease the reconfiguration-process I found `pacbuilder
<https://wiki.archlinux.org/index.php/Pacbuilder>`__, a script to easily
recompile single packages or even the whole system. Install it using yaourt (or
manually if you prefer)::

    $ yaourt -S pacbuilder-svn

Then rebuild the `vim` and `vim-runtime` packages with the `--edit` option::

    $ pacbuilder --install --edit vim vim-runtime

When the script asks you whether you want to edit the `PKGBUILD` file, answer
with `y`. Then find the first line that looks like this::

    ./configure --prefix=/usr --localstatedir=/var/lib/vim \
      --with-features=big --with-compiledby=ArchLinux \
      --enable-gpm --enable-acl --with-x=no \
      --disable-gui --enable-multibyte --enable-cscope \
      --disable-netbeans --enable-perlinterp --disable-pythoninterp \
      --disable-python3interp --disable-rubyinterp --disable-luainterp

Edit the configure options to your likings. In my case, I changed the following
things:

- `--disable-pythoninterp` ⇒ `--enable-pythoninterp`
- `--disable-python3interp` ⇒ `--enable-python3interp`
- `--disable-rubyinterp` ⇒ `--enable-rubyinterp`
- `--with-compiledby=ArchLinux` ⇒ `--with-compiledby="Custom Build (http://s.dbrgn.ch/uqK6)"`

Also add `python`, `python2` and `ruby` to the `depends` list inside the
`package_vim()` function. Then save and close the `PKGBUILD` file.

Pacbuilder will now go on to compile and install your custom build of Vim. You
can verify it with ``vim --version`` on the commandline.

Afterwards, if you want to prevent `pacman` from auto-upgrading your `vim`
package, you can add `vim` and `vim-runtime` to the `IgnorePkg` variable in
`/etc/pacman.conf`.
