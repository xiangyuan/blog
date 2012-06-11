public: yes
tags: [LaTeX]

A simple LaTeX Makefile
=======================

Today I created a simple LaTeX Makefile based on `this tutorial
<http://www.linux-fuer-alle.de/doc_show.php?docid=92>`_. First of all, this is
the first time I'm writing a Makefile, but it seems to work; if I have
overlooked anything just point it out to me.

.. sourcecode:: makefile

    # Makefile to create PDF documents from LaTeX-Files
    # Needed software packages: pdflatex, rubber
    # License: No copyright, just do what the heck you want with it

    all: pdf clean

    pdf:
        for file in $$(ls *tex | cut -d \. -f 1) ; do make $$file.pdf ; done

    %.pdf: %.tex
        rubber -m pdftex $<

    clean:
        rm -f *.toc *.aux *.log

    cleanall:
        rm -f *.toc *.pdf *.aux *.log

    .PHONY: all pdf clean cleanall
    .SILENT: pdf

    # vim: set tabstop=4 shiftwidth=4 noexpandtab:

This creates a PDF version of each \*.tex-File in the current directory using
`rubber <https://launchpad.net/rubber>`_. I chose rubber over directly using
pdflatex because it compiles the documents as many times as necessary in order
to get all the TOCs and footnotes. Feel free to substitute it with whatever
other command you prefer.

Save the code in a file called ``Makefile`` and run ``make`` to get all
\*.tex-files in the current directory converted to PDF. Type ``make file.pdf``
to convert file.tex to file.pdf. Type ``make clean`` to remove all unnecessary
\*.toc, \*.aux and \*.log files and ``make cleanall`` to remove all PDF
documents as well.

Warnings:

#. Don't use ``make cleanall`` if you have other important PDF files in
   the current directory, they will get removed as well.
#. Retain the tabs in the Makefile, spaces won't work
