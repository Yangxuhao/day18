import urllib
import urllib.request
import re

def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk","ignore")
    return data
def runpage(min,max):
    for page in range(min,max):
        mystr="https://quote.stockstar.com/stock/sha_3_1_"+str(page)+".html"


def gettbody(data):
    pat=re.compile("<tbody>[\s\S]*</tbody>")
    body=pat.findall(data)
    return body

#print(getpage(r"https://quote.stockstar.com/stock/sha_3_1_1.html"))
data=getpage(r"https://quote.stockstar.com/stock/sha_3_1_1.html")
print(gettbody(data))