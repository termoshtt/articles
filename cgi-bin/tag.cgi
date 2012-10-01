#!/usr/bin/python2
# coding=utf-8

import cgitb
cgitb.enable()
import handler

ActionTypes = ["AddTag"]

import dbio
def AddTag(form):
    tag_name = form["TagName"].value
    adb = dbio.articles_db("articles.db")
    adb.create_tag(tag_name)

    res = handler.Response()
    res.set_body("""
        <html><body>
        Tag Created Successfully : <br>
        tag name = %s
        </body></html>""" % tag_name)
    print(res)

def AddTagKey(form):
    pass

action = {
        "AddTag" : AddTag,
        "AddTagKey" : AddTagKey,
    }

def main():
    req = handler.Request()
    action_type = req.form["TagAction"].value

    if action_type in ActionTypes:
        action[action_type](req.form)
    else:
        raise UserWarning("TagAction is not implimented yet." )

if __name__ == "__main__":
    main()

