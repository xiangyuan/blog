#!/bin/bash
pdflatex perceptron.tex
pdftops -eps perceptron.pdf
convert -density 600 -resize 398x262 perceptron.eps perceptron.png
