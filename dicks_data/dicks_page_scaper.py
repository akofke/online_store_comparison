import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
import time


def main():
    strainer = SoupStrainer("div", id="contentRight")
    groups = ("mens", "womens", "kids")

    for group in groups:
        urls_file = open(os.getcwd() + "/urls/urls_%s.txt" % group)

        for url_line in urls_file:
            url = url_line.strip()
            category = url.split("_")[-1]
            url += "&ppp=2000"

            response = requests.get(url)
            page_soup = BeautifulSoup(response.text, parse_only=strainer)

            out = open(os.getcwd() + "/dicks_pages/%s_%s.html" % (group, category), "w")
            out.write(page_soup.encode("utf-8"))
            out.close()

            print "done %s %s" % (group, category)
            time.sleep(2)

        urls_file.close()
        time.sleep(30)


if __name__ == '__main__':
    pass
    # main()