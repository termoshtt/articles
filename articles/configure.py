#!/usr/bin/env python
# coding=utf-8

import os.path
def _read_path(parser,dest):
    path = parser.get("path",dest)
    if os.path.exists(path):
        raise Warning("Path does not found : destination = %s, value = %s" % (dest,path))
    return os.path.expanduser(path)

import ConfigParser
def read(filename):
    parser = ConfigParser.SafeConfigParser()
    parser.read(filename)
    config = {}
    config["bib_file"]      = _read_path(parser,"bib")
    config["output"]        = _read_path(parser,"output_dir")
    config["template_file"] = parser.get("name","template")
    config["html_file"]     = parser.get("name","html")
    config["port"]          = int(parser.get("server","port"))
    config["address"]       = parser.get("server","address")
    config["db_file"]       = os.path.join(config["output"],parser.get("name","database"))
    config["logfile"]       = parser.get("name","logfile")
    return config
