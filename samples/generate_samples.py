import os
import random
import csv

def generate_indep_samples(sample_size):
    d_in = open(os.getcwd() + "/dsg_prices.txt")
    e_in = open(os.getcwd() + "/eb_prices.txt")

    dsg_prices = d_in.read().split(",")
    eb_prices = e_in.read().split(",")

    d_in.close()
    e_in.close()

    dsg_sample = random.sample(dsg_prices, sample_size)
    eb_sample = random.sample(eb_prices, sample_size)

    d_out = open(os.getcwd() + "/dsg_sample_%d.csv" % sample_size, "w")
    e_out = open(os.getcwd() + "/eb_sample_%d.csv" % sample_size, "w")

    d_csv = csv.DictWriter(d_out, fieldnames=("price",))
    e_csv = csv.DictWriter(e_out, fieldnames=("price",))

    d_csv.writeheader()
    e_csv.writeheader()

    for i in range(sample_size):
        d_csv.writerow({"price": dsg_sample[i]})
        e_csv.writerow({"price": eb_sample[i]})

    d_out.close()
    e_out.close()

def gen_paired_samples(sample_size):
    paired_in = open("/Users/akofke/stats_project/paired_data/paired_data.csv")

    prices_list = list()

    reader = csv.DictReader(paired_in)
    for line in reader:
        prices_list.append((line["dicksPrice"], line["eastbayPrice"]))

    paired_sample = random.sample(prices_list, sample_size)

    fields = ("dsgPrice", "ebPrice")
    out = open(os.getcwd() + "/paired_sample_%d" % sample_size, "w")
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()

    for line in paired_sample:
        writer.writerow({
            "dsgPrice": line[0],
            "ebPrice": line[1]
        })

    paired_in.close()
    out.close()


def main():
    # generate_indep_samples(100)
    gen_paired_samples(50)


if __name__ == '__main__':
    main()