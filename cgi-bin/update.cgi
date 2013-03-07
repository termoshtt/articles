#!/usr/bin/env python
# coding=utf-8

import cgitb
cgitb.enable()

sys.path.append(os.getcwd())
from articles import handler
from articles import bib2html

def main():
    req = handler.Request()
    with open(".config.pickle","rb") as g_cfg_f:
        g_cfg = pickle.load(g_cfg_f)
    bib2html.generate(g_cfg)

if __name__ == "__main__":
    main()
