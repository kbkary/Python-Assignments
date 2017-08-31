import bs4, requests

def amazonProductPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#addToCart > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    price = elem[0].text.strip()
    return price

price = amazonProductPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1504117455&sr=8-1&keywords=automate+the+boring+stuff+with+python')
print (price)
