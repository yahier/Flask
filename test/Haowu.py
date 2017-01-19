# -*- coding: UTF-8 -*-
from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup
import sys


nuomi = 'https://gz.nuomi.com'
nuomiSearch ='https://www.nuomi.com/search?k='


def testurl(keyword):
    doc=urlopen(nuomiSearch+keyword).read()
    print(doc)


def testSoup(keyword):
    print('keyword:'+keyword)
    req = urllib2.Request(nuomiSearch+keyword)
    webpage = urllib2.urlopen(req)


    soup = BeautifulSoup(webpage.read( ),'lxml')

    con = soup.find_all("span", class_="price")# tag
    for item in con:

        print(item)



    #到了这一层，怎么继续往下呢
    #soup = BeautifulSoup(cons.source,'lxml')






#get content of url 哈哈
def gethtml(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
	return html

def main():
    pass


if __name__ == '__main__':
    #keyword = sys.argv[1]
    keyword = '海底捞'
    testSoup(keyword)







