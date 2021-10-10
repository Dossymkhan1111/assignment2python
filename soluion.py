import requests
from bs4 import BeautifulSoup
r = requests.get('https://decrypt.co/81612/bitcoin-org-compromised-fraudulent-crypto-giveaway-advertised?&utm_medium=referral&utm_campaign=feed&utm_source=coinmarketcap')
f = open("index.txt", "w", encoding='utf-8')
f.write(r.text)
f.close()

with open("index.txt", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

rp = soup.find_all("p")



for i in rp:
    print(i)