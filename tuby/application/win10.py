module_error = False
import PIL._tkinter_finder
import time
start_time = time.time()
import os
print(" [   OK   ] - Started OS module successfully imported \n  ")
import sys
print(" [   OK   ] - Started SYS module successfully imported \n  ")
import threading
print(" [   OK   ] - Started threading module successfully imported \n  ")
import tkinter.ttk
print(" [   OK   ] - Started tkinter.ttk module successfully imported \n  ")
import webbrowser
print(" [   OK   ] - Started webbrowser module successfully imported \n  ")
from datetime import datetime
print(" [   OK   ] - Started datetime module successfully imported \n  ")
from tkinter import *
from tkinter import filedialog, messagebox
print(" [   OK   ] - Started tkinter module successfully imported \n  ")
from turtle import *
print(" [   OK   ] - Started turtle module successfully imported \n  ")

print("Inbuilt Module imported Successfully ")
try:
    import pyperclip
except ModuleNotFoundError:
    print(" [ Error! ] - pyperclip module is not Installed ")

try:
    import requests
    print(" [   OK   ] - Started request module successfully imported \n   ")
except ModuleNotFoundError:
    print(" [ Error! ] - request module is not Installed ")

try:
    from PIL import Image, ImageTk
    print(" [   OK   ] - Started pillow module successfully imported \n  ")
except ModuleNotFoundError:
    print(" [ Error! ] - pillow module is not Installed ")

try:
    from pytube import YouTube
    print(" [   OK   ] - Started pytube module successfully imported \n  ")
except ModuleNotFoundError:
    print(" [ Error! ] - pytube module is not Installed ")

try:
    from tqdm import tqdm
    print(" [   OK   ] - Started tqdm module successfully imported \n  ")
except ModuleNotFoundError:
    print(" [ Error! ] - tqdm is not Installed ")



try:
    import tuby.validate
except ModuleNotFoundError:
    import validate


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


banner = (r'''
      ______      __         
     /_  __/_  __/ /_  __  __
      / / / / / / __ \/ / / /
     / / / /_/ / /_/ / /_/ / 
    /_/  \__,_/_.___/\__, /  
                    /____/  
                   Speed Matters :-)
    ''')

#########################################################################################################################
def print_slow(str):
        for char in str:
            time.sleep(.05)
            sys.stdout.write(char)
            sys.stdout.flush()

if module_error:
    
    print_slow('Module error Found !!')

else:
    #print_slow("All modules are installed Successfully ")
#    os.system('clear')
#    print("Welcome to Tuby Downloader")
#    print(banner)
#    print("Copyright (c) 2020 guruprasadh_j")
#    print("--- %s seconds ---" % (time.time() - start_time))
    page_Num = 1
    srcPath = os.path.dirname(os.path.abspath(__file__))

##########################################################################################################################
# For Py Installer
def resource_path(relative_path):
    #This Secource Path is for converterting .py to .exe or .appimage
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__)) #os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

########################################################################################################################
#COLOUR CODE

#Youtube Color code
def yt_color_code(*args):
    download_text.config(bg='#df0024')
    downloader_label.config(image=downloader_img)
    Download_label.config(image=download_img)
    copyright.config(bg = '#df0024')

#FaceBook Color Code
def fb_color_code(*args):
    download_text.config(bg='#3b5998')
    downloader_label.config(image=fb_downloader_img)
    Download_label.config(image=fb_download_img)
    copyright.config(bg = '#3b5998')

#Dark or Light Mode
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
        btnState = True

#Change Frame
def changepage():
    global page_Num
    app.pack_forget()

    if page_Num == 1:
        tuby_plus(root)
        page_Num = 2

    else:

        tuby_regular(root)
        page_Num = 1

#########################################################################################################################
# MINI TASK
#On Closing
def on_closing(*arg):
    os._exit(0)

#Move Windows
def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

#Download Button
def OnHover_Download(*args):
    download_text.config(fg='#2c2c2c')
def OnLeave_Download(*args):
    download_text.config(fg='#f3f3f3')

#Clear Entry Box and validation
def clear_entry(*args):
    urlClip = pyperclip.paste()
    validation = offline_check(urlClip)
    
    
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

#Validation
def validation(event):
    url_link = url.get()
    validation = offline_check(url_link)
    

    if (validation == ('ytvideo')):
        download_thread = threading.Thread(target=yt_downloader)
        download_thread.start()

    elif(validation == ('ytplaylist')):
        print("It's a playlist")
    
    elif(validation == ('fbvideo')):
        fb_resolution(url_link)
        
        
# Loader 
def loader(*args):
    global canvas , colors
    canvas = Canvas(root,width=100,height = 90,background="black",highlightthickness=1, highlightbackground="black")
    p = TurtleScreen(canvas)
    p.bgcolor('black')
    t = RawTurtle(p)
    t.speed(10)
    colors = ('red','grey')
    for a in range(360):
        t.pencolor(colors[a%2]) 
        t.pensize(5)
        t.circle(20)
        t.hideturtle()

def about(*args):
    license_prompt = Toplevel()
    license_prompt.title('About')
    license_prompt.geometry('700x400')
    license_prompt.iconphoto(False,i_button_img)
    license_text = Text(license_prompt,background="#2c2c2c", foreground="#888")#justify = CENTER,)
    license_text.pack(fill='both', expand=True)
    license_text.tag_config('justified', justify=CENTER)
    #license_text.tag_config("here", background="#2c2c2c", foreground="#888")  #.tag_add("center", 1.0, "end")
    f = open('assets/LICENSE')
    license_lines = f.readlines()
    for line in license_lines:
        license_text.insert('end', line, 'justified')
    license_text['state'] = DISABLED
    f.close()
    #webbrowser.open("https://gpstudiolaboftech.github.io/")

#########################################################################################################################

def progress(chunk,file_handle,remaining):
    file_downloaded = int(file_size-remaining)
    per = (file_downloaded/file_size)*100
    loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)

def yt_downloader():
    global file_size
    
    canvas.place(relx=0.5, rely=0.48, anchor=CENTER)
    loading_label.config(anchor = CENTER)
    loading_label.place(relx=0.5, rely=0.70, anchor=CENTER)
    app.pack_forget()
    
#    try:
    url1 = url.get()
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
            
        else:
            on_closing()
    else:
        messagebox.showerror("error","no directory exist")
#    except Exception as e :
#        print(e)
#        if(url.get()== ''):
#            loading_label.config(text = 'Enter The URL')
#            
#        else:
#            loading_label.config(text = 'Failed! There is an error.')

def fb_resolution(url_link):
    global fb_url_link,quality
    print(url_link)
    fb_url_link = str(url_link)
    fb_list = fb_get_data(url_link)
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

def fb_download():
    
    canvas.place(relx=0.5, rely=0.48, anchor=CENTER)
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
    fb_filename = datetime.strftime(datetime.now(), path +'%Y-%m-%d-%H-%M-%S')
    print(file_size)
    progress = tkinter.ttk.Progressbar(root, orient = HORIZONTAL, length = 800,maximum = 100, mode = 'determinate') 
    progress.place(relx=0.5, rely=0.48, anchor=CENTER)
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=fb_filename, ascii=True)
    file_downloaded = 0
    
    with open(fb_filename + '.mp4', 'wb') as f:
        
        for data in file_size_request.iter_content(block_size):
            
            t.update(len(data))
            file_downloaded += 1024
            per = (file_downloaded/file_size)*100
            loading_label.config(text='{:00.0f} % downloaded'.format(per),font=('Helvetica',20,'bold','italic'),)
            progress['value'] = per 
            block_size +=block_size
            root.update_idletasks()            
            f.write(data)

    t.close()

    print("\nVideo downloaded successfully.")

#########################################################################################################################
#Internet Check
def net_check(*args): 
    global status_text , status
    status_text = Label(app, font = ('Courier 15 bold'),bg='#2c2c2c',fg='white')
    status_text.place(x = 27,y=267)
    status = Label(app,bg='#2c2c2c')
    status.place(x=10,y=270)
    while True:
        try:
            status_img = check(online_img,offline_img)
        except NameError:
            status_img = check(online_img,offline_img)
        status.config(image = status_img)
        off_or_on = StringVar()
        off_or_on.set('online') if status_img==online_img else off_or_on.set('offline') 
        status_text.config(textvariable = off_or_on,)

# Regular GUi
def tuby_regular(root):
    global app , page_Num , downloader_text , downloader_label , i_icon , url_label  , url , Download_label ,download_text
    
    page_Num = 1
    app = Frame(root,bg='#2c2c2c')
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
    i_icon.place(x=560,y=10)
    i_icon.bind('<Button-1>',about)
    url_label = Label(app,image = url_img,bg='#2c2c2c')
    url_label.place(x=30,y=140)
    url = Entry(app, width = 35,border=1, relief= SUNKEN , font = ('verdana',15))
    url.place(x=90,y=140)
    url.bind("<Button-1>", clear_entry)
    url.insert(0, 'Enter a Url')
    Download_label = Label(app,image = download_img,bg='#2c2c2c')
    Download_label.place(x=160,y=185)
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
    coming_soon.pack(anchor=CENTER, fill=X, expand=YES)


def structure():
    global page_Num , srcPath , root , title_bar , close_button , add_button , minus_button , btnState , dark_img , light_img , mode , offline_img , online_img ,  downloader_img , fb_downloader_img , url_img , download_img , fb_download_img , loading_gif , loading_label , i_button_img , copyright , loaderThread 

    root = Tk(className='Tuby')
    root.protocol("WM_DELETE_WINDOW", on_closing)
    #root.overrideredirect(True)
    iconres = resource_path("assets/favicon.png")
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
    close_button = Button(title_bar ,text='X', command=on_closing,   width=3, bg="#090909", fg="#888",activebackground='#ff453a',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    add_button   = Button(title_bar ,text='+', command=changepage,   width=3, bg="#090909", fg="#888",activebackground='#ff9f0a',activeforeground='black', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    minus_button = Button(title_bar ,text='_', command=root.destroy, width=3, bg="#090909", fg="#888",activebackground='#32d74b',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    btnState  = False 
    
    dark_img_res =resource_path('assets/dark-mode.png')
    dark_img  = Image.open(dark_img_res)
    dark_img  = dark_img.resize((37,20),Image.ANTIALIAS)
    dark_img  = ImageTk.PhotoImage(dark_img)
    
    light_img_res = resource_path('assets/light-mode.png') 
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

    offline_img_res = resource_path('assets/red.png')
    offline_img = Image.open(offline_img_res)
    offline_img = offline_img.resize((10,10),Image.ANTIALIAS)
    offline_img = ImageTk.PhotoImage(offline_img)

    online_img_res = resource_path('assets/green.png')
    online_img = Image.open(online_img_res)
    online_img = online_img.resize((10,10),Image.ANTIALIAS)
    online_img = ImageTk.PhotoImage(online_img)

    downloader_img_res = resource_path('assets/downloader.png')
    downloader_img = Image.open(downloader_img_res)
    downloader_img = downloader_img.resize((50,50),Image.ANTIALIAS)
    downloader_img = ImageTk.PhotoImage(downloader_img)

    fb_downloader_img_res = resource_path('assets/fb_downloader.png')
    fb_downloader_img = Image.open(fb_downloader_img_res)
    fb_downloader_img = fb_downloader_img.resize((50,50),Image.ANTIALIAS)
    fb_downloader_img = ImageTk.PhotoImage(fb_downloader_img)

    url_img_res = resource_path('assets/url.png')
    url_img  = Image.open(url_img_res)
    url_img  = url_img.resize((30,30),Image.ANTIALIAS)
    url_img  = ImageTk.PhotoImage(url_img)

    download_img_res = resource_path('assets/download.png')
    download_img = Image.open(download_img_res)
    download_img = download_img.resize((260,100),Image.ANTIALIAS)
    download_img = ImageTk.PhotoImage(download_img)

    fb_download_img_res = resource_path('assets/fb_download.png')
    fb_download_img = Image.open(fb_download_img_res)
    fb_download_img = fb_download_img.resize((260,100),Image.ANTIALIAS)
    fb_download_img = ImageTk.PhotoImage(fb_download_img)

    i_button_img_res = resource_path('assets/i.png')
    i_button_img = Image.open(i_button_img_res)
    i_button_img = i_button_img.resize((25,25),Image.ANTIALIAS)
    i_button_img = ImageTk.PhotoImage(i_button_img)

    tuby_regular(root)
    
    ##############################################################################################
    
    loading_label= Label(root,text='please wait..',bg='black',fg='white') 
    copyright = Label(root, text="Cup ,\xa9 2020", bg= "red",fg="white" )
    copyright.pack(side="bottom",fill=X)
    
    loaderThread = threading.Thread(target=loader)
    loaderThread.start()
    root.mainloop()




if __name__ == "__main__":
    os.system('clear')
    print("Welcome to Tuby Downloader")
    print(banner)
    print("Copyright (c) 2020 guruprasadh_j")
    print("--- %s seconds ---" % (time.time() - start_time))
    structure()
