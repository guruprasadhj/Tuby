import multiprocessing
import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox
from turtle import *

import pyfiglet
import pyperclip
import requests
from PIL import Image, ImageTk
from pytube import YouTube

try:
    print('hello')
    import tuby.validate
    
except ModuleNotFoundError:
    import validate

file_size = 0
class GifLabel(Label):       #only gif player 
    global GifLabel 
    def __init__(self, master, filename,frame): 
        gif_image = Image.open(filename) 
        seq = [] 
        try: 
            while 1: 
                seq.append(gif_image.copy()) 
                gif_image.seek(len(seq)) # skip to next frame 
        except EOFError: 
            pass # we're done 
 
        try: 
            self.delay = frame #gif_image.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)] 

        Label.__init__(self, master, image=self.frames[0],bg='#000000',border=0) 

        temp = seq[0] 
        for image in seq[1:]: 
            temp.paste(image) 
            frame = temp.convert('RGBA') 
            self.frames.append(ImageTk.PhotoImage(frame)) 
 
        self.idx = 0 
 
        self.cancel = self.after(self.delay, self.play) 
 
    def play(self): 
        self.config(image=self.frames[self.idx]) 
        self.idx += 1 
        if self.idx == len(self.frames): 
            self.idx = 0 
        self.cancel = self.after(self.delay, self.play)


class ui():
    def __init__(self):
        print("Welcome to Tuby Downloader")
        print(pyfiglet.figlet_format("Tuby", font = "slant"  ) )
        print("Copyright (c) 2020 guruprasadh_j")
        
        self.page_Num = 1
        self.srcPath = os.path.dirname(os.path.abspath(__file__))
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #root.overrideredirect(True)
        #root.wm_attributes('-type', 'splash')
        #root.update_idletasks()
        self.root['bg'] = ('black') #202020
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width/2) - (600/2)
        y_coordinate = (screen_height/2) - (350/2)
        self.root.geometry("{}x{}+{}+{}".format(600, 350, int(x_coordinate), int(y_coordinate)))

        #Title Bar
        self.title_bar = Frame(self.root, bg='#212121', relief='raised', bd=0, height=20, width=600)
        self.close_button = Button(self.title_bar ,text='X', command=self.on_closing,   width=1, bg="#090909", fg="#888",activebackground='#ff453a',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
        self.add_button   = Button(self.title_bar ,text='+', command=self.changepage,   width=1, bg="#090909", fg="#888",activebackground='#ff9f0a',activeforeground='black', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
        self.minus_button = Button(self.title_bar ,text='_', command=self.root.destroy, width=1, bg="#090909", fg="#888",activebackground='#32d74b',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)


        self.btnState  = False 
        self.dark_img  = Image.open(self.srcPath + '/assets/dark-mode.png')
        self.dark_img  = self.dark_img.resize((37,20),Image.ANTIALIAS)
        self.dark_img  = ImageTk.PhotoImage(self.dark_img)

        self.light_img = Image.open(self.srcPath + '/assets/light-mode.png')
        self.light_img = self.light_img.resize((37,20),Image.ANTIALIAS)
        self.light_img = ImageTk.PhotoImage(self.light_img)

        self.mode = Button(self.title_bar,image= self.dark_img,command=self.mode_switch,bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
        self.mode.pack(side='left')

        self.title_bar.pack(side='top', fill=X)
        self.close_button.pack(side='right')
        self.add_button.pack(side='right')
        self.minus_button.pack(side='right')
        self.title_bar.bind('<B1-Motion>', self.move_window)

        self.offline_img = Image.open(self.srcPath + '/assets/red.png')
        self.offline_img = self.offline_img.resize((10,10),Image.ANTIALIAS)
        self.offline_img = ImageTk.PhotoImage(self.offline_img)

        self.online_img = Image.open(self.srcPath + '/assets/green.png')
        self.online_img = self.online_img.resize((10,10),Image.ANTIALIAS)
        self.online_img = ImageTk.PhotoImage(self.online_img)

        self.downloader_img = Image.open(self.srcPath + '/assets/downloader.png')
        self.downloader_img = self.downloader_img.resize((50,50),Image.ANTIALIAS)
        self.downloader_img = ImageTk.PhotoImage(self.downloader_img)

        self.fb_downloader_img = Image.open(self.srcPath + '/assets/fb_downloader.png')
        self.fb_downloader_img = self.fb_downloader_img.resize((50,50),Image.ANTIALIAS)
        self.fb_downloader_img = ImageTk.PhotoImage(self.fb_downloader_img)

        self.url_img  = Image.open(self.srcPath + '/assets/url.png')
        self.url_img  = self.url_img.resize((30,30),Image.ANTIALIAS)
        self.url_img  = ImageTk.PhotoImage(self.url_img)

        self.download_img = Image.open(self.srcPath + '/assets/download.png')
        self.download_img = self.download_img.resize((260,100),Image.ANTIALIAS)
        self.download_img = ImageTk.PhotoImage(self.download_img)

        self.fb_download_img = Image.open(self.srcPath + '/assets/fb_download.png')
        self.fb_download_img = self.fb_download_img.resize((260,100),Image.ANTIALIAS)
        self.fb_download_img = ImageTk.PhotoImage(self.fb_download_img)

        self.tuby(self.root)
        self.loading_img = ('dark-loading.gif')
        self.loading_gif = GifLabel(self.root,self.srcPath+'/assets/'+self.loading_img,100)

        self.per = StringVar()
        self.per.set('Please wait...')
        #self.loading_label= Label(self.root,textvariable = self.per,bg='white',fg='black') 
        self.loading_label= Label(self.root,text='please wait..',bg='black',fg='white') 
        self.copyright = Label(self.root, text="Cup ,\xa9 2020", bg= "red",fg="white"  )
        self.copyright.pack(side="bottom",fill=X)
        
        loaderThread = threading.Thread(target=self.loader)
        loaderThread.start()

        self.root.mainloop()

    def tuby(self,root):
        

        self.app = Frame(root,bg='#2c2c2c')
        self.app.pack(fill='both', expand=True)
        #multiproces = multiprocessing.Process(target=self.net_check)
        #multiproces.start()
        self.downloader_text = Label(self.app,text = 'uby Downloader',font=('Calibri',15,'bold'),bg='#2c2c2c',fg='white')
        self.downloader_text.place(x=65,y=45)

        self.downloader_label = Label(self.app,image = self.downloader_img,bg='#2c2c2c' )
        self.downloader_label.place(x=15,y=25)

        #Internet Check
        thread = threading.Thread(target= self.net_check)
        thread.start()
        

        self.url_label = Label(self.app,image = self.url_img,bg='#2c2c2c')
        self.url_label.place(x=30,y=140)

        self.url = Entry(self.app, width = 35,border=1, relief= SUNKEN , font = ('verdana',15))
        self.url.place(x=90,y=140)
        self.url.bind("<Button-1>", self.clear_entry)
        self.url.insert(0, 'Enter a Url')

        self.Download_label = Label(self.app,image = self.download_img,bg='#2c2c2c')
        self.Download_label.place(x=160,y=180)
        self.Download_label.bind('<Button-1>', self.validation)
        self.Download_label.bind('<Enter>', self.OnHover_Download)
        self.Download_label.bind('<Leave>', self.OnLeave_Download)

        self.download_text = Label(self.app,text = 'Download',font=('Helvetica',20,'bold','italic'),bg='#df0024',fg='white')
        self.download_text.place(x=200,y=218)
        self.download_text.bind('<Button-1>', self.validation)
        self.download_text.bind('<Enter>', self.OnHover_Download)

    def tuby_plus(self,root):
        self.under__construction
        self.app = Frame(self.root,bg='#2c2c2c')
        self.app.pack()
        Label(self.app, text = 'This feature will Introduced as soon as possible',font=('Helvetica',20,'bold','italic')).place(relx=0.5, rely=0.48, anchor=CENTER)#.pack(anchor=CENTER, fill=X, expand=YES)

    def mode_switch(self):
        #global btnState

        if self.btnState == True: #Dark Mode
            self.mode.config(image=self.dark_img, bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
            self.root['bg'] = ('#202020')
            self.title_bar.config(bg='#212121')
            self.close_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
            self.add_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
            self.minus_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
            self.app.config(bg='#2c2c2c')
            self.downloader_text.config(bg='#2c2c2c',fg='white')
            self.downloader_label.config(bg='#2c2c2c')
            self.url_label.config(bg='#2c2c2c')
            self.Download_label.config(bg='#2c2c2c')
            self.status_text.config(bg='#2c2c2c',fg='#f3f3f3')
            self.status.config(bg='#2c2c2c',fg='#f3f3f3')
            self.loading_img = ('dark-loading.gif')
            self.loading_gif = GifLabel(self.root,self.srcPath+'/assets/'+self.loading_img,100)
            self.btnState = False

        else : #Light Mode
            self.mode.config(image=self.light_img,bg='#cccccc',activebackground='#cccccc',bd=0,highlightcolor="#cccccc", highlightbackground="#cccccc", )
            self.root['bg']=('white')
            self.title_bar.config(bg='#cccccc')
            self.close_button.config(bg='#74777a',fg='black',activebackground='#bb0000', highlightcolor="#74777a", highlightbackground="#74777a")
            self.add_button.config(bg='#74777a',  fg='black',activebackground='#e9730c', highlightcolor="#74777a", highlightbackground="#74777a")
            self.minus_button.config(bg='#74777a',fg='black',activebackground="#107e3e", highlightcolor="#74777a", highlightbackground="#74777a")
            self.app.config(bg='#f3f3f3')
            self.downloader_text.config(bg='#f3f3f3',fg='black')
            self.downloader_label.config(bg='#f3f3f3')
            self.url_label.config(bg='#f3f3f3')
            self.Download_label.config(bg='#f3f3f3')
            self.status_text.config(bg='#f3f3f3',fg='#2c2c2c')
            self.status.config(bg='#f3f3f3',fg='#2c2c2c')
            self.loading_img = ('light-loading.gif')
            self.loading_gif = GifLabel(self.root,self.srcPath+'/assets/'+self.loading_img,100)
            self.btnState = True

    #Move Window
    def move_window(self,event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def changepage(self):
        
        self.app.pack_forget()
        if self.page_Num == 1:
            self.tuby_plus(self.root)
            self.page_Num = 2
        else:
            self.tuby(self.root)
            self.page_Num = 1
    
    def validation(self,event):
        
        self.url_link = self.url.get()
        try:
            validation = validate.offline_check(self.url_link)
        except NameError:
            validation = tuby.validate.offline_check(self.url_link)
        if (validation == ('ytvideo')):
            #self.downThread()
            self.download_thread = threading.Thread(target=self.yt_downloader)
            self.download_thread.start()
        elif(validation == ('ytplaylist')):
            print("It's a playlist")
        elif(validation == ('fbvideo')):
            self.copyright.config(bg = '3b5998')
            

    def net_check(self,*args): 
        
        self.status_text = Label(self.app, font = ('Courier 15 bold'),bg='#2c2c2c',fg='white')
        self.status_text.place(x = 27,y=267)
        self.status = Label(self.app,bg='#2c2c2c')
        self.status.place(x=10,y=270)
        while True:
            try:
                self.status_img = validate.check(self.online_img,self.offline_img)
            except NameError:
                self.status_img = tuby.validate.check(self.online_img,self.offline_img)
            self.status.config(image = self.status_img)
            self.off_or_on = StringVar()
            self.off_or_on.set('online') if self.status_img==self.online_img else self.off_or_on.set('offline') 
            self.status_text.config(textvariable = self.off_or_on,)

    def downThread(self):
        print('Hello World!!')
        self.download_thread = threading.Thread(target=self.yt_downloader)
        self.download_thread.start()
        
    
    def progress(self,chunk,file_handle,remaining):
        
        self.file_downloaded = int(file_size-remaining)
        per = (self.file_downloaded/file_size)*100
        self.loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)


    def fb_download_video(self,html,quality):
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

    def yt_downloader(self):
        global file_size
        #self.download_button.config(state=DISABLED)
        
        canvas.place(relx=0.5, rely=0.48, anchor=CENTER)#x=250,y=150)
        #canvas.config(anchor= CENTER)
        #canvas.pack(anchor=W, fill=X, expand=YES)
        self.loading_label.config(anchor = CENTER)
        self.loading_label.place(relx=0.5, rely=0.70, anchor=CENTER)
        #self.loading_label.pack(side=TOP, anchor=W, fill=X, expand=YES) #.place(x=230,y=250)
        self.app.pack_forget()
        #self.loading_gif.place(x=180,y=50)
        try:
            url1 = self.url.get()
            path = filedialog.askdirectory()
            yt   = YouTube(url1,on_progress_callback=self.progress)
            if os.path.isdir(path):
                video = yt.streams.filter(progressive=True,file_extension='mp4').first()
                file_size = video.filesize
                video.download (path)
                self.loading_label.config(text='Download Finish...' )
                self.loading_label.pack_forget()
                res = messagebox.askyesno("YouTube Video Downloader","Do youtube another video ?")
                if res == 1:
                    self.loading_label.config(text = 'Restarted' )
                    self.url.delete(0,END)
                    #self.download_button.config(state= NORMAL)
                    
                else:
                    self.on_closing()
            else:
                messagebox.showerror("error","no directory exist")
        except Exception as e :
            print(e)
            if(self.url.get()== ''):
                self.loading_label.config(text = 'Enter The URL')
                #self.download_button.config(state=NORMAL)
            else:
                self.loading_label.config(text = 'Failed! There is an error.')
                #elf.download_button.config(state=NORMAL)
        
    def clear_entry(self,*args):
        urlClip = pyperclip.paste()
        try:
            validation = validate.offline_check(urlClip)
        except:
            validation = tuby.validate.offline_check(urlClip)
        if(validation == ('ytvideo')):
            self.url.delete(0, END)
            self.url.insert(0, urlClip)
        elif(validation == 'fbvideo'):
            self.url.delete(0, END)
            self.url.insert(0, urlClip)
            self.download_text.config(bg='#3b5998')
            self.downloader_label.config(image=self.fb_downloader_img)
            self.Download_label.config(image=self.fb_download_img)
            self.copyright.config(bg = '#3b5998')
        else:
            self.url.delete(0, END)
    def loader(self,*args):
        global canvas
        canvas = Canvas(self.root,width=100,height = 90,background="black",highlightthickness=1, highlightbackground="black")
        #canvas.place(x=230,y=130)
        p = TurtleScreen(canvas)
        p.bgcolor('black')
        t = RawTurtle(p)
        t.speed(10)
        #t.title("Loader")
        #t.bgcolor("black")
        colors = ('red','grey')

        for a in range(360):
            t.pencolor(colors[a%2]) 
            t.pensize(5)
            t.circle(20)
            t.hideturtle()

    def OnPressed_Download(self,*args):
        #print('OnPressed_Download')
        self.app.pack_forget()
        self.loading_gif.place(x=180,y=50)
        

    def OnHover_Download(self,*args):
        #print('OnHover_Download')
        self.download_text.config(fg='#2c2c2c')


    def OnLeave_Download(self,*args):
        #print('OnLeave_Download')
        self.download_text.config(fg='#f3f3f3')

    def on_closing(self,*arg):
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #self.root.destroy()
        os._exit(0)
    def under__construction(self,*args):
        print('This feature is under construction')
if __name__ == "__main__":
    try:
        ui()
    except Exception as e:
        print(e)
