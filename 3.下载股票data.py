import urllib
import urllib.request
import re

# url="https://cn.bing.com/az/hprichbg/rb/WinterGrand_ZH-CN5111542555_1920x1080.jpg"
# path=r"E:\股票数据\1.jpg"
# urllib.request.urlretrieve(url,path)

url="http://quotes.money.163.com/service/chddata.html?code=1300133&end=20190101&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
path=r"E:\股票数据\300133.csv"
urllib.request.urlretrieve(url,path)