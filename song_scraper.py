import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import random
import sys

# extract artist name from url for text file name
def get_artist(url):
    url  = url.split('/')[-1]
    url = url.split('.')[0]
    return url

# scrape song links from artist page
def get_links(url, headers, base = "https://www.azlyrics.com/lyrics"):
    p = requests.get(url, headers=headers)

    soup = BeautifulSoup(p.content, 'html.parser').encode("utf-8")
    listAlbum = soup.find(id="listAlbum")
    a = listAlbum.find_all('a')

    links = []
    for link in a:
        links.append(link.get('href'))

    links = [link for link in links if link != None]
    links = [link.split('lyrics')[1] for link in links]
    links = [link for link in links if link != '.com/']
    links = [base+link for link in links]
    return links

# get text of song from song page
def get_song(url, headers):
    p = requests.get(url, headers = headers)
    print("got:\t{}\t{}".format(p,url))
    soup = BeautifulSoup(p.content, 'html.parser').encode("utf-8")
    main = soup.find(class_='container main-page')
    div_row = main.find(class_="row")
    div_col = div_row.find(class_='col-xs-12 col-lg-8 text-center')
    return div_col.find_all('div')[6].text

# write text to file
def write_to_file(file, text):
    with open(file, "a") as f:
        f.write(text+"\n\n")

# get songs from list of song links and writes to text file
def write_songs(links, headers, file):
    for url in links:
        sleep(random.randint(3,10))
        write_to_file(file, (get_song(url, headers).strip()+"\n\n"))

headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

url = ("https://www.azlyrics.com/m/macklemore.html" if len(sys.argv)<2 else sys.argv[1])

print(get_song(, headers = headers))

artist = get_artist(url)
file = artist+".txt"

links = get_links(url, headers = headers)
songs = write_songs(links, headers, file)
