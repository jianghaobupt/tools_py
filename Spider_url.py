#coding=utf-8
import urllib
import urllib2
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

def getHeader(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    header = response.info()
    return header

html = getHtml("http://tieba.baidu.com/p/2460150866")

print getHeader("http://tieba.baidu.com/p/2460150866")
# print getImg(html)
print html