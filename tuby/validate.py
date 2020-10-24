#!/usr/bin/python
import re
print(" [   OK   ] - Started regex module successfully imported in validate \n  ")
import time
print(" [   OK   ] - Started time module successfully imported in validate \n  ")
import urllib
print(" [   OK   ] - Started urllib module successfully imported in validate \n ")
import webbrowser
print(" [   OK   ] - Started webbrowser module successfully imported in validate \n ")
from urllib.request import urlopen
print(" [   OK   ] - Started urllib module successfully imported in validate \n ")
import requests
print(" [   OK   ] - Started requests module successfully imported in validate \n ")

def video_validation(url_link):
    regex_yt_video = re.compile(r'^(http(s)??\:\/\/)?(www\.)?((youtube\.com\/watch\?v=)|(youtu.be\/))([a-zA-Z0-9\-_])+',re.IGNORECASE)
    video = (re.match(regex_yt_video, url_link) is not None)
    return video

def playlist_validaton(url_link):
    regex_playlist = re.compile(r'^.*(youtu.be\/|list=)([^#\&\?]*).*')  #^.*(youtu.be\/|list=)([^#\&\?]*).*')
    playlist = (re.match(regex_playlist, url_link) is not None)
    return playlist

def fb_video_validation(url_link):
    regex_fb_video = re.compile(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com',re.IGNORECASE)
    fb_video = (re.match(regex_fb_video, url_link) is not None)
    return fb_video

def twit_video_validation(url_link):
    regex_tw_video = re.compile(r'https:\/\/twitter.com\/\w{1,15}\/status\/(\d{15,25})',re.IGNORECASE)
    tw_video = (re.match(regex_tw_video, url_link) is not None)
    return tw_video


def check(online_img,offline_img,):
    try:
        requests.get('https://www.google.com/').status_code
        #print('online')
        return online_img
        time.sleep(5)
        check_again(online_img,offline_img)
    except:
        
        #print('offline')
        return offline_img
        time.sleep(5)
        check_again(online_img,offline_img)
        
def check_again(online_img,offline_img):
    try:
        requests.get('https://www.google.com/').status_code
        #print('online')
        time.sleep(5)
        check(online_img,offline_img)
    except:
        #print('offline')
        time.sleep(5)
        check(online_img,offline_img)



def offline_check(url_link):
    link = ('')
    video = video_validation(url_link)
    playlist = playlist_validaton(url_link)
    fb_video = fb_video_validation(url_link)
    tw_video  = twit_video_validation(url_link)
    if(video == True):
        if(playlist == True):
            print('Its a playlist')
            link = ('ytplaylist')
            return link 
        else:
            print('Offline validation Sucess')
            link = ('ytvideo')
            return link 

    elif (fb_video == True):
        print('Its a fb video')
        link = ('fbvideo')
        return link

    elif (tw_video == True):
        print('Its a twitter video')
        link = ('twvideo')
        
        return link

    elif(video == False and url_link == 'Enter a Url')or(len(url_link)==0):
        print('urls is empty')

    else:
        #webbrowser.open('https://www.youtube.com/results?search_query=' + url_link )
        #print('type something')
        link = ('this not an url')
        return link


def fb_get_data(url_link):
    html = requests.get(url_link).content.decode('utf-8')

    _qualityhd = re.search('hd_src:"https',html)
    _qualitysd = re.search('sd_src:"https', html)
    _hd = re.search('hd_src:null', html)
    _sd = re.search('sd_src:null', html)
    lists = []
    _thelist = [_qualityhd, _qualitysd, _hd, _sd]
    print(_thelist)
    for id,val in enumerate(_thelist):
        if val != None:
            lists.append(id)
            print(lists) 
    return lists