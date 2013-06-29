#!/usr/bin/env python
# coding=utf-8

import cgitb
cgitb.enable()

import pickle
import os
import sys
from articles import dbio,handler,bib2html,configure

def CreateTag(form):
    tag_name = form["TagName"].value
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.create_tag(tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def DeleteTag(form):
    tag_name = form["TagName"].value
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.delete_tag(tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def Tagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.tagging(bib_key,tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def unTagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.untagging(bib_key,tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

action = {
        "CreateTag" : CreateTag,
        "DeleteTag" : DeleteTag,
        "Tagging"   : Tagging,
        "unTagging" : unTagging,
    }

def main():
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    req = handler.Request()
    if "TagAction" not in req.form:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) TagAction is not found in cgi.form")
        return 1
    action_type = req.form["TagAction"].value
    if action_type not in action:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) TagAction is not implimented")
        return 1
    try:
        action[action_type](req.form)
    except Warning,e:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) catch warning while TagAction:")
            logf.write(str(e))
        return 1
    except Exception,e:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(EE) error occured in TagAction:")
            logf.write(str(e))
        return 1

if __name__ == "__main__":
    main()
