import requests
import BeautifulSoup

#get page html
def get_html():
    url = 'https://www.nytimes.com/'
    response = requests.get(url)
    response_html = response.text
    
    return response_html


soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string