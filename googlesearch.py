import sys, requests, bs4, webbrowser

# downloading google search page with search keywords
res = requests.get('https://www.google.co.in/search?q=' + ' '.join(sys.argv[1:]))

# html parsing of downloaded web page
soup = bs4.BeautifulSoup(res.text)

# css selection of search links
elems = soup.select('.r a')

# opening the selected links in new tabs of browser
for i in range(min(5,len(elems))):
    webbrowser.open_new_tab('https://www.google.co.in/'+elems[i].get('href'))
