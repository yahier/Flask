# -*- coding: UTF-8 -*-
from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup

# BeautifulSoup 4种对象
# BeautifulSoup表示一个文档的全部内容，大部分时候可以把它看做一个Tag
# Tag对应xml或html中的tag相同，可以获取名称 属性，Tag可以包含Tag
#    有parent parents children descendants
#    find_all(["a", "b"])   find_all('p', class_='story') find_all(id='link2') 查看文档吧
# NavigableString 类来包装tag中的字符串
# Comment对应注释 是一个特殊类型的 NavigableString 对象:
# 查看 https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/


def main():
    soup = BeautifulSoup(open('test.html'), 'lxml')
    ps = soup.find_all('p', class_='story')  # ResultSet Tag的集合
    # print(soup.get_text())#获取整个文档的内容
    for p in ps:
        len = list(p.children)
        for c in p.children:
            print(type(c))
            # print(c) #直接输出子节点的内容
        # pcontent = p.get_text() #得到Tag的内容
        # pContent =pContent.replace('\n',"").replace(" ","")#去掉空格，和去掉换行符
        # print(pcontent)
        print('\n')

    # print(soup.p.get_text())
    # print(soup.title.string)
    # print soup.title


if __name__ == '__main__':
    main()
