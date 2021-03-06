#!/usr/bin/env python
# coding=utf-8

import sqlite3

class articles_db(object):
    def __init__(self,filename):
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.cur.execute('create table if not exists articles(bibtexkey primary key,tags)')
        self.cur.execute('create table if not exists tags(name)')

    def __del__(self):
        self.con.commit()
        self.con.close()
        
    def commit(self):
        self.con.commit()

    def _print_all(self):
        res = self.cur.execute("select * from articles").fetchall()
        if res != None:
            for art in res:
                print("bibtexkey = %s ; tags = %s" % (art[0],art[1]))
        res = self.cur.execute("select * from tags").fetchall()
        if res != None:
            print([r[0] for r in res])

    def article_tags(self,bibtexkey):
        res = self.cur.execute('select tags from articles where bibtexkey=?',(bibtexkey,)).fetchone()
        if res == None or res[0] == "":
            return None
        else:
            return res[0].strip(',').split(',')

    def tags(self):
        res = self.cur.execute('select name from tags').fetchall()
        return [r[0] for r in res]

    def create_tag(self,tag):
        if tag not in self.tags():
            self.cur.execute("insert into tags values (?)",(tag,))

    def delete_tag(self,tag):
        if tag not in self.tags():
            raise Warning("tag does not exist.")
        tag_keys = self.keys(tag)
        if len(tag_keys) == 0:
            self.cur.execute("delete from tags where name=?",(tag,))
        else:
            return False

    def keys(self,tag=None):
        res = self.cur.execute("select * from articles").fetchall()
        if tag == None:
            return [r[0] for r in res]
        else:
            # TODO replace by SQL
            result = []
            for art in res:
                a_key = art[0]
                a_tags = art[1].split(',')
                if tag in a_tags:
                    result.append(a_key)
            return result

    def tagging(self,bibtexkey,tag):
        if tag not in self.tags():
            self.create_tag(tag)
        res = self.cur.execute('select tags from articles where bibtexkey=?',(bibtexkey,)).fetchone()
        if res == None:
            self.cur.execute("insert into articles values (?,?)",(bibtexkey,tag))
            return
        else:
            art_tags = res[0].strip(', ').split(',')
            if not tag in art_tags:
                art_tags.append(tag)
                self.cur.execute("update articles set tags = ? where bibtexkey = ?",(",".join(art_tags),bibtexkey))
            return

    def untagging(self,bibtexkey,tag):
        art_tags = self.article_tags(bibtexkey)
        if art_tags != None and tag in art_tags:
            art_tags.remove(tag)
            self.cur.execute("update articles set tags = ? where bibtexkey = ?",(",".join(art_tags),bibtexkey))
            return
        else:
            raise Warning("tag does not in articles tag")

