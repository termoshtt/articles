#!/usr/bin/env python
# coding=utf-8

import cgitb
cgitb.enable()

import pickle
import os
import sys
sys.path.append(os.getcwd())
from articles import dbio
from articles import handler
from articles import bib2html
def CreateTag(form):
    tag_name = form["TagName"].value
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.create_tag(tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def DeleteTag(form):
    tag_name = form["TagName"].value
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.delete_tag(tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def Tagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.tagging(bib_key,tag_name)
    adb.commit()
    bib2html.generate(g_cfg)

def unTagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    with open(".config.pickle","rb") as g_cfg_f:
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
    req = handler.Request()
    action_type = req.form["TagAction"].value
    if action_type in action:
        action[action_type](req.form)
    else:
        raise Warning("TagAction is not implimented yet." )

if __name__ == "__main__":
    main()
