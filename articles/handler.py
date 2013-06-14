#!/usr/bin/env python
# coding:utf-8 

import cgi 
import os

import time

_weekdayname=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
_monthname=[None,"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


class Request(object):
    """
    A class handling HTTP requests
    """
    def __init__(self,environ=os.environ):
        self.form=cgi.FieldStorage()
        self.environ=environ

class Response(object):
    """
    The class handring Response of HTTP
    you can use this class by making Instance before sending Response
    save Response and Header
    """

    def __init__(self,content_type="html",charset='utf-8'):
        if content_type == "html":
            self.headers={'Content-type':'text/html;charset=%s' % charset}
        elif content_type == "json":
            self.headers={'Content-type':'application/json; charset=%s' % charset}
        elif content_type == "xml":
            self.headers={'Content-type':'text/xml; charset=%s' % charset}
            # self.headers={'Content-type':'application/xml; charset=%s' % charset}
        else:
            raise RuntimeError("invalid content_type : please choose from {html,json,xml}")
        self.status=200
        self.status_message='success'
        self.body=""

    def set_header(self, name, value):
        """set header of Response"""
        self.headers[name]=value
    
    def get_header(self,name):
        """get the header which already set"""
        return self.headers.get(name,None)

    def set_body(self, bodystr):
        """return the text which output as Response"""
        self.body=bodystr

    def make_output(self,timestamp=None):
        """make Response text including header and text"""
        if timestamp is None:
            timestamp=time.time()
        year,month,day,hh,mm,ss,wd,y,z=time.gmtime(timestamp)
        dtstr="%s, %02d %3s %4d %02d:%02d:%02d GMT" % (_weekdayname[wd],day,_monthname[month],year,hh,mm,ss)
        self.set_header("Last-Modified",dtstr)
        headers='\n'.join(["%s: %s" % (key,self.headers[key]) for key in self.headers])
        return headers+'\n\n'+self.body

    def __str__(self):
        """convert Request into text"""
        return self.make_output()

