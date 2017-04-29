import os
import csv


def main():
    in1 = open("/Users/akofke/stats_project/dicks_data/dicks_all_data.csv")
    in2 = open("/Users/akofke/stats_project/eastbay_data/eastbay_data_nosales.csv")

    reader1 = csv.DictReader(in1)
    reader2 = csv.DictReader(in2)

    dsg_prices = list()
    eb_prices = list()

    for line in reader1:
        dsg_prices.append(line["price"])

    for line in reader2:
        eb_prices.append(line["price"])

    in1.close()
    in2.close()

    out1 = open(os.getcwd() + "/dsg_prices.txt", "w")
    out2 = open(os.getcwd() + "/eb_prices.txt", "w")

    for line in dsg_prices:
        out1.write(line + ",")

    for line in eb_prices:
        out2.write(line + ",")



if __name__ == '__main__':
    main()