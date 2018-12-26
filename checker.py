import requests 
from bs4 import BeautifulSoup

myfile = open('wordlist-wiki').read().split()
for i in myfile:
    try:
        url = str("https://www.instagram.com/" + i)
        print(url)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(url,headers=headers)
        html = response.content
        soup = BeautifulSoup(html , 'html.parser')
        page_title = str(soup.title.string)
        print(page_title)
        if "Page Not Found" in page_title:
            f = open("instagram" , 'a')
            f.write(i + "\n")
    
    except :
        f = open("insta-error" , 'a')
        f.write(i + "\n")