#!/usr/bin/python
# coding=utf-8

import os
import os.path
import sys
import argparse
import pickle
import BaseHTTPServer
import CGIHTTPServer
from daemon import DaemonContext
from daemon.pidfile import PIDLockFile

import articles.configure

def install(cfg):
    """install necessaries"""
    pass

def update(cfg):
    """update [server root]/index.html"""
    pass

def start(cfg,pid_filename = "/tmp/articles.pid"):
    """start articles daemon"""
    s_root = cfg["root"]
    log_path = os.path.join(s_root,"server.log") # not secure
    if not os.path.exists(pid_filename):
        dc = DaemonContext(
                pidfile = PIDLockFile(pid_filename),
                stderr = open(log_path,"w+"),
                working_directory = s_root,
            )
        with dc:
            pickle.dump(cfg,open(articles.configure.configure_cache_fn,'wb'))
            server = BaseHTTPServer.HTTPServer
            handler = CGIHTTPServer.CGIHTTPRequestHandler
            addr = ("",cfg["port"])
            # handler.cgi_directories = [""]
            httpd = server(addr,handler)
            httpd.serve_forever()
    else:
        print("already running")
        sys.exit(1)

def kill(cfg,pid_filename = "/tmp/articles.pid"):
    """kill articles server"""
    if not os.path.exists(pid_filename):
        print("no server is running (or cannot found pid rock file)")
        sys.exit(1)
    pid = int(open(pid_filename,'r').read())
    os.kill(pid,9)
    os.remove(pid_filename)

def main():
    parser = argparse.ArgumentParser(description="article manager based on BibTeX")
    parser.add_argument("-c","--configure",
            dest="configure_filename",
            default="~/.articles.ini",
            help="specify configure file")
    sub_psr = parser.add_subparsers()
    sub_psr.add_parser("install",help="install necessaries").set_defaults(func=install)
    sub_psr.add_parser("update",help="update [server root]/index.html").set_defaults(func=update)
    sub_psr.add_parser("start",help="start articles daemon").set_defaults(func=start)
    sub_psr.add_parser("kill",help="kill articles server").set_defaults(func=kill)
    args = parser.parse_args()

    cfg_fn  = os.path.expanduser(args.configure_filename)
    if not os.path.exists(cfg_fn):
        print("configure file does not found")
        sys.exit(1)
    cfg = articles.configure.read(cfg_fn)
    args.func(cfg)

if __name__ == "__main__":
    main()
