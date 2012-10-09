#!/usr/bin/python2 
# coding=utf-8

import ConfigParser
def read_configure_file(filename):
    parser = ConfigParser.SafeConfigParser()
    parser.read(filename)
    config = {}
    config["bib_file"]      = _read_path(parser,"bib")
    config["output"]        = _read_path(parser,"output_dir")
    config["template_file"] = parser.get("name","template")
    config["db_file"]       = parser.get("name","database")
    config["html_file"]     = parser.get("name","html")
    return config

def _read_path(parser,dest):
    path = parser.get("path",dest)
    if os.path.exists(path):
        raise Warning("Path does not found : destination = %s, value = %s" % (dest,path))
    return os.path.expanduser(path)

import sys
sys.path.append("./cgi-bin")
from articles import bib2html
def generate_html(config):
    html_path = os.path.join(config["output"],config["html_file"])
    with open(html_path,'w') as f:
        f.write(bib2html.convert(config))

import BaseHTTPServer
import CGIHTTPServer
def start_CGI_server(config):
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    addr = ("",8000)
    # handler.cgi_directories = [""]
    httpd = server(addr,handler)
    httpd.serve_forever()

import os.path
from optparse import OptionParser
def main():
    opt_parser = OptionParser()
    opt_parser.add_option("-c","--config",action="store",type="string",
                          dest="config",default="~/.articles.ini")
    (option,args) = opt_parser.parse_args()

    config_file = os.path.expanduser(option.config)
    if not os.path.exists(config_file):
        print("configure file does not exists : " + config_file)
        return -1
    config = read_configure_file(config_file)
    generate_html(config)
    start_CGI_server(config)

if __name__ == "__main__":
    main()
