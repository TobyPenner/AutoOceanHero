import requests
from http.cookiejar import MozillaCookieJar

count = 1
url = "https://oceanhero.today/web?q=test"
cj = MozillaCookieJar('cookies.txt')
cj.load(ignore_expires=True)
while True:
    r = requests.get(url, cookies=cj)
    print(str(r) + " " + str(count))
    count += 1