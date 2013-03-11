#!/usr/bin/env python
# coding=utf-8

import cgitb
cgitb.enable()
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
    req = handler.Request()
    if "Action" not in req.form:
        raise Warning("Action form is not contained.")
        return 1
    action_type = req.form["Action"].value
    if action_type not in action:
        raise Warning("TagAction is not implimented yet." )
        return 1
    action[action_type](req.form)

if __name__ == "__main__":
    main()
