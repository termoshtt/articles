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
