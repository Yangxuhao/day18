import urllib
import urllib.request
import re
import os

def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk","ignore")
    return data
def getcode(data):
    #regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/([sh|sz].*?).html\">"
    regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat=re.compile(regex_str,re.IGNORECASE)
    codelist=pat.findall(data)
    return codelist
def downloadstock(code,name,date):
    path="E:股票数据\\"+date+"\\"
    isSZ=None
    if not os.path.exists(path):
        os.makedirs(path)
    if code[0:2]=="sh":
        isSZ=0
    else:
        isSZ=1
    #print(path)
    if isSZ!=None:
        url = "http://quotes.money.163.com/service/chddata.html?code="+str(isSZ)+code[2:]+"&end="+date+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        savepath =path+name+".csv"
        urllib.request.urlretrieve(url, savepath)


path="http://quote.eastmoney.com/stocklist.html"
data=getpage(path)
codelist=getcode(data)
for Stockdata in codelist:
    try:
        download=downloadstock(Stockdata[0],Stockdata[1],"20190101")
    except:
        print(Stockdata[0]+" error")