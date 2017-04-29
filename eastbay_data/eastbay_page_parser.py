from bs4 import BeautifulSoup
import os
import csv

products_set = set()


def parse_page(page):
    items = page.find("div", id="endeca_search_results").ul

    def valid_item(tag):
        return tag.name == "li" and not tag.has_attr("class")

    for item in items.find_all(valid_item):
        name = item.a.get_text(strip=True)
        if name not in products_set:
            products_set.add(name)

            price_tag = item.find("p", class_="product_price")

            if price_tag.contents[0].name == "strike":
                nosale_price = price_tag.find("strike").get_text().strip("$")
                sale_price = price_tag.find("em").get_text().strip("Now $")
            else:
                nosale_price = price_tag.get_text().strip("$")
                sale_price = nosale_price

            nosales_dict = {"productName": name.encode("utf-8"), "price": nosale_price}
            sales_dict = {"productName": name.encode("utf-8"), "price": sale_price}

            yield nosales_dict, sales_dict
        else:
            print name



def main():
    path = os.getcwd() + "/eastbay_pages/"
    fields = ("productName", "price")

    nosales_file = open(os.getcwd() + "/eastbay_data_nosales.csv", "w")
    sales_file = open(os.getcwd() + "/eastbay_data_withsales.csv", "w")

    csv_sales = csv.DictWriter(sales_file, fieldnames=fields)
    csv_nosales = csv.DictWriter(nosales_file, fieldnames=fields)
    csv_sales.writeheader()
    csv_nosales.writeheader()

    for i in range(13):
        with open(path + "eb_page%d.html" % i) as html_file:
            page = BeautifulSoup(html_file.read())

            for nosales_dict, sales_dict in parse_page(page):
                csv_nosales.writerow(nosales_dict)
                csv_sales.writerow(sales_dict)

    nosales_file.close()
    sales_file.close()

if __name__ == '__main__':
    main()

