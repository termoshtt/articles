#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex
from jinja2 import Template
import dbio
def convert(bib_file,db_file,template):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)
    entries = []
    art_db = dbio.articles_db(db_file)
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
        tags = art_db.get_tag(key)
        if tags != None:
            entry.update({ u"tags" : ','.join(tags), })
        entries.append(entry)
    
    cfg = {}
    cfg.update({u'title' : u'Articles',})
    cfg.update({u'tags' : art_db.tags(),})
    cfg.update({u'entries' : entries,})
    tmpl = Template(template)
    html = tmpl.render(cfg)
    return html.encode("utf-8")

import handler
def generate_response(bib_file,db_file,template):
    res = handler.Response()
    html = convert(bib_file,db_file,template)
    res.set_body(html)
    print(res)

import os
from optparse import OptionParser
def main():
    parser = OptionParser()
    parser.add_option("-s","--static",action="store_true",dest="static")
    parser.add_option("-t","--template",type="string",action="store",dest="template",default="user.html")
    parser.add_option("-d","--db_file",type="string",action="store",dest="db_file",default="articles.db")
    (option,args) = parser.parse_args()

    bib_file = os.getenv("MAIN_BIB")
    if(os.path.exists(option.template)):
        template = open(option.template).read()
    else:
        template = open("template.html").read()

    if option.static:
        print(convert(bib_file,option.db_file,template))
    else:
        generate_response(bib_file,option.db_file,template);

import cgitb
cgitb.enable()
if __name__ == "__main__":
    main()

