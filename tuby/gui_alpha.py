import os
import sys
import threading
import tkinter.ttk
import urllib
import webbrowser
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox
from turtle import *

import pyperclip
import requests
from PIL import Image, ImageTk
from pytube import YouTube
from tqdm import tqdm

try:
    #print('hello')
    import tuby.validate
    
except ModuleNotFoundError:
    import validate

try:
    #print('hello')
    import tuby.dengine
    
except ModuleNotFoundError:
    import dengine


file_size = 0
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__)) #os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 20
        y = y + cy + self.widget.winfo_rooty() + 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#2c2c2c", foreground='white' , relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


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


#Move Window
def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def OnPressed_Download(*args):
    #print('OnPressed_Download')
    app.pack_forget()
    loading_gif.place(x=180,y=50)
    
def OnHover_Download(*args):
    #print('OnHover_Download')
    download_text.config(fg='#2c2c2c')
def OnLeave_Download(*args):
    #print('OnLeave_Download')
    download_text.config(fg='#f3f3f3')

def on_closing(*arg):
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #root.destroy()
    os._exit(0)
def under__construction(*args):
    print('This feature is under construction')

def add_hyperlink(section, tag):
    # when you insert text, you can directly give it tags with 
    # text.insert(<index>, <text>, [tag1, tag2, ...])
    license_text.insert('end', section + '\n\n', ('link', tag))
    license_text.tag_bind(tag, '<Button-1>', lambda e: webbrowser.open(tag))

def about(*args):
    global license_text
    license_prompt = Toplevel()
    license_prompt.title('About')
    license_prompt.geometry('700x400')
    license_prompt.iconphoto(False,i_button_img)
    license_text = Text(license_prompt,background="#2c2c2c", foreground="#888")#justify = CENTER,)
    license_text.pack(fill='both', expand=True)
    license_text.tag_configure('link', foreground='cyan', underline=True)
    
    license_text.tag_config('justified', justify=CENTER)
    #license_text.tag_config("here", background="#2c2c2c", foreground="#888")  #.tag_add("center", 1.0, "end")
    f = open('LICENSE')
    license_lines = f.readlines()
    for line in license_lines:
        license_text.insert('end', line, 'justified')
    add_hyperlink('about', 'https://gpstudiolaboftech.github.io/')
    license_text['state'] = DISABLED
    f.close()
    #webbrowser.open("https://gpstudiolaboftech.github.io/")

def changepage():
    global page_Num
    app.pack_forget()

    if page_Num == 1:
        tuby_plus(root)
        page_Num = 2

    else:

        tuby_normal(root)
        page_Num = 1

def validation(event):
    url_link = url.get()
    try:
        validation = validate.offline_check(url_link)
    except NameError:
        validation = tuby.validate.offline_check(url_link)
    if (validation == ('ytvideo')):
        #downThread()
        download_thread = threading.Thread(target=yt_downloader)
        download_thread.start()
    elif(validation == ('ytplaylist')):
        print("It's a playlist")
    
    elif(validation == ('fbvideo')):
        fb_resolution(url_link)
        print('hello world!!')
        #copyright.config(bg = '3b5998')
    
        
def net_check(*args): 
    global status_text , status
    status_text = Label(app, font = ('Courier 15 bold'),bg='#2c2c2c',fg='white')
    status_text.place(x = 27,y=267)
    status = Label(app,bg='#2c2c2c')
    status.place(x=10,y=270)
    while True:
        try:
            status_img = validate.check(online_img,offline_img)
        except NameError:
            status_img = tuby.validate.check(online_img,offline_img)
        status.config(image = status_img)
        off_or_on = StringVar()
        off_or_on.set('online') if status_img==online_img else off_or_on.set('offline') 
        status_text.config(textvariable = off_or_on,)

def downThread():
    print('Hello World!!')
    download_thread = threading.Thread(target= dengine.yt_downloader)
    download_thread.start()

def yt_color_code(*args):
    download_text.config(bg='#df0024')
    downloader_label.config(image=downloader_img)
    Download_label.config(image=download_img)
    copyright.config(bg = '#df0024')

def fb_color_code(*args):
    download_text.config(bg='#3b5998')
    downloader_label.config(image=fb_downloader_img)
    Download_label.config(image=fb_download_img)
    copyright.config(bg = '#3b5998')

def tuby_normal(root):
    global app , page_Num , downloader_text , downloader_label , i_icon , url_label  , url , Download_label ,download_text
    page_Num = 1
    app = Frame(root,bg='#2c2c2c')
    #app.place(relx=0, rely=0, anchor=CENTER,)
    app.pack(fill='both', expand=True)
    downloader_text = Label(app,text = 'uby Downloader',font=('Calibri',15,'bold'),bg='#2c2c2c',fg='white')
    downloader_text.place(x=65,y=45)

    #downloader_text.place(relx=-10, rely=-10, anchor=CENTER,)
    downloader_label = Label(app,image = downloader_img,bg='#2c2c2c' )
    downloader_label.place(x=15,y=25)
    #Internet Check
    thread = threading.Thread(target= net_check)
    thread.start()
    
    i_icon = Label(app,image = i_button_img,bg='#2c2c2c')
    i_icon.place(x=555,y=10)
    i_icon.bind('<Button-1>',about)
    CreateToolTip(i_icon,text='info')
    url_label = Label(app,image = url_img,bg='#2c2c2c')
    url_label.place(x=30,y=140)
    url = Entry(app, width = 35,border=1, relief= SUNKEN , font = ('verdana',15))
    url.place(x=90,y=140)
    url.bind("<Button-1>", clear_entry)
    url.insert(0, 'Enter a Url')
    Download_label = Label(app,image = download_img,bg='#2c2c2c')
    Download_label.place(x=160,y=180)
    Download_label.bind('<Button-1>', validation)
    Download_label.bind('<Enter>', OnHover_Download)
    Download_label.bind('<Leave>', OnLeave_Download)
    download_text = Label(app,text = 'Download',font=('Helvetica',20,'bold','italic'),bg='#df0024',fg='white')
    download_text.place(x=200,y=218)
    download_text.bind('<Button-1>', validation)
    download_text.bind('<Enter>', OnHover_Download)

def tuby_plus(root):
    global app
    app = Frame(root,bg='#2c2c2c')
    app.pack(fill='both', expand=True)
    coming_soon = Label(app, text = 'This feature will Introduced as soon as possible',font=('Helvetica',15,'bold'),bg='#2c2c2c',fg='white')
    coming_soon.pack(anchor=CENTER, fill=X, expand=YES) #.place(relx=0.5, rely=0.48, anchor=CENTER)#\


def mode_switch():
    global btnState
    if btnState == True: #Dark Mode
        mode.config(image=dark_img, bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
        root['bg'] = ('#202020')
        title_bar.config(bg='#212121')
        close_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        add_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        minus_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        app.config(bg='#2c2c2c')
        i_icon.config(bg='#2c2c2c')
        downloader_text.config(bg='#2c2c2c',fg='white')
        downloader_label.config(bg='#2c2c2c')
        url_label.config(bg='#2c2c2c')
        Download_label.config(bg='#2c2c2c')
        status_text.config(bg='#2c2c2c',fg='#f3f3f3')
        status.config(bg='#2c2c2c',fg='#f3f3f3')
        loading_img = ('dark-loading.gif')
        btnState = False
    else : #Light Mode
        mode.config(image=light_img,bg='#cccccc',activebackground='#cccccc',bd=0,highlightcolor="#cccccc", highlightbackground="#cccccc", )
        root['bg']=('white')
        title_bar.config(bg='#cccccc')
        close_button.config(bg='#74777a',fg='black',activebackground='#bb0000', highlightcolor="#74777a", highlightbackground="#74777a")
        add_button.config(bg='#74777a',  fg='black',activebackground='#e9730c', highlightcolor="#74777a", highlightbackground="#74777a")
        minus_button.config(bg='#74777a',fg='black',activebackground="#107e3e", highlightcolor="#74777a", highlightbackground="#74777a")
        app.config(bg='#f3f3f3')
        i_icon.config(bg = '#f3f3f3')
        downloader_text.config(bg='#f3f3f3',fg='black')
        downloader_label.config(bg='#f3f3f3')
        url_label.config(bg='#f3f3f3')
        Download_label.config(bg='#f3f3f3')
        status_text.config(bg='#f3f3f3',fg='#2c2c2c')
        status.config(bg='#f3f3f3',fg='#2c2c2c')
        loading_img = ('light-loading.gif')
        loading_gif = GifLabel(root,srcPath+'/assets/'+loading_img,100)
        btnState = True

def progress(chunk,file_handle,remaining):
    
    file_downloaded = int(file_size-remaining)
    per = (file_downloaded/file_size)*100
    loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)
    #display_progress_bar(file_downloaded, file_size)
    #while per<100:
    #t.update(round(per))


def yt_downloader():
    global file_size
       
    canvas.place(relx=0.5, rely=0.48, anchor=CENTER)#x=250,y=150)
    loading_label.config(anchor = CENTERtuby_plus)
    loading_label.place(relx=0.5, rely=0.70, anchor=CENTER)
    app.pack_forget()
    
    try:
        url1 = url.get()
        path = filedialog.askdirectory()
        yt   = YouTube(url1,on_progress_callback=progress)# and on_progress)
        if os.path.isdir(path):

            video = yt.streams.filter(progressive=True,file_extension='mp4').first()
            
            file_size = video.filesize
            
            #t = tqdm(total=100 )#unit='B', unit_scale=True, ascii=True)
            
            video.download (path)
            loading_label.config(text='Download Finish...' )
            loading_label.pack_forget()
            res = messagebox.askyesno("YouTube Video Downloader","Do youtube another video ?")
            if res == 1:
                loading_label.config(text = 'Restarted' )
                url.delete(0,END)
                #download_button.config(state= NORMAL)
                
            else:
                on_closing()
        else:
            messagebox.showerror("error","no directory exist")
    except Exception as e :
        print(e)
#    except Exception :
#        #print(e)
#        if(url.get()== ''):
#            loading_label.config(text = 'Enter The URL')
#            #download_button.config(state=NORMAL)
#        else:
#            loading_label.config(text = 'Failed! There is an error.')
#

def fb_download():
    
    """Download the video in HD or SD qtuby_plusality"""
    canvas.place(relx=0.5, rely=0.48, anchor=CENTER)#x=250,y=150)
    loading_label.config(anchor = CENTER)
    loading_label.place(relx=0.5, rely=0.70, anchor=CENTER)
    app.pack_forget()
    
    

    html = requests.get(fb_url_link).content.decode('utf-8')
    print(f"\nDownloading the video in {quality} quality... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    path = filedialog.askdirectory()
    fb_filename = datetime.strftime(datetime.now(), path +'/%Y-%m-%d-%H-%M-%S')
    print(file_size)
    progress = tkinter.ttk.Progressbar(root, orient = HORIZONTAL, length = 800,maximum = 100, mode = 'determinate') 
    progress.place(relx=0.5, rely=0.48, anchor=CENTER)
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=fb_filename, ascii=True)
    file_downloaded = 0
    with open(fb_filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            #print(len(data))
            file_downloaded += 1024
            per = (file_downloaded/file_size)*100
            loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)
            progress['value'] = per 
            block_size +=block_size
            root.update_idletasks() 
            #per = (len(data)/file_size)*100

            #loading_label.config('{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)
            
            f.write(data)
    t.close()

    print("\nVideo downloaded successfully.")

def clear_entry(*args):
    urlClip = pyperclip.paste()
    try:
        validation = validate.offline_check(urlClip)
    except:
        validation = tuby.validate.offline_check(urlClip)
    if(validation == ('ytvideo')):
        url.delete(0, END)
        url.insert(0, urlClip)
        yt_color_code()

    elif(validation == 'fbvideo'):
        url.delete(0, END)
        url.insert(0, urlClip)
        fb_color_code()

    else:
        url.delete(0, END)

def loader(*args):
    global canvas
    canvas = Canvas(root,width=100,height = 90,background="black",highlightthickness=1, highlightbackground="black")
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


def structure():
    global page_Num , srcPath , root , title_bar , close_button , add_button , minus_button , btnState , dark_img , light_img , mode , offline_img , online_img ,  downloader_img , fb_downloader_img , url_img , download_img , fb_download_img , loading_img , loading_gif , per , loading_label , i_button_img , copyright , loaderThread #download_imgdark_img,root,add_button,copyright,close_button,btnState,mode,title_bar

    os. system('clear') 
    print("Welcome to Tuby Downloader")
    #print(pyfiglet.figlet_format("Tuby", font = "slant"  ) )
    
    banner = (r'''
      ______      __         
     /_  __/_  __/ /_  __  __
      / / / / / / __ \/ / / /
     / / / /_/ / /_/ / /_/ / 
    /_/  \__,_/_.___/\__, /  
                    /____/  
    ''')

    print(banner)
    print("Copyright (c) 2020 guruprasadh_j")
    
    page_Num = 1
    srcPath = os.path.dirname(os.path.abspath(__file__))
    root = Tk(className='Tuby 1')
    root.protocol("WM_DELETE_WINDOW", on_closing)
    #root.overrideredirect(True)
    #root.wm_attributes('-type', 'splash')
    #root.update_idletasks()
    iconres = resource_path(srcPath+"/assets/favicon.png")
    icon = PhotoImage(file = (iconres))
    root.iconphoto(False, icon)
    root.title('Tuby (3.8.5)')
    root['bg'] = ('black') #202020
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2) - (600/2)
    y_coordinate = (screen_height/2) - (350/2)
    root.geometry("{}x{}+{}+{}".format(600, 350, int(x_coordinate), int(y_coordinate)))
    
########################################################################################
    #Title Bar
    title_bar = Frame(root, bg='#212121', relief='raised', bd=0, height=20, width=600)
    close_button = Button(title_bar ,text='X', command=on_closing,   width=1, bg="#090909", fg="#888",activebackground='#ff453a',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    add_button   = Button(title_bar ,text='+', command=changepage,   width=1, bg="#090909", fg="#888",activebackground='#ff9f0a',activeforeground='black', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    minus_button = Button(title_bar ,text='_', command=root.destroy, width=1, bg="#090909", fg="#888",activebackground='#32d74b',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    btnState  = False 
    
    dark_img_res =resource_path(srcPath + '/assets/dark-mode.png')
    dark_img  = Image.open(dark_img_res)
    dark_img  = dark_img.resize((37,20),Image.ANTIALIAS)
    dark_img  = ImageTk.PhotoImage(dark_img)
    
    light_img_res = resource_path(srcPath + '/assets/light-mode.png') 
    light_img = Image.open(light_img_res)
    light_img = light_img.resize((37,20),Image.ANTIALIAS)
    light_img = ImageTk.PhotoImage(light_img)
    mode = Button(title_bar,image= dark_img,command=mode_switch,bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
    mode.pack(side='left')
    title_bar.pack(side='top', fill=X)
    close_button.pack(side='right')
    add_button.pack(side='right')
    minus_button.pack(side='right')
    title_bar.bind('<B1-Motion>', move_window)

############################################################################################

    #Collection Images

    offline_img_res = resource_path(srcPath + '/assets/red.png')
    offline_img = Image.open(offline_img_res)
    offline_img = offline_img.resize((10,10),Image.ANTIALIAS)
    offline_img = ImageTk.PhotoImage(offline_img)

    online_img_res = resource_path(srcPath + '/assets/green.png')
    online_img = Image.open(online_img_res)
    online_img = online_img.resize((10,10),Image.ANTIALIAS)
    online_img = ImageTk.PhotoImage(online_img)

    downloader_img_res = resource_path(srcPath + '/assets/downloader.png')
    downloader_img = Image.open(downloader_img_res)
    downloader_img = downloader_img.resize((50,50),Image.ANTIALIAS)
    downloader_img = ImageTk.PhotoImage(downloader_img)

    fb_downloader_img_res = resource_path(srcPath + '/assets/fb_downloader.png')
    fb_downloader_img = Image.open(fb_downloader_img_res)
    fb_downloader_img = fb_downloader_img.resize((50,50),Image.ANTIALIAS)
    fb_downloader_img = ImageTk.PhotoImage(fb_downloader_img)

    url_img_res = resource_path(srcPath + '/assets/url.png')
    url_img  = Image.open(url_img_res)
    url_img  = url_img.resize((30,30),Image.ANTIALIAS)
    url_img  = ImageTk.PhotoImage(url_img)

    download_img_res = resource_path(srcPath + '/assets/download.png')
    download_img = Image.open(download_img_res)
    download_img = download_img.resize((260,100),Image.ANTIALIAS)
    download_img = ImageTk.PhotoImage(download_img)

    fb_download_img_res = resource_path(srcPath + '/assets/fb_download.png')
    fb_download_img = Image.open(fb_download_img_res)
    fb_download_img = fb_download_img.resize((260,100),Image.ANTIALIAS)
    fb_download_img = ImageTk.PhotoImage(fb_download_img)

    i_button_img_res = resource_path(srcPath + '/assets/i.png')
    i_button_img = Image.open(i_button_img_res)
    i_button_img = i_button_img.resize((25,25),Image.ANTIALIAS)
    i_button_img = ImageTk.PhotoImage(i_button_img)

    tuby_plus(root)
    loading_img_res = resource_path(srcPath + '/assets/dark-loading.gif')
    loading_gif = GifLabel(root,loading_img_res,100)
    
##############################################################################################
    
    loading_label= Label(root,text='please wait..',bg='black',fg='white') 
    copyright = Label(root, text="Cup ,\xa9 2020", bg= "red",fg="white" )
    copyright.pack(side="bottom",fill=X)
    
    loaderThread = threading.Thread(target=loader)
    loaderThread.start()
    root.mainloop()



def fb_resolution(url_link):
    global fb_url_link,quality
    print(url_link)
    fb_url_link = str(url_link)
    fb_list = validate.fb_get_data(url_link)
    print(fb_list)
    if len(fb_list) == 2:
        if 0 in fb_list and 1 in fb_list:
            quality = ("HD")
            fb_thread = threading.Thread( target= fb_download )
            fb_thread.start()

        elif 1 in fb_list and 2 in fb_list:
            quality = ("SD")
            fb_thread = threading.Thread( target= fb_download )
            fb_thread.start()
        elif 0 in fb_list and 3 in fb_list:
            quality = ("HD")
            fb_thread = threading.Thread( target= fb_download )
            fb_thread.start()




if __name__ == "__main__":

    try:
        structure()

    except KeyboardInterrupt:
        print('\n Youn have Force Stoped the application')
        on_closing()
