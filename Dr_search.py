# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import optparse 
from sys import exit
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText('Dr.search'))


def help_page():
    project= optparse.OptionParser()  
    project.add_option("-u","--url",dest="url",help=" Write url")
    project.add_option("-w","--wordlist",dest="wordlist",help=" Write wordlist path")
    return project.parse_args()


def directory_search(input_url, input_wordlist):
    with open(input_wordlist, "r") as wordlist:
        for directory in wordlist:
            directory = directory.strip()
            test_url = input_url + "/" + directory
            response = requests.get(test_url)
            if response.status_code == 200:
                print("Found:", test_url)
            if response.status_code == 301:
                print("Redirect:", test_url)
                

try:
    (userİnput,argument)=help_page()
    directory_search(userİnput.url,userİnput.wordlist)
except KeyboardInterrupt:
    exit()
except TypeError:
	print("Usage: python3 dirScan.py -u http://target.com -w /wordlist/path")


