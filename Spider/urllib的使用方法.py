#urllib模块中的方法
import urllib.request
import urllib
#1.urllib.request.urlopen(url[,data[,proxies]])
#打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作。
url='http://www.huajiao.com/category/1000'
html = urllib.request.urlopen(url)             #返回一个类似于文本对象
print(html.read())                             #read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
print(html.getcode())                          #返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
print(html.geturl())                           #返回请求的url
print(html.info())                             #返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息

req = urllib.request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with urllib.request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))