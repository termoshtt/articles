#encoding:utf-8

import pdf2bib,bibio

import sys
def extractDOI(pdfs,logf=sys.stdout):
    """
    extract DOI from pdfs
    PDFS is list of pdffile path specified with either abs or relative.
    LOG specify the file where pdffile name failed to extract DOI is written.
    """
    import os
    dic = {}
    for pdf in pdfs:
        pdf = os.path.abspath(pdf)
        try:
            text = pdf2bib.pdf2text(pdf)
            doi = pdf2bib.pick_out_doi(text)
            os.remove(text)
            dic[os.path.basename(pdf)] = doi
        except Warning:
            string = os.path.basename(pdf) + ": DOI is not found.\n"
            logf.write(string)
    return dic

def update(g_cfg, silent=False):
    """
    search pdf without bibfile and add bibfile to bib_file specified by configure file
    """
    import os
    pdf_addr = g_cfg["pdf"]
    if pdf_addr[:7] != "file://":
        raise UserWarning("only file:// type address is enable in this version")
    pdf_dir = pdf_addr[7:]

    nobib_pdfs = check_bib(g_cfg,pdf_dir)
    if nobib_pdfs != [] and not silent:
        for pdf in nobib_pdfs:
            print(pdf)
        print("Above files are pdfs without bibtex information.")
        update = raw_input("Do you try to get bibtex files? [y/n]: ")
        if update != "y":
            print "Did not updated bibfile."
            return
        else:
            print "Try to updated bibfile."

    dois = extractDOI(nobib_pdfs)
    for pdfname in dois.keys():
        oldpdf = os.path.join(pdf_dir, pdfname)
        if not silent:
            print(oldpdf + "'s bibfile is update")
        try:
            bibstr = pdf2bib.doi2bib(dois[pdfname])
            bib_new = bibio.read_str(bibstr)
            if len(bib_new.entries.keys()) == 0:
                raise Warning("bib data cannot be obtained")
            bibkey = bibio.read_str(bibstr).entries.keys()[0]
        except Exception,e:
            print("catch a Warning while getting bib info:")
            print(e)
            print("skip this pdf")
            continue
        newpdf = os.path.join(pdf_dir, bibkey + u".pdf")
        if not silent:
            print("%s is renamed to %s" % (oldpdf.encode("utf-8"), newpdf.encode("utf-8")))
        os.rename(oldpdf, newpdf)
        try:
            bibio.add(bibstr,g_cfg["bib"])
        except Exception,e:
            print("Unknown error occurs while writing bib info into file")
            print(e)
            print("skip this pdf")
            continue
    return

def check_bib(g_cfg,pdf_dir):
    """
    search pdf file without bibfile
    """
    import glob, os
    def ext_key(pdfpath):
        return os.path.splitext(os.path.basename(pdfpath))[0]
    nobib_list = []
    pdfkeys = [ext_key(pdf) for pdf in list(glob.glob(os.path.join(pdf_dir, u"*pdf")))]
    bibdb =  bibio.read_file(g_cfg[u"bib"])
    bibkeys = bibdb.entries.keys()
    for pdfkey in pdfkeys:
        if not pdfkey in bibkeys:
            nobib_list.append(pdfkey)
    return [os.path.join(pdf_dir, pdfkey + u".pdf") for pdfkey in nobib_list]

