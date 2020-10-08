#!/usr/bin/python
from tkinter import *
from PIL import Image,ImageTk
import os,re
from validate import redirect_link
#beta version and will be added soon

#Move Window
def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

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
    url_link = url.get()
    redirect_link(url_link)



#Plus Page (this page show )
def tuby_plus(root):

    app = Frame(root,bg='#2c2c2c')
    app.pack()
def clear_entry(*args):
    url.delete(0, END)

def OnPressed_Download(*args):
    print('OnPressed_Download')
    

def OnHover_Download(*args):
    #print('OnHover_Download')
    download_text.config(fg='#2c2c2c')

def OnLeave_Download(*args):
    #print('OnLeave_Download')
    download_text.config(fg='#f3f3f3')

#Minimal Ui
def tuby(root):
    global app,url_img,url_label,Download_label,downloader_label,download_text,downloader_text,url
    
    app = Frame(root,bg='#2c2c2c')
    app.pack(fill='both', expand=True)

    downloader_text = Label(app,text = 'uby Downloader',font=('Calibri',15,'bold'),bg='#2c2c2c',fg='white')
    downloader_text.place(x=65,y=45)

    downloader_label = Label(app,image = downloader_img,bg='#2c2c2c' )
    downloader_label.place(x=15,y=25)
    
    

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
    download_text.bind('<Button-1>', OnPressed_Download)
    download_text.bind('<Enter>', OnHover_Download)

#Switch Mode
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
        btnState = True


if __name__ == "__main__":
    page_Num = 1
    srcPath = os.path.dirname(os.path.abspath(__file__))
    root = Tk()
    #root.overrideredirect(True)
    #root.wm_attributes('-type', 'splash')
    #root.update_idletasks()
    root['bg'] = ('#202020')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2) - (600/2)
    y_coordinate = (screen_height/2) - (350/2)
    root.geometry("{}x{}+{}+{}".format(600, 350, int(x_coordinate), int(y_coordinate)))
    
    
    #Title Bar
    title_bar = Frame(root, bg='#212121', relief='raised', bd=0, height=20, width=600)
    close_button = Button(title_bar ,text='X', command=root.destroy, width=1, bg="#090909", fg="#888",activebackground='#ff453a',activeforeground='white', bd=0,highlightcolor="#090909", highlightbackground="#090909",)
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
    copyright = Label(root, text="Cup ,\xa9 2020", bg= "red",fg="white"  )
    copyright.pack(side="bottom",fill=X)


    root.mainloop()