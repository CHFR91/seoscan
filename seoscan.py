#!/usr/bin/env python3

"""
Python script to check the TITLE and METAs of a web site.
Based on: https://github.com/chfr91/seoscan
Usage: ./seoscan.py
"""

import requests
from bs4 import BeautifulSoup

print("\n:'######::'########::'#######:::'######:::'######:::::'###::::'##::: ##:")
print("'##... ##: ##.....::'##.... ##:'##... ##:'##... ##:::'## ##::: ###:: ##:")
print(" ##:::..:: ##::::::: ##:::: ##: ##:::..:: ##:::..:::'##:. ##:: ####: ##:")
print(". ######:: ######::: ##:::: ##:. ######:: ##:::::::'##:::. ##: ## ## ##:")
print(":..... ##: ##...:::: ##:::: ##::..... ##: ##::::::: #########: ##. ####:")
print("'##::: ##: ##::::::: ##:::: ##:'##::: ##: ##::: ##: ##.... ##: ##:. ###:")
print(". ######:: ########:. #######::. ######::. ######:: ##:::: ##: ##::. ##:")
print(":......:::........:::.......::::......::::......:::..:::::..::..::::..::")
print("V0.01 - 05/11/2024")
print("\nSEOscan is a script that help you to check your SEO\n\n")

site_url = input("Please enter the web site that you want to scan (https://www.example.com): ")

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

# Function to get the info from a web site
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

# TITLE
title = get_info(site_url, 1)

if title == "":
  print(f"\n{COLOUR.FAIL}No TITLE for {site_url} !{COLOUR.ENDC}\n")
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
meta = get_info(site_url, 2)

if meta == "":
  print(f"\n{COLOUR.FAIL}No META DESCRIPTION for {site_url}!{COLOUR.ENDC}\n")
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
meta = get_info(site_url, 3)

if meta == "":
  print(f"\n{COLOUR.FAIL}No META KEYWORDS for {site_url}!{COLOUR.ENDC}\n")
else:
  print(f"\nThe META KEYWORDS are: {COLOUR.OKGREEN}{meta}{COLOUR.ENDC}\n")


# SOURCES for SEO
print(f"\n\nSOURCES:\n")
print(f"https://searchengineland.com/title-tag-length-388468 (04/25/2024)")
print(f"https://searchengineland.com/write-meta-description-clicks-428217 (06/14/2023)")
print(f"https://ahrefs.com/blog/meta-keywords/ (12/15/2020)")
