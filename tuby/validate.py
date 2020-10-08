#!/usr/bin/python
import re
def video_validation(url_link):
    regex_video = re.compile(r'^(http(s)??\:\/\/)?(www\.)?((youtube\.com\/watch\?v=)|(youtu.be\/))([a-zA-Z0-9\-_])+',re.IGNORECASE)
    video = (re.match(regex_video, url_link) is not None)
    return video

def playlist_validaton(url_link):
    regex_playlist = re.compile(r'^.*(youtu.be\/|list=)([^#\&\?]*).*')
    playlist = (re.match(regex_playlist, url_link) is not None)
    return playlist

def redirect_link(url_link):
    video = video_validation(url_link)
    playlist = playlist_validaton(url_link)
    if(video == True):
        if(playlist == True):
            print('Its a playlist')
        else:
            print('Offline validation Sucess')
    
    elif(video == False and url_link == 'Enter a Url'):
        print('urls is empty')
    
    else:
        print('type something')
