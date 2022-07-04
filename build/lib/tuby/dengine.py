from pytube import YouTube
import os
#try:
#    import gui_alpha 

#except ModuleNotFoundError:
#    import tuby.gui_alpha 


def progress(chunk,file_handle,remaining):
    file_downloaded = int(file_size-remaining)
    per = (file_downloaded/file_size)*100
    gui_alpha.loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)



def yt_downloader():
    from gui_alpha import tuby_normal

    global file_size
    #download_button.config(state=DISABLED)
    
    gui_alpha.canvas.place(relx=0.5, rely=0.48, anchor=CENTER)#x=250,y=150)
    #canvas.config(anchor= CENTER)
    #canvas.pack(anchor=W, fill=X, expand=YES)an
    gui_alpha.loading_label.config(anchor = CENTER)
    gui_alpha.loading_label.place(relx=0.5, rely=0.70, anchor=CENTER)
    #loading_label.pack(side=TOP, anchor=W, fill=X, expand=YES) #.place(x=230,y=250)
    app.pack_forget()
    #loading_gif.place(x=180,y=50)
    try:
        url1 = gui_alpha.url.get()
        path = filedialog.askdirectory()
        yt   = YouTube(url1,on_progress_callback=progress)
        if os.path.isdir(path):
            video = yt.streams.filter(progressive=True,file_extension='mp4').first()
            file_size = video.filesize
            video.download (path)
            loading_label.config(text='Download Finish...' )
            loading_label.pack_forget()
            res = messagebox.askyesno("YouTube Video Downloader","Do youtube another video ?")
            if res == 1:
                loading_label.config(text = 'Restarted' )
                url.delete(0,END)
                #download_button.config(state= NORMAL)
                
            else:
                gui_alpha.on_closing()
        else:
            messagebox.showerror("error","no directory exist")
    except Exception as e :
        print(e)
        if(url.get()== ''):
            loading_label.config(text = 'Enter The URL')
            #download_button.config(state=NORMAL)
        else:
            loading_label.config(text = 'Failed! There is an error.')
            #elf.download_button.config(state=NORMAL)
    

def fb_download_video(html,quality):
    """Download the video in HD or SD quality"""
    print(f"\nDownloading the video in {quality} quality... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    #filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    #t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    #with open(filename + '.mp4', 'wb') as f:
    #    for data in file_size_request.iter_content(block_size):
    #        t.update(len(data))
    #        f.write(data)
    #t.close()
    print("\nVideo downloaded successfully.")