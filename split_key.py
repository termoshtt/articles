#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex

def parsef(bib_file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)

    for key in bib_data.entries:
        print key

def parset(bib_text):
    import io
    parser = bibtex.Parser()
    ss = io.StringIO(unicode(bib_text))
    bib_data = parser.parse_stream(ss)

    for key in bib_data.entries:
        print key

import sys
from optparse import OptionParser
if __name__ == "__main__":
    par = OptionParser()
    par.add_option("-t","--text",dest="text",default=None)
    par.add_option("-f","--file",dest="filename",default=None)

    (opt,arg) = par.parse_args()

    if opt.filename:
        parsef(opt.filename)
    elif opt.text:
        parset(opt.text)
    elif len(arg) > 0:
        parsef(arg[0])

