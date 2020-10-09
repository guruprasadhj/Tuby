from pytube import YouTube
from threading import *
from tkinter import *
from tkinter import filedialog,messagebox
import tubygui,os


    
def ytdownloader(url_link,loading_label):
    global file_size,per 

    try:
        url1 = url_link
        
        path = filedialog.askdirectory()
        per = tubygui.per
        yt   = YouTube(url1,on_progress_callback=tubygui.loading)
        if os.path.isdir(path):
            video = yt.streams.filter(progressive=True,file_extension='mp4').first()
            file_size = video.filesize
            video.download (path)
            tubygui.per.set('Download Finish...' )
            
            res = messagebox.askyesno("Youtubr Video Downloader","Do youtube another video ?")
            
            if res == 1:
                #tubygui.loading_label.config(text = 'Restarted' )
                #tubygui.url.delete(0,END)
                #tubygui.app.pack()
                print('okay')
                 
            else:
                print('noooo')
                #tubygui.root.destroy()
        else:
            messagebox.showerror("error","no directory exist")
                
                
    except Exception as e :
        print(e)

        """
        if(self.url.get()== ''):
            self.download_status.config(text = 'Enter The URL')
            self.download_button.config(state=NORMAL)
        else:
            self.download_status.config(text = 'Failed! There is an error.')
            self.download_button.config(state=NORMAL)
        """