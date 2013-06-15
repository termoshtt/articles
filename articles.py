#!/usr/bin/python
# coding=utf-8

def install(cfg):
    """install necessaries"""
    pass

def update(cfg):
    """update [server root]/index.html"""
    pass

def start(cfg):
    """start articles daemon"""
    pass

def kill(cfg):
    """kill articles server"""
    pass

import os.path
import sys
import argparse
import articles.configure
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
