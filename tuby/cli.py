import sys
import time,pyfiglet
try:
    import validate 
except NameError:
    import tuby.validate 

def print_slow(str):
        for char in str:
            time.sleep(.1)
            sys.stdout.write(char)
            sys.stdout.flush()

def redirect(url):
    validation = tuby.validate.offline_check(url)
    print(validation)

def main():
    print_slow('welcom to Tuby \n')
    url = str(input('Enter an URL to be Dowload: '))
    redirect(url)

    
if __name__ == "__main__":
    
    main()
