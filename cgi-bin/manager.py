#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex
from jinja2 import Template

def convert(bib_file,template):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)
    entries = []
    for key in bib_data.entries:
        try:
            persons = bib_data.entries[key].persons[u'author']
            authors = [unicode(au) for au in persons]
        except:
            authors = [u'unknown']
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

import cgitb
cgitb.enable()
import handler
def generate_response(bib_file,template):
    res = handler.Response()
    html = convert(bib_file,template)
    res.set_body(html)
    print(res)

import os
from optparse import OptionParser
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s","--static",action="store_true",dest="static")
    parser.add_option("-t","--template",type="string",action="store",dest="template")
    (option,args) = parser.parse_args()

    bib_file = os.getenv("MAIN_BIB")

    if(option.template and os.path.exists(option.template)):
        template = open(option.template).read()
    elif(os.path.exists("user.html")):
        template = open("user.html").read()
    else:
        template = open("template.html").read()

    if option.static:
        print(convert(bib_file,template))
    else:
        generate_response(bib_file,template);

