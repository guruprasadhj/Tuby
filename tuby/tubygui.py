#!/usr/bin/python
from tkinter import *
from PIL import Image,ImageTk
import os,re,threading,pyfiglet
import validate, dengine
#beta version and will be added soon

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

def on_closing(*arg):
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    root.destroy()
    os._exit(0)

#Change Page
def changepage():
    global page_Num, root,app
    app.pack_forget()
    if page_Num == 1:
        tuby_plus(root)
        page_Num = 2
    else:
        tuby(root)
        page_Num = 1


def validation(event):
    global url_link
    OnPressed_Download()
    url_link = url.get()
    validate.redirect_link(url_link,loading_label)

def net_check(*args): 
    global status_text,status
    status_text = Label(app, font = ('Courier 15 bold'),bg='#2c2c2c',fg='white')
    status_text.place(x = 27,y=267)
    status = Label(app,bg='#2c2c2c')
    status.place(x=10,y=270)
    while True:
        status_img = validate.check(online_img,offline_img)
        status.config(image = status_img)
        off_or_on = StringVar()
        off_or_on.set('online') if status_img==online_img else off_or_on.set('offline') 
        status_text.config(textvariable = off_or_on,)
        
def loading(chunk,file_size,remaining):
    file_downloaded = int(dengine.file_size-remaining)
    pers = str((file_downloaded/dengine.file_size)*100)
    per.set(pers)
    print(pers)
        #if per == 100:

# multi-tasking with internet connection check and downloading video
def downThread(url_link,loading_label):
    print('Hello World!!')
    
    download_thread = threading.Thread(target=dengine.ytdownloader(url_link,loading_label))
    download_thread.start()

def tuby_plus(root):
    app = Frame(root,bg='#2c2c2c')
    app.pack()

def clear_entry(*args):
    url.delete(0, END)

def OnPressed_Download(*args):
    print('OnPressed_Download')
    app.pack_forget()
    loading_gif.place(x=180,y=50)
    loading_label.pack(side="bottom",fill=X)

def OnHover_Download(*args):
    #print('OnHover_Download')
    download_text.config(fg='#2c2c2c')


def OnLeave_Download(*args):
    #print('OnLeave_Download')
    download_text.config(fg='#f3f3f3')


#Minimal Ui
def tuby(root):
    global app,url_img,url_label,Download_label,downloader_label,download_text,downloader_text,url,thread
    
    app = Frame(root,bg='#2c2c2c')
    app.pack(fill='both', expand=True)

    downloader_text = Label(app,text = 'uby Downloader',font=('Calibri',15,'bold'),bg='#2c2c2c',fg='white')
    downloader_text.place(x=65,y=45)

    downloader_label = Label(app,image = downloader_img,bg='#2c2c2c' )
    downloader_label.place(x=15,y=25)
    
    #Internet Check
    thread = threading.Thread(target= net_check)
    thread.start()

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



def mode_switch():
    global btnState
    
    if btnState: #Dark Mode
        mode.config(image=dark_img, bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
        root['bg'] = ('#202020')
        title_bar.config(bg='#212121')
        close_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        add_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        minus_button.config(bg='#090909',fg='#888',highlightcolor="#090909", highlightbackground="#090909")
        app.config(bg='#2c2c2c')
        downloader_text.config(bg='#2c2c2c',fg='white')
        downloader_label.config(bg='#2c2c2c')
        url_label.config(bg='#2c2c2c')
        Download_label.config(bg='#2c2c2c')
        status_text.config(bg='#2c2c2c',fg='#f3f3f3')
        status.config(bg='#2c2c2c',fg='#f3f3f3')
        btnState = False
    
    else: #Light Mode
        mode.config(image=light_img,bg='#cccccc',activebackground='#cccccc',bd=0,highlightcolor="#cccccc", highlightbackground="#cccccc", )
        root['bg']=('white')
        title_bar.config(bg='#cccccc')
        close_button.config(bg='#74777a',fg='black',activebackground='#bb0000', highlightcolor="#74777a", highlightbackground="#74777a")
        add_button.config(bg='#74777a',  fg='black',activebackground='#e9730c', highlightcolor="#74777a", highlightbackground="#74777a")
        minus_button.config(bg='#74777a',fg='black',activebackground="#107e3e", highlightcolor="#74777a", highlightbackground="#74777a")
        app.config(bg='#f3f3f3')
        downloader_text.config(bg='#f3f3f3',fg='black')
        downloader_label.config(bg='#f3f3f3')
        url_label.config(bg='#f3f3f3')
        Download_label.config(bg='#f3f3f3')
        status_text.config(bg='#f3f3f3',fg='#2c2c2c')
        status.config(bg='#f3f3f3',fg='#2c2c2c')
        btnState = True


if __name__ == "__main__":
    global loading_label,per

    print(pyfiglet.figlet_format("Tuby", font = "slant"  ) )
    page_Num = 1
    srcPath = os.path.dirname(os.path.abspath(__file__))
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    #root.overrideredirect(True)
    #root.wm_attributes('-type', 'splash')
    #root.update_idletasks()
    root['bg'] = ('black') #202020
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2) - (600/2)
    y_coordinate = (screen_height/2) - (350/2)
    root.geometry("{}x{}+{}+{}".format(600, 350, int(x_coordinate), int(y_coordinate)))
       
    #Title Bar
    title_bar = Frame(root, bg='#212121', relief='raised', bd=0, height=20, width=600)
    close_button = Button(title_bar ,text='X', command=on_closing,   width=1, bg="#090909", fg="#888",activebackground='#ff453a',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    add_button   = Button(title_bar ,text='+', command=changepage,   width=1, bg="#090909", fg="#888",activebackground='#ff9f0a',activeforeground='black', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    minus_button = Button(title_bar ,text='_', command=root.destroy, width=1, bg="#090909", fg="#888",activebackground='#32d74b',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
    

    btnState  = False 
    dark_img  = Image.open(srcPath + '/assets/dark-mode.png')
    dark_img  = dark_img.resize((37,20),Image.ANTIALIAS)
    dark_img  = ImageTk.PhotoImage(dark_img)

    light_img = Image.open(srcPath + '/assets/light-mode.png')
    light_img = light_img.resize((37,20),Image.ANTIALIAS)
    light_img = ImageTk.PhotoImage(light_img)

    mode = Button(title_bar,image= dark_img,command=mode_switch,bg='#202020',activebackground='#090909',bd=0,highlightcolor="#202020", highlightbackground="#202020",)
    mode.pack(side='left')

    title_bar.pack(side='top', fill=X)
    close_button.pack(side='right')
    add_button.pack(side='right')
    minus_button.pack(side='right')
    title_bar.bind('<B1-Motion>', move_window)

    offline_img = Image.open(srcPath + '/assets/red.png')
    offline_img = offline_img.resize((10,10),Image.ANTIALIAS)
    offline_img = ImageTk.PhotoImage(offline_img)

    online_img = Image.open(srcPath + '/assets/green.png')
    online_img = online_img.resize((10,10),Image.ANTIALIAS)
    online_img = ImageTk.PhotoImage(online_img)

    downloader_img = Image.open(srcPath + '/assets/downloader.png')
    downloader_img = downloader_img.resize((50,50),Image.ANTIALIAS)
    downloader_img = ImageTk.PhotoImage(downloader_img)

    url_img  = Image.open(srcPath + '/assets/url.png')
    url_img  = url_img.resize((30,30),Image.ANTIALIAS)
    url_img  = ImageTk.PhotoImage(url_img)

    download_img = Image.open(srcPath + '/assets/download.png')
    download_img = download_img.resize((260,100),Image.ANTIALIAS)
    download_img = ImageTk.PhotoImage(download_img)

    tuby(root)
    
    loading_gif = GifLabel(root,srcPath+'/assets/ezgif.com-crop.gif',100)
    
    per = StringVar()
    per.set('Please wait...')
    loading_label= Label(root,textvariable = per,bg='white',fg='black') 
    
    copyright = Label(root, text="Cup ,\xa9 2020", bg= "red",fg="white"  )
    copyright.pack(side="bottom",fill=X)


    root.mainloop()