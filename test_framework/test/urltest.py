import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("UTF-8"))
