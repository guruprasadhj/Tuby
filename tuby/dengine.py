from pytube import YouTube
from tkinter import filedialog,messagebox
import os
#from gui import ui 
#import gui

def ytdownloader(url_link):
    global file_size,file_handle,remaining
    url1 = url_link
    path = filedialog.askdirectory()
     
    yt = YouTube(url1)#on_progress_callback= gui.ui.loading)        
     
     
    if os.path.isdir(path):
        video = yt.streams.filter(progressive=True,file_extension='mp4').first()
        file_size = video.filesize
        video.download (path)
        print('download finished')
    else:
        messagebox.showerror("error","no directory exist")
                
                
    
def progress(self,chunk,file_handle,remaining):

        file_downloaded = int(file_size-remaining)
        per = str((file_downloaded/file_size)*100
        #loading_label.config(text='{:00.0f} % downloaded'.format(per))