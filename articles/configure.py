#!/usr/bin/env python
# coding=utf-8

def _read_path(parser,dest,create=None):
    import os.path
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
        else:
            print("Please create by yourself.")
    raise UserWarning("invalid configure : path does not found (destination = %s, value = %s)" % (dest,path))

def read(cfg_path):
    import ConfigParser
    parser = ConfigParser.SafeConfigParser()
    parser.read(cfg_path)
    config = {}
    config["root"]     = _read_path(parser,"root",create="directory")
    config["bib"]      = _read_path(parser,"bib",create="file")
    config["template"] = _read_path(parser,"template")
    config["port"]     = int(parser.get("server","port"))
    config["address"]  = parser.get("server","address")
    config["index_html"] = "index.html"
    config["database"] = "articles.db"
    return config

cache_fn = ".config.pickle"
log_fn = "server.log"
