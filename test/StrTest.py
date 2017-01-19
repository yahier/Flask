# -*- coding: UTF-8 -*-

#字符串格式化   除了s,d之外，更多的请查看python字符串格式化符号:
def format():
    print "My name is %s and age is %d kg!" % ('yahier', 27)


#是否包含
def contain(str):
    if ('bi' in str):
        print('包含了bi')
    else:
        print('没有包含bi')

    if ('ya' not in str):
        print('ya不在' + str + '之中')
    else:
        print('ya在' + str + '之中')
    print('')


if __name__ == '__main__':
    contain('yahier')
    format()
