#!/bin/bash
PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

rm -r output \
&& pelican --verbose $INPUTDIR -o $OUTPUTDIR -s $CONFFILE $PELICANOPTS \
&& cd output \
&& python -m SimpleHTTPServer
