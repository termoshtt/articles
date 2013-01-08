articles
=========

An article manager based on BibTeX

# Features
This application is an article manager composed of WebApp(HTML+JavaScript) and CGI server.
This generate a HTML containing the information of articles from a BibTeX file,
and an articles searching function is implemented by JavaScript.
The WebApp can be used alone,
but a tagging feature is available if you use CGI server simultaneously.
After you add tags to your articles, 
since these tagging informations are also saved into HTML file,
you can use tag-search feature in WebApp alone.
Using this project,
You can view the information of articles saved in BibTeX file by your favor web browser.
Since a static HTML is generated,
it can be used on iPad or other tablet PCs same as on the PC.

This application supports Linux only now.
This may work on Mac or other UNIX system, but not tested.

# Install

## necessaries (BibTeX key)
In order to use link embedded in HTML articles list,
the filename of PDF files must be in the form '[bibtexkey].pdf'.
([bibtexkey] represents the BibTeX key of the article.)
Since it is too hard to provide filename converter, please rename by your own.

## dependencies
The most part of this project is written in python2,
and depends on the following libraries.
* pybtex : parse BibTeX source
* jinja2 : generate HTML

For famous distribution of Linux, at least on Fedora,
jinja2 can be found in the package manager (yum,apt,..).
However, pybtex might not be found, so you have to install it manually.
Fortunately, pybtex can be installed by easy-install
```shell
    easy-install pybtex
```
(usually root authorication is needed.)

## procedure for install (Linux)

Before install this program, please install pybtex and jinja2.

At first, please get the source code of this project:
```shell
    git clone http://github.com/termoshtt/ariticles.git
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

When the BibTeX file updated,
you can update HTML file by
```shell
    ./start.py -n
```

### start to use
After installed, you can start a CGI server as:
```shell
    ./start.py
```
This script wait requests until you kill this script.
If you want only to generate articles.html i.e. not to start CGI server,
```shell
    ./start.py -n
```
Other options are displayed with
```shell
    ./start.py -h
```
Since tagging feature is implemented as a CGI,
the tagging cannot use unless the CGI server stands.
In other word, searching and tag choosing can be used without the CGI server.

(experimental)
The CGI server can daemonize by option -d:
```shell
    ./start.py -d
```
This feature have not fully tested.

## use for iPad(GoodReader)
to be written...

