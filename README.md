# Cycling Team Website

## Introduction

This branch contains the website of a cycling team (more information on the website). It is a __static website__ (no php) host on GitHub pages. Most of its pages are built using the template engine Jinja (for Python), whereas a few of them are not following this template and built using  Rmarkdown files converted into HTML.

## Use

The branch ```gh-pages``` contains :
   * Jinja templates : these files do not require any specific extension. In this project, their extension is ```.j2```, which has the advantage that it allows to the Atom package "atom-Jinja2" to recognize the files (specific syntax highlighting)
   * Generated HTML Files (```.html```)
   * The Python script that converts templates into HTML files, computing and providing to the templates the information needed (```script.py```)


   * RMarkdown templates for some specific pages (```.Rmd```) and their generated HTML files


   * CSS and JavaScript Files (respectively ```css``` and ```js``` folders)
   * All pictures

It does not contain, for confidentiality reasons :
   * *Results.xlsx*, a file with a given structure that contains the results.

### Prerequisites
  Python 3 with jinja2 and a few other libraries (pandas, numpy, os, sys, codecs, copy).
  R with several libraries (flexdashboard, leaflet, htmlwidgets, among others...)

### Templating

#### Jinja Files

Jinja templates use various elements of syntax provided by Jinja2 (see jinja.pocoo.org for all the information). The "index" page contains all the elements and defines several blocks (header menu, sidebar) which are included in other pages which follow the same structure.

In order to generate HTML files from Jinja templates, the file ```script.py``` simply needs to be executed. Any modification in the template will then be applied to the HTML file, erasing the previous one).

#### RMarkdown Files

Rmarkdown files can for example be converted into HTML using the following command, in the folder where the file is :
```rmarkdown::render(filename.Rmd)```
