#coding:utf-8
import re
import urllib2
import sys
#import utils
from bs4 import BeautifulSoup

def getTitle():
    html = getPage(url)
    #解析html文档，解析器指定使用html.parser
    soup = BeautifulSoup(html, 'html.parser')   
    #传入列表参数,返回都匹配的内容 使用 class_ 参数搜索有指定CSS类名的tag
    #fandall返回列表，所以使用[0]选择第一个对象  h4 class="item-title"
    tag_a = soup.find_all("h4", class_="item-title")[0]
    title = re.findall("blank\">(.*)</a></h4>",str(tag_a))[0]
    tag_a = unicode(str(tag_a),'utf-8')
    print(u'标题:'),
    print(title)
    return title

def getDescription():
    html = getPage(url)
    #解析html文档，解析器指定使用html.parser
    soup = BeautifulSoup(html, 'html.parser')   
    #传入列表参数,返回都匹配的内容 使用 class_ 参数搜索有指定CSS类名的tag
    #fandall返回列表，所以使用[0]选择第一个对象  h4 class="item-title"
    tag_a = str(soup.find_all("div", class_="item-description")[0])
    #print(tag_a)
    description = re.findall("item-description\">(.*)...<", str(tag_a))[0]
    description = unicode(str(description),'utf-8')
    print(u"描述:"),
    print(description)
    return description

def getPrice():
    html = getPage(url)
    #解析html文档，解析器指定使用html.parser
    soup = BeautifulSoup(html, 'html.parser')   
    #传入列表参数,返回都匹配的内容 使用 class_ 参数搜索有指定CSS类名的tag
    #fandall返回列表，所以使用[0]选择第一个对象  h4 class="item-title"
    tag_a = str(soup.find_all("span", class_="price")[0])
    price = re.findall("<em>(.*)</em>", str(tag_a))[0]
    print(u"价格:"),
    print(price)
    return price

def getPage(url):
    '''下载文件html代码，找出一楼的核心代码'''
    #build_opener ()返回的对象具有open()方法，与urlopen()函数的功能相同 .
    #urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。
    opener = urllib2.build_opener()
    # 不加头信息则出现403错误和乱码
    # 添加Http报头
    opener.addheaders = [('User-agent', 'Mozilla/5.0')];
    htmlAll = opener.open(url).read()
    # 文件保存编码和文件编辑编码都是utf-8，所以decode一次，不然会出现乱码，但是不影响结果。
    return htmlAll

if __name__ == '__main__':
    url = "https://s.2.taobao.com/list/list.htm?spm=2007.1000337.6.2.syRomJ&st_edtime=1&q=macbook&ist=0"
    data=getPrice()
f = file('macbook.txt','w')    
f.write(data)
f.seek(f.tell())
f.write('\n\r')

data=getTitle()
#f.write(data)
#f.seek(f.tell())
#print(f.tell())
f.write('\n\r')

data=getDescription()
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
#f.write(data)
#f.seek(f.tell())
f.write('\n\r')
f.close


