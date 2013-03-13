#!/usr/bin/env python
# coding=utf-8

import cgi
import sys
import os
import pickle

sys.path.append(os.getcwd())
from articles import handler,bib2html,bibio

def update_html(form):
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    bib2html.generate(g_cfg)

def register_bibstr(form):
    if "BibStr" not in form:
        raise Warning("BibStr is not found.")
        return 1
    bibstr = form["BibStr"].value
    ubibstr = unicode(bibstr,"UTF-8")
    f.write(bibstr)
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    bibio.add(ubibstr,g_cfg["bib_file"])
    update_html(form)

action = {
        "UpdateHTML" : update_html,
        "RegisterBibStr" : register_bibstr,
    }

def main():
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    logfile = g_cfg["logfile"]
    req = handler.Request()
    if "Action" not in req.form:
        with open(logfile,"a+") as logf:
            logf.write("(WW) Action is not found in cgi.form")
        return 1
    action_type = req.form["Action"].value
    if action_type not in action:
        with open(logfile,"a+") as logf:
            logf.write("(WW) Action is not implimented")
        return 1
    try:
        action[action_type](req.form)
    except Warning,e:
        with open(logfile,"a+") as logf:
            logf.write("(WW) catch warning while Action:")
            logf.write(str(e))
        return 1
    except Exception,e:
        with open(logfile,"a+") as logf:
            logf.write("(EE) error occured in Action:")
            logf.write(str(e))
        return 1

if __name__ == "__main__":
    main()
