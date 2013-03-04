def add_bibfile(bibfile, bibstring):
    """
    Add bibtex file format string(BIBSTRING) to BIBFILE.
    """
    bibdb = read_bibdb(bibfile)
    bibdb = add_bib2db(bibdb, bibstring)
    write_bibdb(bibdb, bibfile)


def add_bib2db(bibdb, bibstring, noerror=True):
    """
    Add bibstring (bibtex file format string) to bibtex database.
    If NOERROR is False, throw a exception for capturing duplicate bibtexkey.
    """
    addbib = parse_str(bibstring)

    if not noerror:
        for key in addbib.entries:
            if key in bibdb.entries.keys():
                raise Warning("This key is already used.")

    for key in addbib.entries:
        bibdb.add_entry(key, addbib.entries[key])

    return bibdb


def write_bibdb(bibdb, output_file):
    """
    BIBDB is written in OUTPUT_FILE
    """

    from pybtex.database.output import bibtex
    writer = bibtex.Writer()
    writer.write_file(bibdb, output_file)


def read_bibdb(input_file):
     from pybtex.database.input import bibtex
     parser = bibtex.Parser()
     return parser.parse_file(input_file)


def parse_str(string):
    from pybtex.database.input import bibtex
    from io import StringIO
    parser = bibtex.Parser()
    return parser.parse_stream(StringIO(string))
