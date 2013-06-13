#!/usr/bin/env python
# coding=utf-8

import os.path
def _read_path(parser,dest,create=None):
    path = os.path.expanduser(parser.get("path",dest))
    if os.path.exists(path):
        return path
    if create in ["file","directory"]:
        ans = raw_input("%s %s does not found. Create now? [y/N]" % (create,path))
        if ans == "y":
            if create == "file":
                dir_path = os.path.dirname(path)
                if not os.path.exists(dir_path):
                    os.makedirs(os.path.dirname(path))
                with open(path,"w") as f:
                    f.write("")
            else:
                os.makedirs(path)
            print("successfully created : %s" % (path,))
            return path
    raise UserWarning("invalid configure : path does not found (destination = %s, value = %s)" % (dest,path))

import ConfigParser
def read(filename):
    parser = ConfigParser.SafeConfigParser()
    parser.read(filename)
    config = {}
    config["output"]        = _read_path(parser,"output_dir",create="directory")
    config["bib_file"]      = _read_path(parser,"bib",create="file")
    config["template_file"] = parser.get("name","template")
    config["html_file"]     = parser.get("name","html")
    config["port"]          = int(parser.get("server","port"))
    config["address"]       = parser.get("server","address")
    config["db_file"]       = os.path.join(config["output"],parser.get("name","database"))
    config["logfile"]       = parser.get("name","logfile")
    return config
