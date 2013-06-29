#!/usr/bin/env python
# coding=utf-8

import cgi
import sys
import os
import pickle
from articles import handler,bib2html,bibio,configure

def update_html(form):
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    bib2html.generate(g_cfg)

def register_bibstr(form):
    if "BibStr" not in form:
        raise Warning("BibStr is not found.")
        return 1
    bibstr = form["BibStr"].value
    ubibstr = unicode(bibstr,"UTF-8")
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    bibio.add(ubibstr,g_cfg["bib_file"])
    update_html(form)

action = {
        "UpdateHTML" : update_html,
        "RegisterBibStr" : register_bibstr,
    }

def main():
    with open(configure.cache_fn,"rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    req = handler.Request()
    if "Action" not in req.form:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) Action is not found in cgi.form\n")
        return 1
    action_type = req.form["Action"].value
    if action_type not in action:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) Action is not implimented\n")
        return 1
    from pybtex.exceptions import PybtexError
    try:
        action[action_type](req.form)
    except Warning,e:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(WW) catch warning while Action:\n")
            logf.write(str(e)+'\n')
        return 1
    except PybtexError,e:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(EE) error occured from Pybtex in Action:\n")
            logf.write(str(e)+'\n')
        return 1
    except Exception,e:
        with open(configure.log_fn,"a+") as logf:
            logf.write("(EE) error occured in Action:\n")
            logf.write(str(e)+'\n')
        return 1

if __name__ == "__main__":
    main()
