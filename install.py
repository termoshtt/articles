#!/usr/bin/python
# coding=utf-8

import shutil
import urllib2
def copy_attachment(config):
    attachments = ["js","css","icons","cgi-bin"]
    jquery_filename = "jquery-1.8.2.js"
    jquery_url = "http://code.jquery.com/" + jquery_filename
    for att in attachments:
        dest_path = os.path.join(config["root"],att)
        if not os.path.isdir(dest_path):
            os.mkdir(dest_path)
        for src in os.listdir(att):
            src_path = os.path.join(att,src)
            shutil.copy2(src_path,dest_path)
        if att == "js":
            with open(os.path.join(dest_path,jquery_filename),"w") as f:
                f.write(urllib2.urlopen(jquery_url).read())

    lib_path = os.path.join(config["root"],"cgi-bin/articles")
    if not os.path.exists(lib_path):
        os.mkdir(lib_path)
    for py in os.listdir("articles"):
        src_path = os.path.join("articles",py)
        dest_path = os.path.join(lib_path,py)
        shutil.copy2(src_path,dest_path)

import os.path
import sys
import argparse
from articles import bib2html,configure,bibupdate
def main():
    parser = argparse.ArgumentParser(description="an installer of articles")
    parser.add_argument("-c","--configure",
            dest="configure_filename",
            default="~/.articles.ini",
            help="specify configure file")
    args = parser.parse_args()

    cfg_fn  = os.path.expanduser(args.configure_filename)
    if not os.path.exists(cfg_fn):
        print("configure file does not found")
        sys.exit(1)
    cfg = configure.read(cfg_fn)

    bib2html.generate(cfg)
    copy_attachment(cfg)

if __name__ == "__main__":
    main()

