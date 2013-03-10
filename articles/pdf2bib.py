# coding=utf-8

def pdf2text(pdf_path,encoding="ASCII7"):
    import subprocess
    import os.path
    pdf_path = os.path.abspath(pdf_path)
    subprocess.call(["pdftotext","-l","1","-enc",encoding,"-q",pdf_path])
    text = os.path.splitext(pdf_path)[0] + ".txt"
    return text

def pick_out_doi(txt):
    import re
    body = open(txt)
    reg = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>,])\S)+)\b')
    m = reg.search(body.read())
    if m == None:
        raise Warning("DOI is not found.")
    else:
        return m.group(0)

def doi2bib(doi):
    import urllib2
    uri = "http://dx.doi.org/"
    edoi = urllib2.quote(doi)
    url = uri +  edoi
    req = urllib2.Request(url, headers = {"Accept":"text/bibliography; style=bibtex"})
    bibstr = urllib2.urlopen(req).read()
    return unicode(bibstr, "utf-8")

