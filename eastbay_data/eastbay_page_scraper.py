import requests
import os
import time

def main():
    url = "http://www.eastbay.com/Shoes/_-_/N-neZ1m2Z1z13y0m?Nao={}&Rpp=1000&cm_PAGE={}"
    pages_path = os.getcwd() + "/eastbay_pages"

    for i in range(13):
        num = i * 1000

        response = requests.get(url.format(num, num))

        with open(pages_path + "/eb_page%d.html" % i, "w") as out:
            out.write(response.text.encode("utf-8"))

        print "done page %d" % i
        time.sleep(10)


if __name__ == '__main__':
    pass
    # main()