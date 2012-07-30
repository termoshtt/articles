bib2paperlist
-------------------------

# Install

## dependences
This script is written in python2,
and depends on the following libraries.
* pybtex
* jinja2

# usage
This script generates HTML files from bibtex files like follows:
    ./convert.py -t [template_file] [bibtex_filename] > output.html

The generated HTML files contain links to .pdf files.
To enable this link, you NEED to set up the directories like follows:
    [document root]/
        output.html
        pdf/
            bibtexkey1.pdf
            bibtexkey2.pdf
            ...
        js/
            ...
        css/
            blue/...
You can choose [document root] directory a piacere.
The js/ and css/ directories are copied from this repository.

## templates
Two templates are ready in this repository:
+ all.html
+ list.html
The default is all.html in convert.py.

