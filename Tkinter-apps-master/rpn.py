from tkinter import *

import math
import operator            
    
    
class myapp(Frame):

    def __init__ (self,parent):
        Frame.__init__(self ,parent)
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.parent.title("REVERSE POLISH CALCULATOR")
        self.pack( fill=BOTH,expand=True)
        frame1 = Frame(self)
        frame1.place(x=20,y=30)
        frame2 = Frame(self)
        frame2.place(x=550,y=45)
        frame3 = Frame(self)
        frame3.place(x=20,y=100)
        frame4 = Frame(self)
        frame4.place(x=155,y=113)
        frame5 = Frame(self)
        frame5.place(x=255,y=213)
        operator_list = {'+' : operator.add,
                         '-' : operator.sub,
                         '/' : operator.truediv,
                         '*' : operator.mul,
                         '^' : operator.pow,
                         }


        def rpn():
            cop=0
            cnum=0
            global res
            stack = []
            expression=w.get("1.0","end-1c")
            
            labele1=Label(frame5,text="Enter valid Expression")

            
            for i in expression.split(' '):
                if i in operator_list:
                    cop+=1
                    op1=float(stack.pop())
                    op2=float(stack.pop())
                    result=operator_list[i](op1,op2)
                    stack.append(result)
                else:
                    cnum+=1
                    stack.append((i))
            res=stack.pop()
            w2.configure(state="normal")
            w2.insert(END,res)
            w2.configure(state="disabled")
            is_valid=[True if len(expression.split(' '))>2 and cnum==cop+1 else False]
            print(is_valid)
            if not is_valid:
                 labele1.pack()
                 labele1.config(text='yoooo',width=20)
            if is_valid :
             
                labele1.pack()
                labele1.config(text='wrrroo',width=20)      
            


               
        
        label = Label( frame1 , text = "EXPRESSION : ",width = 14 , font = "Verdana 10 bold")
        label.pack( side = LEFT ,padx = 0 , pady = 15 )
        
        w = Text(frame1,width=35,height=1 ,font=("Helvetica",15))
        #w.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        w.pack(side="left",fill=X)
        #w.bind("<Return>", lambda event: callback(event,frame1))
        w.pack(side = "left" , fill = X ,padx = 5 , pady = 15 )
        button=Button(frame2 , width = 10 , text = "Calculate" ,font=("Arial",10,"bold"), command = lambda:rpn())
        button.pack()
        label = Label( frame3 , text = "RESULT : ",width = 10 , font = "Verdana 10 bold")
        label.pack( side = LEFT ,padx = 0 , pady = 15 )
        w2 = Text(frame4,width=35,height=1 ,font=("Helvetica",15))
        w2.configure(state="disabled")
        #w.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        w2.pack(side="left",fill=X)        

        #result = rpn(expression)
        #print(result)
        
def main():
  
    root = Tk()
    root.geometry("700x500")
    #root.resizable(width=False, height=False)
    
    app = myapp(root)
    
    
    
    root.mainloop()  

    
if __name__ == '__main__':
    main()

