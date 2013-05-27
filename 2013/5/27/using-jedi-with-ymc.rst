public: yes
tags: [python,vim]
language: en
summary: |
    How to use Jedi with the YouCompleteMe library.

Using Jedi with YouCompleteMe
=============================

The "official" Jedi_ plugin for vim is jedi-vim_, but there's another vim
autocompletion plugin that supports Jedi: YouCompleteMe_.

In contrast to jedi-vim, YCM does not only support Python, it also provides
intelligent Clang_-based completion support for C/C++/Objective-C/Objective-C++
as well as omnicomplete based semantic completions for Ruby, PHP and more.

The way YCM works is by automatically showing completion suggestions while
typing, without the need for a trigger key. Another feature that distinguishes
it from other autocompletion plugins is that the filtering of possible
completions is not based on the prefix, but using subsequence matching instead.
To quote the YCM author, this is a fancy way of saying that any input characters
need to be present in a completion string in the order in which they appear in
the input. So `abc` is a subsequence of `xaybgc`, but not of `xbyxaxxc`. And as
yet another bonus, YCM features integration with UltiSnips_.

More information and docs can be found at
http://valloric.github.io/YouCompleteMe/.

Setup
-----

To use YCM with vundle_, simply add the following line to your `.vimrc`:

.. sourcecode:: vim

    Bundle 'Valloric/YouCompleteMe'

Then let vundle install the new bundle::

    $ vim +BundleInstall +qall

In order for YCM to work, you need to compile the core. Use the
``--clang-completer`` argument if you want semantic support for C family
languages. ::

    $ cd ~/.vim/bundle/YouCompleteMe
    $ ./install.sh --clang-completer

Configuration
-------------

In my `.vimrc` I currently use only two configuration lines. The first
enables auto closing of the preview window when the user accepts the offered
completion string.

.. sourcecode:: vim

    let g:ycm_autoclose_preview_window_after_completion=1

The next line maps Jedi's jump to definition/declaration feature to the
`<leader>g` shortcut:

.. sourcecode:: vim

    nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

Further Information
-------------------

jedi-vim and YCM are currently not compatible. You have to choose one of them.

YCM's integration with Jedi is still under development. As soon as all features
are implemented (pydoc is not included yet, for example), it might even replace
jedi-vim as the "officially endorsed" completion plugin. You can find more
information in `jedi-vim issue #119
<https://github.com/davidhalter/jedi-vim/issues/119>`_.

For more information about YCM, refer to its `extensive documentation
<http://valloric.github.io/YouCompleteMe/>`_.


.. _jedi: https://github.com/davidhalter/jedi
.. _jedi-vim: https://github.com/davidhalter/jedi-vim
.. _youcompleteme: http://valloric.github.io/YouCompleteMe/
.. _vundle: https://github.com/gmarik/vundle
.. _clang: http://clang.llvm.org/
.. _ultisnips: https://github.com/SirVer/ultisnips
