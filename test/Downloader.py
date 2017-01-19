# download url is a simple thing.maybe it is not need to use a file.
import urllib2


def down(url):
    response = urllib2.urlopen(url)
    if (response.getcode() == 200):
        return response.read()
    else:
        return "code error"



def downWithData():
    request = urllib2.Request("http://www.baidu.com")
    data = {}
    data['age'] = '2'
    request.add_data("2")#add paramnters. can't be dict params
    request.add_header("User-Agent","Chrome")
    response = urllib2.urlopen(request)
    return response.read()

print(downWithData())
