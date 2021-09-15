#import youtube_dl
#/videos/best/2
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import re
import requests
'''parsed = urlparse.urlparse(url)
print(parsed)
parsed_path_split=parsed.path.split('/')
print(parsed_path_split)'''
def scrape_all(url):
    options = Options()
    options.headless = True
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
    driver = webdriver.Chrome(chromedriver, options=options)
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver.get(url)
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    return soup

def total_pages(soup):
    pagination_block = soup.find(class_="pagination ")
    try:  # then for a multi-page playlist (no pagination of pages)
        total = len(pagination_block.find_all('li')) - 1
    except AttributeError:  # handle single-page playlists (no pagination element)
        total = 1
    return total

def vids_find(page_url):
    soup = scrape_all(page_url)

    videos_block = soup.find(class_="mozaique")

    video_elements = videos_block.find_all(attrs={'data-id': True})
    """for video in video_elements:
        print(video.get('id'))"""
    return video_elements

def custom_dl_download(url):

    outtmpl = r'G:\내 드라이브\창고\history\folder\xvid\xvid' + r'/handpicked/%(title)s.%(ext)s'
    ydl_opts_start = {
        'format': 'best',
        'playliststart:': 1,
        'playlistend': 4,
        'outtmpl': outtmpl,
        'nooverwrites': True,
        'no_warnings': False,
        'ignoreerrors': True,
    }

    '''with youtube_dl.YoutubeDL(ydl_opts_start) as ydl:
        ydl.download([url])'''
def xvid_main(url):
    try:
        file=open('/xvidsave/xvideo.txt','a+')
    except FileNotFoundError:
        os.mkdir('/xvidsave/')


    file.close()
    slash_locs=url.split('/')
    url=slash_locs[0]+'//'+slash_locs[1]+'/'+slash_locs[2]+'/'+slash_locs[3]+'/'+slash_locs[4]

    vids_L=vids_find(url+'/videos/best')
    vids_num=len(vids_L)
    print(vids_num)
    page_no=2
    while True:
        vids=vids_find(url+'/videos/best/{}'.format(page_no))#[<div class="thumb-block" data-id="11000844" id="video_11000844"><div class="thumb-inside"><div class="thumb"><a href="/prof-video-click/upload/davidwiliams/11000844/sp-cheatinggf1_new_">]
        if len(vids[0].get("class"))>1:
            break

        vids_L.extend(vids)
        page_no+=1
    for vid in vids_L:
        print(vid.get('id'))

xvid_main("https://www.xvideos.com/profiles/davidwiliams/a/sdf")