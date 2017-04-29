#!/usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup, SoupStrainer


def get_site():
    url = """http://www.dickssportinggoods.com/family/index.jsp?bc=CatGroup_MensRunningShoes_R1_C2_ViewAll&DeviceOptOut=1&categoryId=4418011&ppp=144"""
    page = requests.get(url)

    out = open("/Users/akofke/stats_project/page_test_cache.html", 'w')
    out.write(page.text.encode("utf-8"))
    out.close()


def main():
    # get_site()

    html_file = open("/Users/akofke/stats_project/page_test_cache.html")

    strainer = SoupStrainer("div", id="contentRight")
    regex = re.compile(r'prod-item')

    soup = BeautifulSoup(html_file.read(), parse_only=strainer)

    for tag in soup.find_all("li", regex):
        price_tag = tag.find(class_="ourPrice2")

        if price_tag is not None:
            product_name = tag.find(class_="prod-title").get_text(strip=True)
            product_price = tag.find(class_="ourPrice2").p.contents[0]
            print product_name
            print product_price.strip("$")





    # print soup.find_all("div", "ourPrice2")

    # out = open("/Users/akofke/stats_project/page_tests.html", 'w')
    # out.write(soup.prettify().encode("utf-8"))
    # out.close()
    # print soup.prettify()

if __name__ == '__main__':
    main()
