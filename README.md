articles
-------------------------

A bibtex based article manager

# Features
This is a HTML article manager based on BibTeX.
A HTML involving the informations of articles is generated from BibTeX file,
and some managing features, searching, tagging, are implemented by javascript.
The tagging datas are saved on a server,
so this project serve a HTML generator and simple CGI server.
Using this project,
You can view the informations of ariticles saved in BibTeX file by your favor web browser.
Since a static HTML is given,
it can be used on iPad or other tablet PCs same as on the PC.

# Install
## dependencies
The most part of this project is written in python2,
and depends on the following libraries.
* pybtex
* jinja2

For foramus distribution of Linux, at least on Fedora,
jinja2 can be found in the package manager (yum,apt,..).
However, pybtex might not be found,
so you have to install it manually.
Fortunately, pybtex can be installed by easy-install
    # easy-install pybtex

## usage
This script needs some configure values:
* [path.bib]        : the path for .bib file
* [path.outputdir]  : the path where you want to install .html and js/, css/, icons/
* [name.template]   : the name of template file used to generate HTML from .bib file
* [name.html]       : the name of generated HTML
* [name.database]   : the name of database that contains the tagging informations
* [server.port]     : the port of CGI server

These values are defined in ~/.articles.ini (default).
The sample of this configuration file is given in sample.ini.
*In order to use the link of HTML, the PDF files should place in outputdir/pdf/
and name as [bibtexkey].pdf.*

The main script is start.py.
This script can install necessaries and generate HTML to destination directory,
and also work as a CGI server.

### install (Linux)
Before install this program, please install pybtex and jinja2.
At first, you get the source code of this program:
    git clone http://github.com/termoshtt/ariticles.git
or please download .zip and extract.
Next go into the directory and copy the configure file to your $HOME:
    cd articles
    cp sample.ini ~/.articles.ini
You should modify the configure file now.
After configuration, generate HTML and copy js/, css/, icons/ to your install directory.
    ./start.py --install --no-cgi-server
if you do not want to place ~/.articles.ini, you can use other configure file:
    ./start.py -i -n -c path/to/configure.ini
--install can be abbreviate by -i and --no-cgi-server by -n.

Up to here, the installation is finished.
You can find articles.html (or name you set) in your install directory.

### normal use
After installed, you can start a CGI server as:
    ./start.py
Since tagging feature is implemented as a CGI,
the tagging cannot use unless the CGI server stands.
In other word, searching and tag choosing can be used without the CGI server.

(experimental)
The CGI server can daemonize by option -d:
    ./start.py -d
This feature have not fully tested.

