#DBS - Übung05

# imports
from bs4 import BeautifulSoup
import requests
import csv

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: heise.de
def main():

    fobj = open('heise.csv', 'wb')      # open file
    csvw = csv.writer(fobj, delimiter = ';')      # create csv writer, set delimiter to ;

    h_url = "https://www.heise.de/thema/https"


    content = getPage(h_url)
    content = content.findAll("div", {"class":"keywordliste"})

    for c in content:
      c = c.findAll("header")
      txt = []
      for t in c:
        txt.append(t.text.encode('utf-8')) 
      for i in range(len(txt)):
        csvw.writerow([txt[i]])
         





    fobj.close()                     # close file
    print("\nDONE !\n\n\nheise.de was scraped completely.\n")



# main program

if __name__ == '__main__':
    main()
