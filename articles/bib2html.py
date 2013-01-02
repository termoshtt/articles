#!/usr/bin/python2
# coding=utf-8

from pybtex.database.input import bibtex
import dbio
def read_bibtex(bib_filename,db_filename):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_filename)
    entries = []
    art_db = dbio.articles_db(db_filename)
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
    return entries

from jinja2 import Template
def convert(g_cfg):
    bib_filename = g_cfg["bib_file"]
    db_filename = g_cfg["db_file"]
    entries = read_bibtex(bib_filename,db_filename)
    art_db = dbio.articles_db(db_filename)

    cfg = {}
    cfg.update({u'title' : u'Articles',})
    cfg.update({u'tags' : art_db.tags(),})
    cfg.update({u'entries' : entries,})
    tmpl = Template(open(g_cfg["template_file"],'r').read())
    html = tmpl.render(cfg)
    return html.encode("utf-8")

import os
def generate(config):
    if not os.path.isdir(config["output"]):
        os.mkdir(config["output"])
    html_path = os.path.join(config["output"],config["html_file"])
    with open(html_path,'w') as f:
        f.write(convert(config))
