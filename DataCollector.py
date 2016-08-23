from tkinter import *
import threading
import datetime
import os.path

def close_window(root): 
    root.destroy()

def popup():
        root = Tk(className ="Current Task")
        
        frame = Frame(root)
        frame.pack()

        t = Text(root, height=20, width=40)
        t.pack()
        root.configure(background='red')
        root.attributes("-topmost", True)
        def retrieve_input():
            
            input = t.get("1.0",'end-1c')
            print(input)
            currentddt = str(datetime.date.today())
            if os.path.exists('D:\\seeroo_timesheet\\'+currentddt+'.txt'):
                 f = open('D:\\seeroo_timesheet\\'+currentddt+'.txt','a+')
                 if input=="":
                         f.seek(0)
                         lineList = f.readlines()
                         lastline=lineList[-1]
                         lastlinearray = lastline.strip().split("$$")                         
                         count=lastlinearray[-1]
                         content=lastlinearray[1]
                         print("content:"+content)
                         countnew=int(count)+1                         
                         lineList[-1]=str(datetime.datetime.today().strftime('%I:%M %p'))+"$$"+content+"$$"+str(countnew)
                         file=open('D:\\seeroo_timesheet\\'+currentddt+'.txt','w')
                         file.writelines(lineList)
                         print(countnew)
                 else:       
                         f.write("\n"+str(datetime.datetime.today().strftime('%I:%M %p'))+"$$"+input+'$$1') # python will convert \n to os.linesep
            else:
                 f = open('D:\\seeroo_timesheet\\'+currentddt+'.txt','a')
                 f.write(str(datetime.datetime.today().strftime('%d/%m/%Y %I:%M %p'))+'\n') # python will convert \n to os.linesep
                 f.write(str(datetime.datetime.today().strftime('%I:%M %p'))+"$$"+input+'$$1') # python will convert \n to os.linesep
            
            f.close() # you can omit in most cases as the destructor will call it
            close_window(root)
            
        foo = Button(root,text="Save to file", command=retrieve_input)
        foo.pack()
        root.mainloop()


def printit():
          popup()
          threading.Timer(5, printit).start()
         

printit()

