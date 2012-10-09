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
    config["port"]          = parser.get("server","port")
    return config

def _read_path(parser,dest):
    path = parser.get("path",dest)
    if os.path.exists(path):
        raise Warning("Path does not found : destination = %s, value = %s" % (dest,path))
    return os.path.expanduser(path)

from articles import bib2html
def generate_html(config):
    html_path = os.path.join(config["output"],config["html_file"])
    with open(html_path,'w') as f:
        f.write(bib2html.convert(config))

import pickle
import BaseHTTPServer
import CGIHTTPServer
def start_CGI_server(config):
    pickle.dump(config,open(".config.pickle",'wb'))
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    addr = ("",config["port"])
    # handler.cgi_directories = [""]
    httpd = server(addr,handler)
    httpd.serve_forever()

import os.path
from optparse import OptionParser
def main():
    opt_parser = OptionParser()
    opt_parser.add_option("-c","--config",action="store",type="string",
                          dest="config",default="~/.articles.ini")
    opt_parser.add_option("-n","--no-cgi-server",action="store_true",dest="nocgi")
    opt_parser.add_option("-d","--daemonize",action="store_true",dest="daemonize")
    (option,args) = opt_parser.parse_args()

    config_file = os.path.expanduser(option.config)
    if not os.path.exists(config_file):
        print("configure file does not exists : " + config_file)
        return -1
    config = read_configure_file(config_file)

    generate_html(config)

    pid_filename = "/tmp/articles.pid"
    log_filename = "server.log"
    if not option.nocgi:
        if option.daemonize and not os.path.exists(pid_filename):
            from daemon import DaemonContext
            from daemon.pidfile import PIDLockFile
            dc = DaemonContext(
                    pidfile = PIDLockFile(pid_filename),
                    stderr = open(log_filename,"w+"),
                    working_directory = os.getcwd(),
                )
            with dc:
                start_CGI_server(config)
        else:
            start_CGI_server(config)

if __name__ == "__main__":
    main()
