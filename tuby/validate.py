#!/usr/bin/python
import re,requests,time,webbrowser,urllib
from urllib.request import urlopen

def video_validation(url_link):
    regex_video = re.compile(r'^(http(s)??\:\/\/)?(www\.)?((youtube\.com\/watch\?v=)|(youtu.be\/))([a-zA-Z0-9\-_])+',re.IGNORECASE)
    video = (re.match(regex_video, url_link) is not None)
    return video

def playlist_validaton(url_link):
    regex_playlist = re.compile(r'^.*(youtu.be\/|list=)([^#\&\?]*).*')  #^.*(youtu.be\/|list=)([^#\&\?]*).*')
    playlist = (re.match(regex_playlist, url_link) is not None)
    return playlist



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
    if(video == True):
        if(playlist == True):
            print('Its a playlist')
            link = ('ytplaylist')
            return link 
        else:
            print('Offline validation Sucess')
            link = ('ytvideo')
            return link 
    
    elif(video == False and url_link == 'Enter a Url')or(len(url_link)==0):
        print('urls is empty')

    else:
        #webbrowser.open('https://www.youtube.com/results?search_query=' + url_link )
        #print('type something')
        link = ('this not an url')
        return link
