#!/usr/bin/env python
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
from articles import bib2html,configure,autoUpdatebib
def main():
    opt_parser = OptionParser()
    opt_parser.add_option("-c","--config",action="store",type="string",
                          dest="config",default="~/.articles.ini")
    opt_parser.add_option("-n","--no-cgi-server",action="store_true",dest="nocgi")
    opt_parser.add_option("-d","--daemonize",action="store_true",dest="daemonize")
    opt_parser.add_option("-i","--install",action="store_true",dest="install")
    (option,args) = opt_parser.parse_args()

    config_file = os.path.expanduser(option.config)
    if not os.path.exists(config_file):
        print("configure file does not exists : " + config_file)
        return -1
    config = configure.read(config_file)

    autoUpdatebib.update(config, silent=False)
    bib2html.generate(config)
    if option.install:
        copy_attachment(config)
        return

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
