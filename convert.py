#!/usr/bin/python2
# coding=utf-8


import sys
from pybtex.database.input import bibtex
from jinja2 import Template

def main(bib_file,template_file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)

    entries = []
    for key in bib_data.entries:
        persons = bib_data.entries[key].persons[u'author']
        authors = [unicode(au) for au in persons]

        entry = { u"key" : key, u"author" : ",".join(authors)}

        fields = bib_data.entries[key].fields
        if u'title' in fields:
            entry.update({ u"title" : fields[u'title'], })
        if u'journal' in fields:
            entry.update({ u"journal" : fields[u'journal'], })
        if u'year' in fields:
            entry.update({ u"year" : fields[u'year'], })
        entries.append(entry)

    template = Template(open(template_file).read())
    html = template.render({u'entries':entries})

    print html.encode("utf-8")

from optparse import OptionParser
if __name__ == "__main__":
    par = OptionParser()
    par.add_option("-t","--template",dest="templatefile",default="all_template.html")

    (options,args) = par.parse_args()
    main(args[0],options.templatefile)

