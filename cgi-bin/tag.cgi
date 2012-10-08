#!/usr/bin/python2
# coding=utf-8

import cgitb
cgitb.enable()
import handler

import pickle
import dbio
import manager
def CreateTag(form):
    tag_name = form["TagName"].value
    g_cfg_f = open(".config.pickle","rb")
    g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.create_tag(tag_name)
    adb.commit()
    manager.generate_response(g_cfg)

def DeleteTag(form):
    tag_name = form["TagName"].value
    g_cfg = pickle.load(open(".config.pickle","rb"))
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.delete_tag(tag_name)
    adb.commit()
    manager.generate_response(g_cfg)

def Tagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    g_cfg_f = open(".config.pickle","rb")
    g_cfg = pickle.load(g_cfg_f)
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.tagging(bib_key,tag_name)
    adb.commit()
    manager.generate_response(g_cfg)

def unTagging(form):
    tag_name = form["TagName"].value
    bib_key = form["BibTeXKey"].value
    g_cfg = pickle.load(open(".config.pickle","rb"))
    adb = dbio.articles_db(g_cfg["db_file"])
    adb.untagging(bib_key,tag_name)
    adb.commit()
    manager.generate_response(g_cfg)

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

