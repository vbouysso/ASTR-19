
from threading import main_thread
from tkinter.tix import MAIN


def firstfunc(x):
    return ((x**3)+8)

def main():
    a = 9
    b = firstfunc(a)
    print(b)
    if(b > 27):
        print("YAY!")

if __name__=="__main__":
    main()