def extractDOI(pdfs, log = "/tmp/extractDOI.log"):
    """
    extract DOI from pdfs
    PDFS is list of pdffile path specified with either abs or relative.
    LOG specify the file where pdffile name failed to extract DOI is written.
    """
    import os.path
    logf = open(log, "w")
    dic = {}
    for pdf in pdfs:
        pdf = os.path.abspath(pdf)
        pdf2text(pdf)
        try:
            text = pdf2text(pdf)
            doi = parseDOI(text)
            dic[os.path.basename(pdf)] = doi
        except:
            string = os.path.basename(pdf) + ": DOI is not found.\n"
            logf.write(string)

    logf.close()
    return dic



def parseDOI(txt):
    """
    Parse DOI from text
    """
    import re
    body = open(txt)
    reg = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>,])\S)+)\b')
    m = reg.search(body.read())
    if m == None:
        raise Warning("DOI is not found.")
    else:
        return m.group(0)



def pdf2text(pdf):
    import subprocess
    import os.path

    pdf = os.path.abspath(pdf)
    # subprocess.call(["pdftotext", "-l", "1", "-enc", "UTF-8", "-q", pdf])
    subprocess.call(["pdftotext", "-l", "1", "-enc", "ASCII7", "-q", pdf])
    text = os.path.splitext(pdf)[0] + ".txt"

    return text




def doi2bib(doi):
    """
    get bibfile from bibtex
    """
    import urllib2
    uri = "http://dx.doi.org/"
    edoi = urllib2.quote(doi)
    url = uri +  edoi
    req = urllib2.Request(url, headers = {"Accept":"text/bibliography; style=bibtex"})
    html = urllib2.urlopen(req).read()
    return html
