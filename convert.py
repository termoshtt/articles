#!/usr/bin/python2
# coding=utf-8


import sys
from pybtex.database.input import bibtex
from jinja2 import Template
def main():
    bib_file = sys.argv[1]

    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)

    entries = []
    for key in bib_data.entries:
        authors = bib_data.entries[key].persons[u'author']
        entry = { u"key" : key, u"author" : authors }

        fields = bib_data.entries[key].fields
        if u'title' in fields:
            entry.update({ u"title" : fields[u'title'], })
        if u'journal' in fields:
            entry.update({ u"journal" : fields[u'journal'], })
        if u'year' in fields:
            entry.update({ u"year" : fields[u'year'], })
        entries.append(entry)

    template = Template(open("all_template.html").read())
    html = template.render({u'entries':entries})

    print html.encode("utf-8")

if __name__ == "__main__":
    main()

