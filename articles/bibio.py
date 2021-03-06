# coding=utf-8

def read_file(filename):
    from pybtex.database.input import bibtex
    from pybtex import errors
    errors.enable_strict_mode()
    parser = bibtex.Parser()
    return parser.parse_file(filename)

def read_str(bibstr):
    from pybtex.database.input import bibtex
    from pybtex import errors
    errors.enable_strict_mode()
    from io import StringIO
    parser = bibtex.Parser()
    return parser.parse_stream(StringIO(bibstr))

def write(bib,filename,Replace=False):
    import os.path
    if os.path.exists(filename) and not Replace:
        raise Warning("File exists")
    from pybtex.database.output import bibtex
    from pybtex import errors
    errors.enable_strict_mode()
    writer = bibtex.Writer()
    import tempfile  # use tempfile in order to save original .bib file
    tmpfilename = tempfile.mkstemp()[1]
    writer.write_file(bib,tmpfilename) # this may raise a exception
    import shutil
    shutil.move(tmpfilename,filename)

def merge(bibfrom,bibto,RaiseWarning=True,ForceReplace=False):
    for key in bibfrom.entries:
        bibto.add_entry(key,bibfrom.entries[key])

def add(bibstr,filename,SkipRepeated=True):
    bibfrom = read_str(bibstr)
    bibto = read_file(filename)
    merge(bibfrom,bibto,SkipRepeated)
    write(bibto,filename,Replace=True)

