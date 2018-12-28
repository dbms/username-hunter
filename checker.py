import requests 
from bs4 import BeautifulSoup

myfile = open('wordlist-wiki').read().split()
for i in myfile:
    try:
        url = str("https://www.codechef.com/users/" + i) # enumeration of usernames
        print(url)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(url,headers=headers)
        html = response.content
        soup = BeautifulSoup(html , 'html.parser')
        page_title = str(soup.title.string)
        print(page_title)
        if "Error Page" in page_title: # see the error message in title
            f = open("avaiable-usernames" , 'a')
            f.write(i + "\n")
    
    except :
        f = open("errors" , 'a')
        f.write(i + "\n")
