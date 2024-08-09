# seoscan
SEOscan check the SEO of a website (TITLE, META description, keywords and robots, H1, H2, nb of words on the page, canonical + options are OpenGraph tags and robots.txt)

# version
V0.06.1 - 08/09/2024

# required
import sys<br>
import requests<br>
from bs4 import BeautifulSoup<br>
import urllib.robotparser<br>
import datetime<br>

# install
$ git clone https://github.com/CHFR91/seoscan.git<br>
$ cd seoscan<br>
$ chmod +x seoscan.py<br>

# usage
$ ./seoscan.py -d WWW.EXAMPLE.COM

# help
$ ./seoscan.py -h

# options
-d <www.example.com> and check the SEO of your site<br>
-o -- check OpenGraph tags<br>
-r -- read robots.txt<br>
-v -- verbose<br>
-h -- help + version<br>
-s -- sources<br>
