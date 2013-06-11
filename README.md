If you are Japanese, see README-ja.md.

# articles

An article manager based on BibTeX

## Features
+ consists of WebApp(HTML+JavaScript) and CGI server
+ Searching and Tagging articles
+ sources for complement of BibTeX key in vim(unite.vim) or emacs(helm) are served
+ works on iPad (GoodReader)
+ get BibTeX informations from PDF automatically

This application is an article manager composed of WebApp(HTML+JavaScript) and CGI server.
This generate a static HTML file from BibTeX file,
and some support features (searching and tagging articles) are implemented by JavaScript.
This WebApp can also be used alone, however,
the tagging feature (add new tags and delete tags) is unavailable without CGI server.
Once you add tags to your articles on WebApp, 
these tagging information are saved into HTML file;
you can use the tag-search feature in WebApp alone.
Using this project,
You can browse your articles managed by BibTeX in your favor web browser.
If you are using GoodReader, which is one of the most cool iPad application,
you can send the static HTML into GoodReader and use the WebApp in GoodReader.
In addition, when you are writing an article or a paper in your favorite editor,
which must be vim or emacs,
you can complement a BibTeX key from this project.
If you are not using BibTeX now,
you can get BibTeX informations from PDFs automatically.

In summary, you can do without server:
+ generate static HTML file
+ article search (title,journal,author,date)
+ auto-generate .bib file (from command line, see below)
+ BibTeX-key complement in your editor(vim,emacs)
and you can do with server:
+ tagging/untagging article
+ register BibTeX information through WebApp
+ update HTML from WebApp

In this version this application is developed on Fedora18 and Mac OS X 10.8.

## Install

### necessaries (BibTeX key)
In order to use link embedded in HTML articles list,
the file name of PDF files must be in the form '[bibtexkey].pdf'.
([bibtexkey] represents the BibTeX key of the article.)
When you get BibTeX informations from PDF files,
these PDF files are renamed to the required form automatically.
So you need not to rename by yourself.

### dependencies
The most part of this project is written in python2,
and depends on the following libraries.
* pybtex : parse BibTeX source
* jinja2 : generate HTML

For famous distribution of Linux, at least on Fedora,
jinja2 can be found in the package manager (yum,apt,..).
However, pybtex might not be found, so you have to install it manually.
Fortunately, pybtex can be installed by easy\_install
```shell
easy_install pybtex
```
(usually root authorization is needed.)
If you use --getbib (-b) option,
*the version of pybtex must be 0.16 or later*.
Package managers sometimes install the older version of pybtex.

### procedure for install (Linux)

Before install this program, please install pybtex and jinja2.

At first, please get the source code of this project:
```shell
git clone git://github.com/termoshtt/ariticles.git
```
or please download .zip and extract.
Next go into the directory and copy the configure file to your $HOME:
```shell
cd articles
cp sample.ini ~/.articles.ini
```
You should modify the configure file now.
* [path.bib]        : the path for .bib file
* [path.outputdir]  : the path where you want to install .html and js/, css/, icons/
* [name.template]   : the name of template file used to generate HTML from .bib file
* [name.html]       : the name of generated HTML
* [name.database]   : the name of database that contains the tagging information
* [name.logfile]    : the name of log file in which messages from CGI will output
* [server.address]  : the address of CGI server
* [server.port]     : the port of CGI server

After configuration, generate HTML and copy js/, css/, icons/ to your install directory.
```shell
./start.py --install
```
if you do not want to place ~/.articles.ini, you can use other configure file:
```shell
./start.py -i -c path/to/configure.ini
```
(--install can be abbreviate by -i)

Up to here, the installation is finished.
You can find articles.html (or name you set) in your install directory 
i.e. [path.outputdir].
Let's open your articles.html with your favorite browser.
If you like Firefox,
```shell
firefox path/to/articles.html
```
or enter 
```
file:///home/yourname/path/to/articles.html
```
into your navigation toolbar.

When the BibTeX file is updated,
you can update HTML file by
```shell
./start.py -n
```

## Usage

### link to .pdf
As mentioned above, 
please the file name of PDF files be '[bibtexkey].pdf'.
In order to enable linking from HTML to .pdf files,
.pdf files have to place under [path.outputdir]/pdf directory.

### tagging articles
You have to stand CGI server in order to use tagging feature,
but you do not have to stand full-featured server like Apache,nginx,etc.
A simple CGI server library for testing CGI script is included
in the official distribution of python,
and use this library in this project.

The CGI server stands also by start.py:
```shell
./start.py
```
Then the .html file is updated and CGI server stands.
This process wait CGI request until you kill this process,
so you terminate this process by Ctrl-C or kill command.

A navigator appears when you click the text "Tags of articles"
placed under the information of articles in WebApp.
Then you can put a tag on the article
by create button with the tag name entered into the text area "Tag Name".
After put tags, you can narrow the articles down to tagged articles.

### get BibTeX information
In order to obtain BibTeX informations from PDF,
please execute the following command:
```shell
./start.py --getbib
```
or
```shell
./start.py -b
```
Then the list of PDF whose corresponding BibTeX key does not exist is displayed.

### use in iPad/GoodReader
Here, the usage of this application in iPad will be explained shortly.
_GoodReader_ is a good PDF reader on iPad(iOS).

#### use WebApp alone
Since _GoodReader_ can read HTML,
WebApp is usable on _GoodReader_ only sync the directory [path.outputdir].
The sync can be done through online storage services, 
such as Dropbox, Google Drive, etc.
If you do not want to use such service, you can also use ssh(sftp).
Since sftp use ssh server,
you need not to stand new server except for ssh server.
The WebApp starts on _GoodReader_ by opening articles.html,
and you can use the links to articles.

#### use with CGI server
Since there is no way to stand CGI server on iPad,
it is necessary to stand a server out of iPad.
The address and port to CGI server are embedded in HTML file,
and they can be modified by the configure file.

## License
BSD 3-Clause License
