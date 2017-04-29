from bs4 import BeautifulSoup
import os
import re
import csv


def main():
    cwd = os.getcwd()
    product_regex = re.compile("prod-item")
    fields = ("productName", "price")
    products_set = set()

    with open(cwd + "/dicks_all_data.csv", "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
        csv_writer.writeheader()

        file_names = (name for name in os.listdir(cwd + "/dicks_pages") if not name.startswith("."))

        for file_name in file_names:
            with open(cwd + "/dicks_pages/" + file_name) as html_file:
                soup = BeautifulSoup(html_file.read())

                for tag in soup.find_all("li", product_regex):
                    price_tag = tag.find(class_="ourPrice2")

                    if price_tag is not None:
                        product_name = tag.find(class_="prod-title").get_text(strip=True)
                        product_price = tag.find(class_="ourPrice2").p.contents[0]

                        if product_name not in products_set:
                            products_set.add(product_name)
                            product_dict = {
                                "productName": product_name.encode("utf-8"),
                                "price": product_price.strip("$")
                            }
                            csv_writer.writerow(product_dict)
                        else:
                            print product_name + " " + file_name

            print "done %s" % file_name

if __name__ == '__main__':
    main()