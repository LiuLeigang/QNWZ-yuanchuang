# -*- coding: utf-8 -*-

import urllib2
import re
import os
def writeFile(url):
    output = open('./thefile.txt', "a")
    output.write(url)
    output.close()
    

def readcontent(url,ext = "mp3", output = "./"):
    #1.domain
    index = url.rfind("/");
    domain = url[0:index+1];
    
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #2.content
    content = response.read()
    #print content
    #3.resource
    #print content
    title = re.findall('<h2>(.*?)</h2>', content)
    # title = u"《" + title[0].decode('GBK') + u"》"
    # writeFile("《".decode('ANSI')) 
    writeFile(title[0]) 
    # writeFile("》".decode('ANSI')) 
    strMatch = re.findall('<p style="text-indent:2em;">[ \t\n\x0B\f\r]*?(.*?)[ \t\n\x0B\f\r]*?</p>', content, re.DOTALL)
    size = len(strMatch)
    for i in range(0,size,1):
        cont = strMatch[i]
        if cont.count('<br />') >0:
            continue
        writeFile(cont) 
    writeFile("\n\r\n\r\n\r") 
    
def handleOnePage(url):
    print 'handle :' + url + ' now...'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    mode = '\'([^\']+'+"html"+')\''
    pattern = re.compile(mode)
    strMatch = pattern.findall(content)
    size = len(strMatch)
    lenth = 0
    for i in range(0,size,1):
        one = strMatch[i]
        if not (one.startswith("/html/article/chengchangjishi/2016") or
			one.startswith("/html/article/chengchangjishi/2015") or
			one.startswith("/html/article/chengchangjishi/2014") or 
            one.startswith("/html/article/chengchangjishi/2013") or
            one.startswith("/html/article/chengchangjishi/2012") or 
            one.startswith("/html/article/chengchangjishi/2011")):
            continue
        lenth = lenth + 1
    # print "amount:" + str(lenth)
    for i in range(0,size,1):
        one = strMatch[i]
        if not (one.startswith("/html/article/chengchangjishi/2016") or
			one.startswith("/html/article/chengchangjishi/2015") or
			one.startswith("/html/article/chengchangjishi/2014") or 
            one.startswith("/html/article/chengchangjishi/2013") or
            one.startswith("/html/article/chengchangjishi/2012") or 
            one.startswith("/html/article/chengchangjishi/2011")):
            continue
        UrlItem = "http://www.qnwz.cn" + one
        readcontent(UrlItem)
        # print "remain:"  + str(lenth - i - 1)

def obtainPages(url):
    pages = []
    #1.domain
    index = url.rfind("/");
    domain = url[0:index+1];
    
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #2.content
    content = response.read()
    #print content
    #3.resource
    #print content
    # pattern = '<span class="pageinfo">共 <strong>(.*?)</strong>页<strong>(.*?)</strong>条</span>'
    pattern = '<span class="pageinfo">(.*?)</span>'
    pageinfo = re.findall(pattern, content, re.DOTALL)[0]
    pageNum = re.findall('<strong>(.*?)</strong>', pageinfo, re.DOTALL)[0]
    pageNumber = int(pageNum)
    for i in range(1, pageNumber + 1, 1):
        pageAddr = 'http://www.qnwz.cn/html/article/chengchangjishi/118-' + str(i) + '.html'
        pages.append(pageAddr);
        handleOnePage(pageAddr)
        print "remain:"  + str(pageNumber - i) + ' pages...'
    
if __name__=='__main__':
    url = "http://www.qnwz.cn/html/article/chengchangjishi/";
    obtainPages(url);
    # url = "http://www.qnwz.cn/html/article/chengchangjishi/201604/04-621447.html";
    
    
