from pytube import YouTube
import os

def progress(chunk,file_handle,remaining):
        global download_status
        file_downloaded = int(file_size-remaining)
        per = (file_downloaded/file_size)*100
        print(per)
    
def yt_downloader(url1, path):
    global file_size, download_status
    try:
       yt   = YouTube(url1,on_progress_callback=progress)
       if os.path.isdir(path):
           video = yt.streams.filter(progressive=True,file_extension='mp4').first()
           file_size = video.filesize
           video.download (path)
           print('Download Finish...' )
           
            
                
    except Exception as e:
        print(e)
        