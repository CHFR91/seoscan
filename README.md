# seoscan
SEOscan check the SEO of a website (TITLE, META description, keywords and robots, H1, H2, nb of words on the page, canonical + options are OpenGraph tags and robots.txt)

# version
V0.06.1 - 08/09/2024

# required
import sys
import requests
from bs4 import BeautifulSoup
import urllib.robotparser
import datetime

# install
$ git clone https://github.com/CHFR91/seoscan.git<br>
$ cd seoscan<br>
$ chmod +x seoscan.py<br>

# usage
$ ./seoscan.py -d WWW.EXAMPLE.COM

# help
$ ./seoscan.py -h

# options
-d <www.example.com> and check the SEO of your site
-o -- check OpenGraph tags
-r -- read robots.txt
-v -- verbose
-h -- help + version
-s -- sources
