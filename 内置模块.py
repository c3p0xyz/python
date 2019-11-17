from urllib import request
import webbrowser

url = "http://www.baidu.com"

data = request.urlopen(url).read()
#print(data.decode())

webbrowser.open("http:www.hao123.com")