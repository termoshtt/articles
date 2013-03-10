# coding=utf-8

def read_file(filename):
     from pybtex.database.input import bibtex
     parser = bibtex.Parser()
     return parser.parse_file(filename)

def read_str(bibstr):
    from pybtex.database.input import bibtex
    from io import StringIO
    parser = bibtex.Parser()
    return parser.parse_stream(StringIO(bibstr))

def write(bib,filename):
    from pybtex.database.output import bibtex
    writer = bibtex.Writer()
    writer.write_file(bib,filename)

def merge(bibfrom,bibto,SkipRepeated=True):
    for key in bibfrom.entries:
        if key in bibto.entries.keys() and SkipRepeated:
            continue
        bibto.add_entry(key,bibfrom.entries[key])

def add(bibstr,filename,SkipRepeated=True):
    bibfrom = read_str(bibstr)
    bibto = read_file(filename)
    merge(bibfrom,bibto,SkipRepeated)
    write(bibto,filename)

