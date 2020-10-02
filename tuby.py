import PIL._tkinter_finder
from tkinter import*
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
from pytube import YouTube
from threading import *
import webbrowser,os,pyperclip,sys



file_size = 0    
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
        return os.path.join(base_path, relative_path)

urlClip = pyperclip.paste()
YouTubeURL = 'https://www.youtube.com/watch?v='
#print(urlClip)

def check(urlClip, YouTubeURL):
    if (urlClip.find(YouTubeURL) == -1): 
        print('Paste A Link')
    else:
        print('Hello')
    #url.insert(0, urlClip)

class tuby():
    def __init__(self):
        self.root= Tk(className='Tuby')
        self.root.geometry('600x350')
        iconres= resource_path("Image/ytlogo.png")
        icon = PhotoImage(file = iconres)
        self.root.iconphoto(False, icon)
        self.root.title("Tuby an YouTube video dowmloader  (3.5.7)")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root['bg'] = 'black'
        self.root.resizable(0,0)
        imgres=resource_path("Image/ytlogo.png")
        img  = Image.open(imgres)
        img  = img.resize((80,80),Image.ANTIALIAS)
        img  = ImageTk.PhotoImage(img)
        self.head = Label(self.root,image=img,bg='black',fg='white')
        self.head.config(anchor = CENTER)
        self.head.pack()

        self.about = Button(text = "i",bg='black',fg='white',font = ('Courier 15 bold'), command = webbrowser.open("https://gpstudiolaboftech.github.io/"),activebackground='red')
        self.about.place(x="560",y="0")

        self.enter_url = Label(self.root,text = 'Enter URL:\n(ctrl+v)',bg='black',fg='white')
        self.enter_url.config(font = ('verdana',15))
        self.enter_url.place(x=5,y=125)

        self.url = Entry(self.root, width = 35,border=1, relief= SUNKEN , font = ('verdana',15))
        self.url.place(x=125,y=125)
        check(urlClip,YouTubeURL)

        download_button_img_res = resource_path("Image/download.png")
        download_button_img = Image.open(download_button_img_res)
        download_button_img = download_button_img.resize((150,50),Image.ANTIALIAS)
        download_button_img = ImageTk.PhotoImage(download_button_img)
        self.download_button = Button(self.root, width=160,height=45,bg='black',relief='raised',activebackground='red', command = self.downThread)
        self.download_button.config(image = download_button_img )
        self.download_button.place(x=220,y=200)
        self.download_status = Label(self.root, text = 'Please wait..',font=('verdana bold',15),bg='black',fg='white')
        self.copyright = Label(self.root, text="Gp Studio,\xa9 2020", bg= "red",fg="white"  )
        self.copyright.pack(side="bottom",fill=X)



        self.root.bind('<Control-c>', quit) 
        self.root.bind('<Control-v>', self.paste)

        self.root.mainloop()


    def on_closing(self,*arg):
        
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            
            self.root.destroy()
            os._exit(0)
             
    
    
    def downThread(self):
        
        thread =Thread(target=self.downloader)
        thread.start()
    
    def progress(self,chunk,file_handle,remaining):
         
        file_downloaded = int(file_size-remaining)
        per = (file_downloaded/file_size)*100
        self.download_status.config(text='{:00.0f} % downloaded'.format(per))
    
    def downloader(self):
        global file_size, download_status
        self.download_button.config(state=DISABLED)
        self.download_status.pack(side="bottom",fill=X) #.place(x=230,y=250)
    
        try:
            url1 = self.url.get()
            path = filedialog.askdirectory()
            yt   = YouTube(url1,on_progress_callback=self.progress)
            if os.path.isdir(path):
                video = yt.streams.filter(progressive=True,file_extension='mp4').first()
                file_size = video.filesize
                video.download (path)
                self.download_status.config(text = 'Download Finish...' )
                res = messagebox.askyesno("Youtubr Video Downloader","Do youtube another video ?")
            
                if res == 1:
                    self.download_status.config(text = 'Restarted' )
                    self.url.delete(0,END)
                    self.download_button.config(state= NORMAL)
                    
                else:
                    self.root.destroy()
            else:
                messagebox.showerror("error","no directory exist")
                
                
        except Exception :
            if(self.url.get()== ''):
                self.download_status.config(text = 'Enter The URL')
                self.download_button.config(state=NORMAL)
            else:
                self.download_status.config(text = 'Failed! There is an error.')
                self.download_button.config(state=NORMAL)
    
    def paste(self,event):
        urlClip = pyperclip.paste()
        self.url.insert(0, urlClip)
    
    def quit(self,event):
        print ("you pressed control c")
        #root.destroy()
        os._exit(0)
    
    
        
        
    
    
    
if __name__ == "__main__":
    
    try:
        tuby()

    except KeyboardInterrupt:
        print('Your have force stoped the Tuby. (Unexpected Keyboard Interuption)')
        

    
    

