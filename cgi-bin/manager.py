#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex
from jinja2 import Template
import dbio
def convert(g_cfg):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(g_cfg["bib_file"])
    entries = []
    art_db = dbio.articles_db(g_cfg["db_file"])
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
        tags = art_db.article_tags(key)
        if tags:
            entry.update({ u"tags" : tags, })
        entries.append(entry)
    
    cfg = {}
    cfg.update({u'title' : u'Articles',})
    cfg.update({u'tags' : art_db.tags(),})
    cfg.update({u'entries' : entries,})
    tmpl = Template(g_cfg["template"])
    html = tmpl.render(cfg)
    return html.encode("utf-8")

import handler
def generate_response(g_cfg):
    res = handler.Response()
    html = convert(g_cfg)
    res.set_body(html)
    print(res)

import os
import pickle
from optparse import OptionParser
def main():
    parser = OptionParser()
    parser.add_option("-s","--static",action="store_true",dest="static")
    parser.add_option("-t","--template",type="string",action="store",dest="template",default="user.html")
    parser.add_option("-d","--db_file",type="string",action="store",dest="db_file",default="articles.db")
    (option,args) = parser.parse_args()

    g_cfg = {}
    g_cfg["bib_file"] = os.getenv("MAIN_BIB")
    if(os.path.exists(option.template)):
        g_cfg["template"] = open(option.template).read()
    else:
        g_cfg["template"] = open("template.html").read()
    g_cfg["db_file"] = option.db_file

    if option.static:
        print(convert(g_cfg))
    else:
        generate_response(g_cfg);

    g_cfg_f = open(".config.pickle","wb")
    pickle.dump(g_cfg,g_cfg_f)

import cgitb
cgitb.enable()
if __name__ == "__main__":
    main()

