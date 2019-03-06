import re
import urllib.request
import urllib
def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk","ignore")
    return data
def getcode(data):
    #regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/([sh|sz].*?).html\">"
    regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat=re.compile(regex_str,re.IGNORECASE)
    codelist=pat.findall(data)
    return codelist


path="http://quote.eastmoney.com/stocklist.html"
data=getpage(path)
print(data)
codelist=getcode(data)
print(codelist)
print(len(codelist))

