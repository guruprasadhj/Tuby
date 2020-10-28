import sys
import time,pyfiglet,threading
from pytube import YouTube
try:
    import validate 
    import dengine
except NameError:
    import tuby.validate 
    import tuby.dengine
def print_slow(str):
        for char in str:
            time.sleep(.1)
            sys.stdout.write(char)
            sys.stdout.flush()

def redirect(url):
    try:
        validation = tuby.validate.offline_check(url)
    except NameError:
        validation = validate.offline_check(url)
    path = str(input('Enter the download location or Drag n Drop the folder to be downloaded:'))
    if (validation == ('ytvideo')):
        download_thread = threading.Thread(target=dengine.yt_downloader,args=(url,path))
        download_thread.start()

    elif(validation == ('ytplaylist')):
        print("It's a playlist")

def main():
    print_slow('welcom to Tuby \n')
    url = str(input('Enter an URL to be Dowload: '))
    redirect(url)

    
if __name__ == "__main__":
    import os, platform
    #os.system('clear')
    print(" [  INFO  ] - Operating system name: " , os.name,'\n' )

    print(" [  INFO  ] - Platform name:",platform.system(),'\n')
    print(" [  INFO  ] - Platform release:",platform.release(),'\n')
    print(' [  INFO  ] - Platform processor:', platform.processor(),'\n') 
    print(' [  INFO  ] - Platform architecture:', platform.architecture(),'\n')
    print(' [  INFO  ] - Machine type:', platform.machine(),'\n')
    print(' [  INFO  ] - Systems network name:', platform.node(),'\n') 
    print(' [  INFO  ] - Platform information:', platform.platform(),'\n') 
    print(' [  INFO  ] - Python compiler:', platform.python_compiler(),'\n') 
    print(' [  INFO  ] - Python SCM:', platform.python_compiler(),'\n')
    print(' [  INFO  ] - Python implementation:', platform.python_implementation(),'\n') 

    #main()
