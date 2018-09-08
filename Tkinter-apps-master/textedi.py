from tkinter import *
import tkinter.filedialog
from  tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename,asksaveasfilename




def open_file():
    try:
        text.delete(1.0,END)
        
        file=open(askopenfilename() , 'r')
     
        if file != '':
          text.insert(INSERT,file.read())
                
    except:
        pass


def save_file():
    try:
        file_name=asksaveasfilename()
        if  file_name:
           savetext=text.get(0.0,END)
           open(file_name,'w').write(savetext)
    except:
        pass
        
        

root=Tk()

root.title("TEXT EDITOR")
menu=Menu(root)

filemenu=Menu(root)
root.config(menu=menu)

menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="open",command=open_file)
filemenu.add_command(label="save",command=save_file)


text = Text(root, height=30, width=60, font = ("Arial", 10))

scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)                  

text.config(yscrollcommand=scroll.set)           

scroll.pack(side=RIGHT, fill=Y)

text.pack()

root.resizable(0,0)

root.mainloop()
