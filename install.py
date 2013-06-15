#!/usr/bin/python
# coding=utf-8

import shutil
import urllib2
def copy_attachment(config):
    attachments = ["js","css","icons"]
    jquery_filename = "jquery-1.8.2.js"
    jquery_url = "http://code.jquery.com/" + jquery_filename
    for att in attachments:
        dest_path = os.path.join(config["output"],att)
        if not os.path.isdir(dest_path):
            os.mkdir(dest_path)
        for src in os.listdir(att):
            src_path = os.path.join(att,src)
            shutil.copy2(src_path,dest_path)
        if att == "js":
            with open(os.path.join(dest_path,jquery_filename),"w") as f:
                f.write(urllib2.urlopen(jquery_url).read())

import os.path
import sys
from articles import bib2html,configure,bibupdate
def main():
    parser = argparse.ArgumentParser(description="article manager based on BibTeX")
    parser.add_argument("-c","--configure",
            dest="configure_filename",
            default="~/.articles.ini",
            help="specify configure file")

    cfg_fn  = os.path.expanduser(args.configure_filename)
    if not os.path.exists(cfg_fn):
        print("configure file does not found")
        sys.exit(1)
    cfg = articles.configure.read(cfg_fn)

    bib2html.generate(config)
    copy_attachment(config)

if __name__ == "__main__":
    main()

