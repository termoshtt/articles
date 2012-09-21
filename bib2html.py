#!/usr/bin/python2
# coding=utf-8

template_html = """
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
        <script src="./js/jquery-1.7.2.min.js"></script>
        <script src="./js/search.js"></script>
    </head>
    <body>
        <form id="SearchForm">
            <input id="SearchKeyID" type="text" name="SearchKeyWard" oninput="search()" autofocus placeholder="Search Keywards">
        </form>
        {% for entry in entries %}
        <div class="ArticleDiv">
            <h4><a href='./pdf/{{entry["key"]}}.pdf'>{{entry["title"]}}</a></h4>
            <ul>
                <li>Author : {{entry["author"]}}</li>
                <li>Journal: {{entry["journal"]}}</li>
                <li>Published Year: {{entry["year"]}}</li>
            </ul>
        </div>
        {% endfor %}
    </body>
</html>
"""

from pybtex.database.input import bibtex
from jinja2 import Template

def main(bib_file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)

    entries = []
    for key in bib_data.entries:
        persons = bib_data.entries[key].persons[u'author']
        authors = [unicode(au) for au in persons]

        entry = { u"key" : key, u"author" : ",".join(authors)}

        fields = bib_data.entries[key].fields
        if u'title' in fields:
            entry.update({ u"title" : fields[u'title'], })
        if u'journal' in fields:
            entry.update({ u"journal" : fields[u'journal'], })
        if u'year' in fields:
            entry.update({ u"year" : fields[u'year'], })
        entries.append(entry)

    template = Template(template_html)
    html = template.render({u'entries':entries})

    print html.encode("utf-8")

import sys
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage: ./convert.py your.bib > your.html"
        sys.exit(1)
    main(sys.argv[1])

