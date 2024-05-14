#!/usr/bin/env python3

"""
Python script to check the SEO of a website.
Usage: ./seoscan-backup.py -d www.example.com
"""
import sys
import requests
from bs4 import BeautifulSoup


# Colours
class COLOUR:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to get the SEO from a web site
def get_info(site_url, valeur):
    response = requests.get(site_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        if valeur == 1:
            title = soup.find('title')
            if title:
                return title.text.strip()
        elif valeur == 2:
            meta_description = soup.find('meta', attrs={'name': 'description'})
            if meta_description:
                return meta_description['content']
        elif valeur == 3:
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            if meta_keywords:
                return meta_keywords['content']
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

        return "Error"
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


version = False
help = False
source = False
domain = None

if "-v" in sys.argv:
    version = True

if "-h" in sys.argv:
    help = True

if "-s" in sys.argv:
    source = True

if "-d" in sys.argv:
    domain = sys.argv[sys.argv.index("-d") +1]


if version:
    print("V0.02 - 05/14/2024\n\n")
    entree = False
elif help:
    print("-d <www.example.com>\n")
    print("-h -- help")
    print("-v -- version")
    print("-s -- source")
    entree = False
elif source:
    print("https://searchengineland.com/title-tag-length-388468 (04/25/2024)")
    print("https://searchengineland.com/write-meta-description-clicks-428217 (06/14/2023)")
    print("https://ahrefs.com/blog/meta-keywords/ (12/15/2020)")
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

    if check_domain(domain) == "Error":
        print(f"\n{COLOUR.FAIL}There is something wrong with your domain: {domain}!\{COLOUR.ENDC}n\n")
    else:
        a = check_domain(domain)
        b = domain
        domain = a + b

        # TITLE
        title = get_info(domain, 1)

        if title == "":
            print(f"\n{COLOUR.FAIL}No TITLE for {domain} !{COLOUR.ENDC}\n")
        else:
            print(f"\nThe TITLE is: {COLOUR.OKGREEN}{title}{COLOUR.ENDC}\n")

            title_length = len(title)
            print(f"The length of your TITLE is: {title_length}")
            if title_length <= 50:
                print(f"Of course, your TITLE is too short, you can add a few words to describe what is your page about.")
            elif title_length > 70:
                print(f"The TITLE of your site is too long, you have to think to remove some words in it !")
            else:
                print(f"Perfect length for your TITLE.")

        # META description
        meta = get_info(domain, 2)

        if meta == "":
            print(f"\n{COLOUR.FAIL}No META DESCRIPTION for {domain}!{COLOUR.ENDC}\n")
        else:
            print(f"\nThe META DESCRIPTION is: {COLOUR.OKGREEN}{meta}{COLOUR.ENDC}\n")

            meta_length = len(meta)
            print(f"The length of your META DESCRIPTION is: {meta_length}")
            if meta_length <= 150:
                print(f"Your META DESCRIPTION is too short. It is an important element of your SEO, write more about your page!")
            elif meta_length > 180:
                print(f"It is not useful to have a META DESCRIPTION which is so long.")
            else:
                print(f"Perfect length for your META DESCRIPTION.")

        # META keywords
        meta = get_info(domain, 3)

        if meta == "":
            print(f"\n{COLOUR.FAIL}No META KEYWORDS for {domain}!{COLOUR.ENDC}\n")
        else:
            print(f"\nThe META KEYWORDS are: {COLOUR.OKGREEN}{meta}{COLOUR.ENDC}\n")

