#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex
from jinja2 import Template

def convert(bib_file,template):
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
    tmpl = Template(template)
    html = tmpl.render({u'entries':entries})
    return html.encode("utf-8")

import os
if __name__ == "__main__":
    bib_file = os.getenv("MAIN_BIB")
    template = open("template.html").read()
    html = convert(bib_file,template)
    print("Content-type: text/html\n")
    print(html)

