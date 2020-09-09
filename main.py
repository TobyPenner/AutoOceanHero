import requests
import threading
from http.cookiejar import MozillaCookieJar

total_count = 1

def main(threadname):
    global total_count
    url = "https://oceanhero.today/web?q=test"
    cj = MozillaCookieJar('cookies.txt')
    cj.load(ignore_expires=True)
    while True:
        requests.get(url, cookies=cj)
        print(f"<{threadname}> {total_count}")
        total_count += 1

threads = list()
for index in range(10):
    thread = threading.Thread( target=main, args=(f"Thread{index+1}",))
    threads.append(thread)
    thread.start()
