import requests
import sys
from bs4 import BeautifulSoup
try:
    url = sys.argv[1]

    resp = requests.get(url).text

    soup = BeautifulSoup(resp, 'html.parser')

    mails = soup.select('[href^=mailto]')

    for mail in mails:
        print(mail.text)
except IndexError:
    print("usage: ./mailto.py <url>\n[*] ./mailto.py https://example.com")