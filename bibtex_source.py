#!/usr/bin/python2
# coding=utf-8

import os
from articles import bib2html,configure
from optparse import OptionParser

def output(entries,comma=u', '):
    for entry in entries:
        bibkey  = entry[u"key"]
        title   = entry[u"title"]
        journal = entry[u"journal"]
        year    = entry[u"year"]
        author  = entry[u"author"]
        tags    = entry[u"tags"]

        description = author+comma+journal+comma+year+comma+title
        if tags:
            description = description + comma + " ".join(tags)
        output = bibkey + comma + description
        print(output.encode("utf-8"))

def main():
    opt_parser = OptionParser()
    opt_parser.add_option("-c","--config",action="store",type="string",
                          dest="config",default="~/.articles.ini")
    (option,args) = opt_parser.parse_args()
    config_file = os.path.expanduser(option.config)
    if not os.path.exists(config_file):
        print("configure file does not exists : " + config_file)
        return -1
    config = configure.read(config_file)

    entries = bib2html.read_bibtex(config)
    output(entries)

if __name__ == "__main__":
    main()
