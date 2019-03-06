
import urllib.request
import urllib
def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk","ignore")
    return data

path="http://quote.eastmoney.com/stocklist.html"
print(getpage(path))