#!/usr/bin/python2
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
    config["db_file"]       = parser.get("name","database")
    config["html_file"]     = parser.get("name","html")
    config["port"]          = int(parser.get("server","port"))
    return config

