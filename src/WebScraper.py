'''
Written by Tarun Ramkumar
Reused with permission by Lea Frost for PA 6
Some modifications made
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import os

#Make sure URLs are HTML version of website links. To do this, open the company's 10k in the EDGAR viewer, then click the menu button. There should be an option to open in the HTML view. Click this, and this is the URL you should use.
'''
Scrapes the company 10-k and saves it to a text file only if it wasn't already scraped

Parameters:
    url (string): URL to the company 10k file
    output_file (string): path to the company text file 
'''
def scrapeFile(url, output_file):

    #handle if file not found
    try:

        #get the size of the file
        file_size = os.path.getsize(output_file)

        #only scrape if file is empty (hasn't already been scraped)
        if (file_size == 0):

            #open file
            file = open(output_file,"w", encoding =  "utf-8")

            #html request
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }
            req = Request(
            url=url, 
            headers=headers
            )
            website = requests.get(url = url, headers = headers)
            html = website.content.decode("utf-8")
            parser = BeautifulSoup(html,"html.parser")
            start = False
            headers = []

            #write each line to the file
            for i in parser.stripped_strings:

                line = str(i)

                #only start writing once beginning of 10k is reached
                if "UNITED" in i and start == False:
                    start = True

                if(start):
                    #ignore extra lines
                    if(len(line) > 1):
                        #write line to file
                        file.write(line+"\n")
            file.close

    except FileNotFoundError as e:
        print("\nERROR - Company file not found\n")
                
#scrape 10ks for apple and amazon
def scrape10ks():
    #Apple
    scrapeFile("https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm", "data/input/Apple-2023.txt")
    #Amazon
    scrapeFile("https://www.sec.gov/Archives/edgar/data/0001018724/000101872423000004/amzn-20221231.htm", "data/input/Amazon-2022.txt")
