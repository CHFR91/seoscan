#!/usr/bin/env python3

"""
Python script to check the SEO of a website.
Usage: ./seoscan.py -d www.example.com
"""
import sys
import requests
from bs4 import BeautifulSoup
import urllib.robotparser
import datetime


# Colours
class COLOUR:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


# Function to get the SEO from a web site
def get_info(site_url, valeur, verbose):
    response = requests.get(site_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # TITLE
        if valeur == 1:
            title = soup.find('title')
            if title:
                title = title.text.strip()
                print(f"\nThe TITLE is: {COLOUR.OKGREEN}{title}{COLOUR.ENDC}\n")

                if verbose:
                    title_length = len(title)
                    print(f"The length of your TITLE is: {title_length}")
                    if title_length <= 50:
                        print(
                            f"Of course, your TITLE is too short, you can add a few words to describe what is your page "
                            f"about.")
                    elif title_length > 70:
                        print(f"The TITLE of your site is too long, you have to think to remove some words in it !")
                    else:
                        print(f"Perfect length for your TITLE.")
            else:
                print(f"\n{COLOUR.FAIL}No TITLE for {domain}!{COLOUR.ENDC}\n")
        # META description
        elif valeur == 2:
            meta_description = soup.find('meta', attrs={'name': 'description'})
            if meta_description:
                meta = meta_description['content']
                print(f"\nThe META DESCRIPTION is: {COLOUR.OKGREEN}{meta}{COLOUR.ENDC}\n")

                if verbose:
                    meta_length = len(meta)
                    print(f"The length of your META DESCRIPTION is: {meta_length}")
                    if meta_length <= 150:
                        print(f"Your META DESCRIPTION is too short. It is an important element of your SEO, write more "
                              f"about your page!")
                    elif meta_length > 180:
                        print(f"It is not useful to have a META DESCRIPTION which is so long.")
                    else:
                        print(f"Perfect length for your META DESCRIPTION.")
            else:
                print(f"\n{COLOUR.FAIL}No META DESCRIPTION for {domain}!{COLOUR.ENDC}\n")
        # META keywords + robots
        elif valeur == 3:
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            if meta_keywords:
                print(f"\nThe META KEYWORDS are: {COLOUR.OKGREEN}{meta_keywords['content']}{COLOUR.ENDC}\n")
            else:
                print(f"\n{COLOUR.FAIL}No META KEYWORDS for {domain}!{COLOUR.ENDC}\n")

            meta_robots = soup.find('meta', attrs={'name': 'robots'})
            if meta_robots:
                print(f"\nThe META ROBOTS are: {COLOUR.OKGREEN}{meta_robots['content']}{COLOUR.ENDC}\n")
            else:
                print(f"\n{COLOUR.FAIL}No META ROBOTS for {domain}!{COLOUR.ENDC}\n")

        # H1
        elif valeur == 4:
            nb_hun = soup.find_all('h1')
            hun_count = len(nb_hun)
            if hun_count == 0:
                print(f"\nH1 but I can't get it!\n")
            elif hun_count == 1:
                hun = soup.find('h1')
                hun = hun.text.strip()
                if hun:
                    print(f"\nH1 is: {COLOUR.OKGREEN}{hun}{COLOUR.ENDC}\n")

                    if verbose:
                        hun_length = len(hun)
                        print(f"The length of your H1 is: {hun_length}")
                        if hun_length <= 30:
                            print(
                                f"Your H1 is too short, you can add a few more words to describe what is your page "
                                f"about.\n")
                        elif 50 >= hun_length > 30:
                            print(f"Try to add some more words in your H1.\n")
                        elif hun_length > 70:
                            print(f"The H1 of your site is too long, you have to think to remove some words in it !\n")
                        else:
                            print(f"Perfect length for your H1.\n")
                else:
                    print(f"\n{COLOUR.FAIL}ERROR that shouldn't happen!{COLOUR.ENDC}\n")
            elif hun_count >= 2:
                print(f"\n{COLOUR.FAIL}Several H1 for {domain} when there must be one.{COLOUR.ENDC}\n")
            else:
                print(f"\n{COLOUR.FAIL}No H1 for {domain}!{COLOUR.ENDC}\n")
        # H2
        elif valeur == 5:
            nb_hde = soup.find_all('h2')
            hde_count = len(nb_hde)
            if hde_count == 0:
                print(f"\n{COLOUR.FAIL}There is no <H2> in your page!{COLOUR.ENDC}")

                if verbose:
                    print(f"It is important to add subheadings (<H2>) to separate the different themes of your page.!")
            else:
                print(f"\nNumber of `<H2>` tags: {hde_count}")
                if verbose:
                    for hde in nb_hde:
                        print("-----------------")
                        ltext = len(hde.text)
                        print(f"{COLOUR.OKGREEN}{hde.text}{COLOUR.ENDC} ({ltext})")

                    print(f"\nDon't make your <H2> too short or too long. This is a good place to put your important "
                          f"keywords.\n")
                    print(f"Your text after a <h2> must be around 250 words long.\nIf you have some <H3>, it must be "
                          f"150 words long after them.")
                else:
                    for hde in nb_hde:
                        print("-----------------")
                        print(f"{COLOUR.OKGREEN}{hde.text}{COLOUR.ENDC}")
            print(f"\n")

        # Words in the page + Canonical
        elif valeur == 6:
            text = soup.get_text()
            words = text.split()
            word_count = len(words)

            print(f"\nNUMBER OF WORDS on this web page ({site_url}): {COLOUR.OKGREEN}{word_count}{COLOUR.ENDC}\n")
            if verbose:
                print(f"Length of your page:\n"
                      f"- {COLOUR.OKBLUE}400 / 500 words:{COLOUR.ENDC} for a text of a niche expression\n"
                      f"- {COLOUR.OKBLUE}1000 words:{COLOUR.ENDC} for a text of mid-tail query\n"
                      f"- {COLOUR.OKBLUE}1500 words:{COLOUR.ENDC} for a text of a competitive expression\n")

            # Canonical tag
            canonical_tag = soup.find('link', rel='canonical')

            print(f"\nThe CANONICAL TAG tells search engines which is the original, preferred version "
                  f"of a page, thus avoiding duplicate content issues.\n")

            if canonical_tag is None:
                print(f"{COLOUR.FAIL}No canonical tag found on {site_url}!{COLOUR.ENDC}\n")
            else:
                print(f"The canonical of {site_url} is: {COLOUR.OKGREEN}{canonical_tag['href']}{COLOUR.ENDC}\n")

        # OpenGraph protocol
        elif valeur == 7:
            if opengraph:
                def get_opengraph_tags(soup):
                    opengraph = {}
                    for meta in soup.find_all('meta'):
                        if meta.get('property') and meta['property'].startswith('og:'):
                            opengraph[meta['property']] = meta.get('content')
                    return opengraph

                tags = get_opengraph_tags(soup)

                if not tags:
                    print(f"\n{COLOUR.FAIL}You do not have OpenGraph tags on {site_url}!{COLOUR.ENDC}\n")
                if tags:
                    print(f"\nYour OpenGraph tags are :\n")

                    for key, value in tags.items():
                        print(f"{key}: {value}")
                    print(f"\n")

                    og_description = soup.find('meta', property='og:description')
                    og_description_len = len(og_description['content'])

                    print(f"Length of the OPEN GRAPH DESCRIPTION is {COLOUR.OKGREEN}{og_description_len}{COLOUR.ENDC}\n")

                    if verbose:
                        if og_description_len < 80:
                            print(f"\nYour OPEN GRAPH DESCRIPTION is too short. You can had some more words in it.\n")
                        elif og_description_len > 120:
                            print(f"\nBe careful, the length of your OPEN GRAPH DESCRIPTION is too long, it is good "
                                  f"to shorten it.\n")
                        else:
                            print(f"\nPerfect length for your OPEN GRAPH DESCRIPTION.\n")

        # robots.txt
        elif valeur == 8:
            if robots:
                rp = urllib.robotparser.RobotFileParser()
                rp.set_url(site_url + "/robots.txt")
                rp.read()

                if not rp.mtime():
                    print(f"\n{COLOUR.FAIL}You do not have a robots.txt on {site_url}!{COLOUR.ENDC}\n")
                if rp.mtime():
                    print(f"\n{COLOUR.OKGREEN}You have a robots.txt on {site_url}!{COLOUR.ENDC}\n")
                    normaltime = datetime.datetime.fromtimestamp(rp.mtime())
                    print(f"Last time your robots.txt was read: {normaltime}\n")
                    print(f"{COLOUR.ITALIC}-v to read your robots.txt but, be careful, it can be pretty "
                          f"long!{COLOUR.ENDC}\n")
                    if verbose:
                        print(rp)
                        print(f"\n")

    else:
        print(f"ERROR: Impossible to get the page of {site_url}")
        exit()
    return ''


# Function to know the protocol of a domain
def check_domain(domain):
    try:
        response = requests.head(f"http://{domain}")
        if response.status_code == 200:
            return "http://"

        response = requests.head(f"https://{domain}")
        if response.status_code == 200:
            return "https://"

        return "https://"
    except requests.exceptions.RequestException:
        return "Error"


# Banner
print("\n:'######::'########::'#######:::'######:::'######:::::'###::::'##::: ##:")
print("'##... ##: ##.....::'##.... ##:'##... ##:'##... ##:::'## ##::: ###:: ##:")
print(" ##:::..:: ##::::::: ##:::: ##: ##:::..:: ##:::..:::'##:. ##:: ####: ##:")
print(". ######:: ######::: ##:::: ##:. ######:: ##:::::::'##:::. ##: ## ## ##:")
print(":..... ##: ##...:::: ##:::: ##::..... ##: ##::::::: #########: ##. ####:")
print("'##::: ##: ##::::::: ##:::: ##:'##::: ##: ##::: ##: ##.... ##: ##:. ###:")
print(". ######:: ########:. #######::. ######::. ######:: ##:::: ##: ##::. ##:")
print(":......:::........:::.......::::......::::......:::..:::::..::..::::..::")
print(f"\n{COLOUR.OKCYAN}... SEOscan is a script that helps you check your SEO ...{COLOUR.ENDC}\n\n")


help = False
source = False
domain = None
verbose = False
opengraph = False
robots = False

if "-h" in sys.argv:
    help = True

if "-s" in sys.argv:
    source = True

if "-v" in sys.argv:
    verbose = True

if "-o" in sys.argv:
    opengraph = True

if "-r" in sys.argv:
    robots = True

if "-d" in sys.argv:
    domain = sys.argv[sys.argv.index("-d") +1]
    help = False
    source = False

if help:
    print("V0.06.1 - 08/09/2024\n\n")
    print("-d <www.example.com> and check the SEO of your site")
    print("-o -- check OpenGraph tags")
    print("-r -- read robots.txt")
    print("-v -- verbose\n")
    print("-h -- help + version")
    print("-s -- sources")
    entree = False
elif source:
    print("https://github.com/CHFR91/seoscan\n")
    print("https://searchengineland.com/title-tag-length-388468 (04/25/2024)")
    print("https://searchengineland.com/write-meta-description-clicks-428217 (06/14/2023)")
    print("https://ahrefs.com/blog/meta-keywords/ (12/15/2020)")
    print("https://ahrefs.com/blog/h1-tag/ (05/11/2021)")
    print ("https://ogp.me/")
    print ("http://www.robotstxt.org/")
    entree = False
elif domain:
    if "http://" in domain:
        print(f"\n{COLOUR.FAIL}You mustn't write your domain with http:// or https://{COLOUR.ENDC}")
        entree = False
    elif "https://" in domain:
        print(f"\n{COLOUR.FAIL}You mustn't write your domain with http:// or https://{COLOUR.ENDC}")
        entree = False
    else:
        entree = True
else:
    domain = input("Please enter the web site that you want to scan (www.example.com): ")
    if "http://" in domain:
        print(f"\n{COLOUR.FAIL}You mustn't write your domain with http:// or https://{COLOUR.ENDC}")
        entree = False
    elif "https://" in domain:
        print(f"\n{COLOUR.FAIL}You mustn't write your domain with http:// or https://{COLOUR.ENDC}")
        entree = False
    else:
        entree = True


if entree:

    a = check_domain(domain)
    b = domain
    domain = a + b

    get_info(domain, 1, verbose)
    get_info(domain, 2, verbose)
    get_info(domain, 3, verbose)
    get_info(domain, 4, verbose)
    get_info(domain, 5, verbose)
    get_info(domain, 6, verbose)
    get_info(domain, 7, verbose)
    get_info(domain, 8, verbose)

