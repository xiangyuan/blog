Merging Multiple PDFs under GNU/Linux
=====================================

:tags: linux, pdf
:language: en
:summary: There are different ways to merge multiple PDF files under GNU/Linux.

If you need to join/merge multiple PDF files into a single one, there are
different options available. I tested three different commands using 9 input
files with about 8-10 pages each.

pdfunite
--------

If Poppler_ is installed on your system, you should have the ``pdfunite``
command available::

    pdfunite input1.pdf input2.pdf input3.pdf output.pdf

It is very fast but has no configuration options and internal hyperlinks in the
resulting output are broken.

.. _poppler: http://poppler.freedesktop.org/ 


pdfjam
------

If you've installed a LaTeX distribution and the pdfpages_ package, there's also
a ``pdfjam`` command. ::

    pdfjam input1.pdf input2.pdf input3.pdf -o output.pdf

In contrast to pdfunite, it has tons of configuration options. You can see them
by issueing ``pdfjam --help``. For example you can change the page size, inject
a custom LaTeX preamble and more.

There area also some additional useful commands:

- ``pdf90``, ``pdf180``, ``pdf27`` rotate the pages of one or more PDF files.
- ``pdfflip`` reflects the pages of one or more PDF files.
- ``pdfjam-slides6up``, ``pdfjam-slides3up`` convert PDF presentation slides to
  six-per-page or three-per-page for handout purposes.

It's a bit slower than ``pdfunite`` and all hyperlinks are gone in the resulting
output.

.. _pdfpages: http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages/


pdftk
-----

The ``pdftk`` command comes together with Ghostscript_ and should be available
on most Linux systems. ::

    pdftk input1.pdf input2.pdf input3.pdf cat output output.pdf

It also features tons of options (see ``pdftk --help``). It is a bit slower than
``pdfunite``, but still very fast. In contrast to the other commands, hyperlinks
are preserved and work fine.

.. _ghostscript: http://www.ghostscript.com/ 


Comparison
----------

+-------------------+----------------------------+-------------------------+-----------------------+
|                   | **pdfunite**               | **pdfjam**              | **pdftk**             |
+-------------------+----------------------------+-------------------------+-----------------------+
| **Configuration** | No configuration options.  | Lots of options.        | Lots of options.      |
|                   |                            | See ``pdfjam --help``.  | See ``pdftk --help``. |
+-------------------+----------------------------+-------------------------+-----------------------+
| **Speed**         | 0.200s                     | 1.297s                  | 0.293s                |
+-------------------+----------------------------+-------------------------+-----------------------+
| **File Size**     | 718 KiB                    | 743 KiB                 | 774 KiB               |
+-------------------+----------------------------+-------------------------+-----------------------+
| **Hyperlinks**    | Internal hyperlinks broken | Gone                    | OK                    |
+-------------------+----------------------------+-------------------------+-----------------------+
| **Page Format**   | Original format is         | All pages are converted | Original format is    |
|                   | preserved.                 | to the same format.     | preserved.            |
+-------------------+----------------------------+-------------------------+-----------------------+


Conclusion
----------

Given the comparison table above, I'd usually go for ``pdftk``. The command is
harder to memorize and generates the largest files, but it is very fast and
preserves both original file format and hyperlinks.

For the cases where I need additional features like header injection, page
numbering, presentation handouts and more, I'll use ``pdfjam``.
