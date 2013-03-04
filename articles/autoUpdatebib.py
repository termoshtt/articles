#!/usr/bin/python
#encoding:utf-8

import getbib, bibManager

def main ():
    print auto_update_bib(g_cfg)
    return



def auto_update_bib(g_cfg):
    import glob, os
    pdf_path = g_cfg["output_dir"]
    pdfkeys = [ext_key(pdf) for pdf in list(glob.glob(os.path.join(pdf_path, "*pdf")))]

    bibdb =  bibManager.read_bibdb(g_cfg["bib_file"])

    bibkeys = bibdb.entries.keys()

    nobib_list = checkbibfile(bibkeys, pdfkeys)

    nobib_pdfs = [os.path.join(pdf_path, pdfkey + ".pdf") for pdfkey in nobib_list]

    dois = getbib.extractDOI(nobib_pdfs)

    bibstr = ""
    for pdfname in dois.keys():
        bibstr = getbib.doi2bib(dois[pdfname])
        bibkey = bibManager.parse_str(bibstr).entries.keys()[0]
        oldpdf = os.path.join(pdf_path, pdfname)
        newpdf = os.path.join(pdf_path, bibkey + ".pdf")
        os.rename(oldpdf, newpdf)
        bibManager.add_bibfile(g_cfg["bib_file"], bibstr)
    return


def checkbibfile(bibkeys, pdfkeys):
    nobib_list = []
    for pdfkey in pdfkeys:
        if not pdfkey in bibkeys:
            nobib_list.append(pdfkey)
    return nobib_list


def ext_key(pdfpath):
    import os.path
    return os.path.basename(pdfpath).rstrip(".pdf")


if __name__ == "__main__":
    main()
