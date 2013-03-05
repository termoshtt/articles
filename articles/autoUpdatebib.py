#encoding:utf-8

import getbib, bibManager

def update(g_cfg, silent=True):
    """
    search pdf without bibfile and add bibfile to bib_file specified by config file
    """

    import os
    pdf_path = os.path.join(g_cfg["output"], u"pdf")

    nobib_pdfs = checkbibfile(g_cfg)
    if nobib_pdfs != [] and not silent:
        for pdf in nobib_pdfs:
            print(pdf)
        print("Above files are pdfs without bibtex infomation.")
        update = raw_input("Do you try to get bibtex files? [y/n]: ")
        if update != "y":
            print "Did not updated bibfile."
            return
        else:
            print "Try to updated bibfile."


    dois = getbib.extractDOI(nobib_pdfs)

    bibstr = u""
    for pdfname in dois.keys():
        oldpdf = os.path.join(pdf_path, pdfname)
        if not silent:
            print(oldpdf + "'s bibfile is update")
        bibstr = getbib.doi2bib(dois[pdfname])
        bibkey = bibManager.parse_str(bibstr).entries.keys()[0]
        newpdf = os.path.join(pdf_path, bibkey + u".pdf")
        if not silent:
            print("%s is renamed to %s" % (oldpdf.encode("utf-8"), newpdf.encode("utf-8")))
        os.rename(oldpdf, newpdf)
        bibManager.add_bibfile(g_cfg[u"bib_file"], bibstr)
    return


def checkbibfile(g_cfg):
    """
    search pdf file without bibfile
    """

    import glob, os

    def ext_key(pdfpath):
        return os.path.splitext(os.path.basename(pdfpath))[0]


    nobib_list = []
    pdf_path = os.path.join(g_cfg[u"output"], u"pdf")
    pdfkeys = [ext_key(pdf) for pdf in list(glob.glob(os.path.join(pdf_path, u"*pdf")))]
    bibdb =  bibManager.read_bibdb(g_cfg[u"bib_file"])
    bibkeys = bibdb.entries.keys()
    for pdfkey in pdfkeys:
        if not pdfkey in bibkeys:
            nobib_list.append(pdfkey)
    return [os.path.join(pdf_path, pdfkey + u".pdf") for pdfkey in nobib_list]
