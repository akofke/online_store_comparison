import os
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def main():
    in1 = open("/Users/akofke/stats_project/dicks_data/dicks_all_data.csv")
    in2 = open("/Users/akofke/stats_project/eastbay_data/eastbay_data_nosales.csv")

    reader1 = csv.DictReader(in1)
    reader2 = csv.DictReader(in2)

    dicks_names = list()
    dicks_prices = list()
    eastbay_names = list()
    eastbay_prices = list()
    for line in reader1:
        dicks_names.append(line["productName"].decode("utf-8"))
        dicks_prices.append(line["price"])

    for line in reader2:
        eastbay_names.append(line["productName"].decode("utf-8"))
        eastbay_prices.append(line["price"])

    dicks_data = dict(zip(dicks_names, dicks_prices))
    eastbay_data = dict(zip(eastbay_names, eastbay_prices))

    out = open(os.getcwd() + "/paired_data.csv", "w")
    fields = ("dicksName", "eastbayName", "dicksPrice", "eastbayPrice")
    paired_csv = csv.DictWriter(out, fieldnames=fields)
    paired_csv.writeheader()

    count = 0
    for eb_name in eastbay_names:
        match_tuple = process.extractOne(eb_name, dicks_names, score_cutoff=90)
        if match_tuple is not None:
            dicks_name = match_tuple[0]
            dicks_price = dicks_data[dicks_name]
            eb_price = eastbay_data[eb_name]

            paired_dict = {
                "dicksName": dicks_name.encode("utf-8"),
                "eastbayName": eb_name.encode("utf-8"),
                "dicksPrice": dicks_price,
                "eastbayPrice": eb_price
            }

            paired_csv.writerow(paired_dict)

        count += 1
        print count

    out.close()
    in1.close()
    in2.close()

if __name__ == '__main__':
    main()