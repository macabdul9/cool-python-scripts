"""
 @author    : macab (macab@debian)
 @file      : iplocator
 @created   : Tuesday Mar 19, 2019 01:25:28 IST
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup


class IPLocationFinder:
    def __init__(self):
        self.keycdn = "https://tools.keycdn.com/geo?host="

    def findIpLocation(self, ipaddr):
        self.keycdn = self.keycdn + ipaddr
        html_page = urlopen(self.keycdn)
        soup = BeautifulSoup(html_page, 'html.parser')

        jsonData = soup.find("table").text.strip()
        jsonData = jsonData.splitlines()

        dataLength = len(jsonData ) -1;
        for x in range(0, dataLength, 2):
            if jsonData[x] and jsonData[ x +1]:
                data = jsonData[x] + " = " + jsonData[ x +1]
                print(data)


    def startApp(self, ipaddr):
        if not ipaddr:
            print("Please enter a valid ip address!")
        else:
            self.findIpLocation(ipaddr)


if __name__ == "__main__":
    ipLoc = IPLocationFinder()
    ipLoc.startApp("103.248.34.41")
