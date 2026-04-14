#!/bin/bash
var="report"
pdflatex -shell-escape $var.tex && bibtex $var && pdflatex -shell-escape $var.tex && pdflatex -shell-escape $var.tex
