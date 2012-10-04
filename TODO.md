TODOs for articles
===================

The following features will be implemented in the future version.

## webapp switch to local .html file
This application is intended to use in iPad/GoodReader.
To do so, The webapp should be local .html file 
in order to link local .pdf files saved in GoodReader.

### Problems
In this version, a web page transition occurs with every CGI request.
This is not adequate to use in iPad:
Then the link './pdf/bibtexkey' is interpreted 
as 'http://name.of.server/cgi-bin/pdf/bibtexkey',
since the HTML of the list is obtained throught http://. 
To get over this problem the cgi request should be replaced 
by ajax request.

## init script, configure file
There are many configurations :
Where .bib file exits ? 
Where pdf/ directory exists ?
What is the name of CGI server ?
...

To manage these information, a configuration file,
for example, $HOME/.articlesrc would help us.

