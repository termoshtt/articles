Paper Manage Tools
-------------------------

This is a bibtex to HTML converter.

# Dependence
This script is written in python2,
and depends on the following libraries.
* pybtex
* jinja2

# Usage
    ./convert.py your.bib > your.html
if you make original template file(yourtemplate.html)
    ./convert.py -t yourtemplate.html your.bib > your.html
To enable searching, you have to place your.html on the same place of convert.py
or copy js/ direcotry and involves to the direcotry where your.html is placed.

