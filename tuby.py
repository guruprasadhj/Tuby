import PIL._tkinter_finder
from tkinter import*
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
from pytube import YouTube
from threading import *
import webbrowser,os,pyperclip

from keybind import KeyBinder


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def on_closing(*arg):
    global thread
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        
        root.destroy()
        os._exit(0)
        #return
        #thread.exit() 

       
    

file_size = 0
def downThread():
    #global thread
    #down=downloader()
    thread =Thread(target=downloader)
    thread.start()

def progress(chunk,file_handle,remaining):
    global download_status 
    file_downloaded = file_size-remaining
    per = (file_downloaded/file_size)*100
    download_status.config(text='{:00.0f} % downloaded'.format(per))

def downloader():
    global file_size, download_status
    download_button.config(state=DISABLED)
    download_status.pack(side="bottom",fill=X) #.place(x=230,y=250)

    try:
        url1 = url.get()
        path = filedialog.askdirectory()
        yt   = YouTube(url1,on_progress_callback=progress)
        if os.path.isdir(path):
            video = yt.streams.filter(progressive=True,file_extension='mp4').first()
            file_size = video.filesize
            video.download (path)
            download_status.config(text = 'Download Finish...' )
            res = messagebox.askyesno("Youtubr Video Downloader","Do youtube another video ?")
        
            if res == 1:
                download_status.config(text = 'Restarted' )
                url.delete(0,END)
                download_button.config(state= NORMAL)
                
            else:
                root.destroy()
        else:
            messagebox.showerror("error","no directory exist")
            
            
    except Exception :
        if(url.get()== ''):
            download_status.config(text = 'Enter The URL')
            download_button.config(state=NORMAL)
        else:
            download_status.config(text = 'Failed! There is an error.')
            download_button.config(state=NORMAL)

def paste(event):
    urlClip = pyperclip.paste()
    url.insert(0, urlClip)

def quit(event):
    print ("you pressed control c")
    #root.destroy()
    os._exit(0)

def about():
    webbrowser.open("https://gpstudiolaboftech.github.io/")
    
urlClip = pyperclip.paste()
YouTubeURL = 'https://www.youtube.com/watch?v='
#print(urlClip)
def check(urlClip, YouTubeURL): 
    if (urlClip.find(YouTubeURL) == -1): 
        print('Paste A Link')
    else: 
        url.insert(0, urlClip)




root= Tk(className='Tuby')
root.geometry('600x350')
iconres= resource_path("ytlogo.png")
icon = PhotoImage(file = iconres)
root.iconphoto(False, icon)
#root.iconbitmap('ytlogo.png')
root.title("Tuby an YouTube video dowmloader  (3.5.7)")
root.protocol("WM_DELETE_WINDOW", on_closing)
root['bg'] = 'black'
root.resizable(0,0)
imgres=resource_path("ytlogo.png")
img  = Image.open(imgres)
img  = img.resize((80,80),Image.ANTIALIAS)
img  = ImageTk.PhotoImage(img)
head = Label(root,image=img,bg='black',fg='white')
head.config(anchor = CENTER)
head.pack()

about = Button(text = "i",bg='black',fg='white',font = ('Courier 15 bold'), command = about,activebackground='red')
about.place(x="560",y="0")

enter_url = Label(root,text = 'Enter URL:\n(ctrl+v)',bg='black',fg='white')
enter_url.config(font = ('verdana',15))
enter_url.place(x=5,y=125)

url = Entry(root, width = 35,border=1, relief= SUNKEN , font = ('verdana',15))
url.place(x=125,y=125)
check(urlClip,YouTubeURL)

download_button_img_res = resource_path("download.png")
download_button_img = Image.open(download_button_img_res)
download_button_img = download_button_img.resize((150,50),Image.ANTIALIAS)
download_button_img = ImageTk.PhotoImage(download_button_img)
download_button = Button(root, width=160,height=45,bg='black',relief='raised',activebackground='red', command = downThread)
download_button.config(image = download_button_img )
download_button.place(x=220,y=200)
download_status = Label(root,text = 'Please wait..',font=('verdana bold',15),bg='black',fg='white')
copyright = Label(root, text="Gp Studio,\xa9 2020", bg= "red",fg="white"  )
copyright.pack(side="bottom",fill=X)



root.bind('<Control-c>', quit) 
root.bind('<Control-v>', paste)

root.mainloop()
