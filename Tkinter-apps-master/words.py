from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
#import lxml.html  
#import requests 

try: #python 3
    from tkinter import *
 
except: #python 2
    from Tkinter import *
  
def web_scrap(word):

    global t
    get_url="http://dictionary.com/browse/"+str(word.replace(" ","-"))
    url=urlopen(get_url)
    content=url.read()
    soup=BeautifulSoup(content,"lxml")
    line=soup.find('div', attrs={'class': 'def-content'})
      
    t=line.text.strip().split()
      

    #can also be done by lxml below is scrapping using lxml

    #tree = lxml.html.fromstring(content)
    #div=tree.cssselect('div.def-content')[0]
    #t=div.text
    #print(t.strip())

    popup() # calling notification window


class mywindow(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
           
    def initUI(self):
        self.parent.title("MEANING FINDER")
        self.pack(fill=BOTH, expand=True)

        global ent

        frame = Frame(self)
        frame.pack(fill=X)
        Label(frame, text="Enter a word : ").pack(side="top",pady=5,padx=5)
        ent = Entry(frame,width=150)
        ent.config(font=("Times", 16, "bold"))
        ent.bind("<Return>",(lambda event: web_scrap(ent.get())))
        ent.pack(side="left",padx=10)
     

class popup(object):

    def __init__(self,show_time=5000):  
        self.stime=show_time
        self.root = Tk()
        self.root.title("MEANING")
        self.root.geometry('320x85')
        text = Text(self.root)
        text.insert(INSERT,t)
        text.config(font=("Calibri",12,"bold"),wrap=WORD,state=DISABLED)
        text.pack()
        self.root.after(self.stime , lambda:self.root.destroy())  #show tkinter window for 5 seconds
        self.root.mainloop()


def main():
    root = Tk()
    root.geometry("350x60")
    root.resizable(width=False, height=False)
    app = mywindow(root)
    root.mainloop() 

if __name__ == '__main__':
    main()  


    
