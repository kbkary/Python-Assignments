import requests, bs4, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img1 = soup.select('#comic img')
    if (img1==[]):
        print('Could not find any comic...')
    else:
        
        print (img1[0].get('src'))
        try:
            comicUrl = 'http:' + img1[0].get('src')
            res1 = requests.get(comicUrl)
            res1.raise_for_status()
        except:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        comicFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunks in res1.iter_content(100000):
            comicFile.write(chunks)
    
        comicFile.close()
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')







