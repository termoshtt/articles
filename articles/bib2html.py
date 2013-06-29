#!/usr/bin/env python
# coding=utf-8

import dbio,bibio
def read_bibtex(g_cfg):
    bib_filename = g_cfg["bib"]
    db_filename = g_cfg["database"]
    bib_data = bibio.read_file(bib_filename)
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
        else:
            entry.update({ u"title" : "", })
        if u'journal' in fields:
            entry.update({ u"journal" : fields[u'journal'], })
        else:
            entry.update({ u"journal" : "", })
        if u'year' in fields:
            entry.update({ u"year" : fields[u'year'], })
        else:
            entry.update({ u"year" : "", })
        tags = art_db.article_tags(key)
        if tags:
            entry.update({ u"tags" : tags, })
        else:
            entry.update({ u"tags" : {}, })
        entries.append(entry)
    return entries

from jinja2 import Template
def convert(g_cfg):
    db_filename = g_cfg["database"]
    template_filename = g_cfg["template"]
    entries = read_bibtex(g_cfg)
    art_db = dbio.articles_db(db_filename)

    cfg = {}
    cfg.update({
        u'title'   : u'Articles',
        u'tags'    : art_db.tags(),
        u'entries' : entries,
        u'address' : g_cfg["address"],
        u'port'    : g_cfg["port"],
        })
    tmpl = Template(open(template_filename,'r').read())
    html = tmpl.render(cfg)
    return html.encode("utf-8")

import os
def generate(config):
    html_path = os.path.join(config["root"],config["index_html"])
    with open(html_path,'w') as f:
        f.write(convert(config))
