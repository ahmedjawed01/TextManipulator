import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import sys
from Tkinter import *
import subprocess as sp
import glob 
import getpass
import re
import tkFileDialog
root=None
run_B=None
entryBox=None
entryBox2=None
entryBox3=None
entryBox4=None
entryBox5=None
counter=0
changingText=None
pathL=None
changingText=None




def exitButtonPushed():
    global root
    root.destroy()  #Kill the root window
  

    



    




    
    
def buttonPushed():
    global entryBox
    global entryBox2
    global entryBox3
    global entryBox4
    global entryBox5
    global run_B
    global pathL
    txt=''
    end_txt=''
    contain_txt=''
    replace1_txt=''
    replace2_txt=''
    if entryBox.get():
        txt=entryBox.get()
        
    if entryBox2.get():    
        end_txt=entryBox2.get()
        
    if entryBox3.get():    
        contain_txt=entryBox3.get()

    if entryBox4.get():    
        replace1_txt=entryBox4.get()

    if entryBox5.get():    
        replace2_txt=entryBox5.get()

    replace1_txt=replace1_txt.replace("#NOTNUMBER","[^0-9]").replace("#NUMBER","[0-9]").replace("#NOTALPHA","[a-zA-Z0-9_]").replace("#ALPHA","[a-zA-Z0-9_]").replace("^","\\^").replace("+","\\+")
    replace1_txt=replace1_txt.replace("#LLETTER","[a-z]").replace("#ULETTER","[A-Z]").replace("#ANY",".*").replace("#REPEAT","+").replace(".","\\.").replace("*","\\*")
    replace1_txt=replace1_txt.replace("?","\\?")

   

    

    """
    #NUMBER Matches any decimal digit; this is equivalent to the class [0-9]
    #NOTNUMBER Matches any non-digit character
    #ALPHA Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
    #NOTALPHA Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]
    #LLETTER  Matches any lowercase letters, [a-z]
    #ULETTER Matches uppercase letters,  [A-Z]
    #ANY Matches any  characters many times , [.*]
    #REPEAT match 1 or more repetitions of the preceding characters 
    """
       
    new_data=""
    data=open(pathL,'r')
    
    for line in data.readlines():
        
        if (not line.strip().startswith(txt) or txt=='' )  and (not line.strip().endswith(end_txt) or end_txt=='') and (contain_txt not in line.strip() or contain_txt=='') :   
            
            if replace1_txt and replace2_txt:
                
                line_repl=re.sub(replace1_txt,replace2_txt,line)
                
                new_data+=line_repl
            else:
                new_data+=line
            
        
            
            
        
            
    data.close()
    pathL2=pathL.replace(".txt","")
    write_data=open(pathL2+'NEW.txt','w')
    write_data.write(new_data)
    write_data.close()
        
        
def browse():
    global pathL
    global changingText
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    
    file=str(file).split(",")[0].split("u'")[-1].replace("'","").replace("/","\\")
    pathL=file
    changingText.set(pathL)
    
    


def main():
    global root
    global changingText
    global run_B
    global entryBox
    global entryBox2
    global entryBox3
    global entryBox4
    global entryBox5
    global changingText
    root=Tk() # root base windows where all widgets go
    root.wm_title("TextManipulator | hackspc.com")
    root.geometry("600x500")
    root["padx"] = 40
    root["pady"] = 40

    choose=Button(root,text="Choose .txt File",command=browse)
    choose["width"]=20
    choose.grid(row=0,column=0, sticky=W)
    changingText=StringVar()
    changingText.set("")
    selected=Label(root,textvariable=changingText)
    
    selected.grid(row=0,column=1, sticky=W)
    
    starts_with=Label(root,text="Delete line that starts with:")
    starts_with["width"]=20 
    starts_with.grid(row=1,column=0, sticky=W) 
    
    
    entryBox=Entry(root)
    entryBox["width"]=60
    entryBox.grid(row=1,column=1, sticky=W)
    
    ends_with=Label(root,text="Delete line that ends with:")
    ends_with["width"]=20 
    ends_with.grid(row=2,column=0, sticky=W) 
    
    entryBox2=Entry(root)
    entryBox2["width"]=60
    entryBox2.grid(row=2,column=1, sticky=W)

    contain=Label(root,text="Delete line that contains:")
    contain["width"]=20 
    contain.grid(row=4,column=0, sticky=W) 
    
    entryBox3=Entry(root)
    entryBox3["width"]=60
    entryBox3.grid(row=4,column=1, sticky=W)

    replace1L=Label(root,text="Replace text:")
    replace1L["width"]=20 
    replace1L.grid(row=6,column=0, sticky=W) 
    
    entryBox4=Entry(root)
    entryBox4["width"]=60
    entryBox4.grid(row=6,column=1, sticky=W)

    replace2L=Label(root,text="with:")
    replace2L["width"]=20 
    replace2L.grid(row=7,column=0, sticky=W)

    entryBox5=Entry(root)
    entryBox5["width"]=60
    entryBox5.grid(row=7,column=1, sticky=W)


    empty1L=Label(root,text="")
    empty1L["width"]=20 
    empty1L.grid(row=8,column=0, sticky=W)
    
    run_B=Button(root,text="EDIT",command=buttonPushed)
    run_B["width"]=20
    run_B.grid(row=9,column=0, sticky=E)
    
    empty2L=Label(root,text="")
    empty2L["width"]=20 
    empty2L.grid(row=10,column=0, sticky=W)
    
   
    
    CRTICA=Label(root,text="----------------------------------------------------------------------------------------------------------")
    CRTICA["foreground"]="red"
    CRTICA["justify"]='center'
    CRTICA.grid(row=11,column=0,columnspan=2, sticky=W) 
    
    
    NUMBER=Label(root,text="#NUMBER Matches any decimal digit; this is equivalent to the class [0-9]")
    NUMBER["foreground"]="red"
    NUMBER["justify"]='center'
    NUMBER.grid(row=12,column=0,columnspan=2, sticky=W) 
    
    NOTNUMBER=Label(root,text="#NOTNUMBER Matches any non-digit character")
    NOTNUMBER["foreground"]="red"
    NOTNUMBER["justify"]='center'
    NOTNUMBER.grid(row=13,column=0,columnspan=2, sticky=W) 
    
    ALPHA=Label(root,text="#ALPHA Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]")
    ALPHA["foreground"]="red"
    ALPHA["justify"]='center'
    ALPHA.grid(row=14,column=0,columnspan=2, sticky=W) 
    
    NOTALPHA=Label(root,text="#NOTALPHA Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]")
    NOTALPHA["foreground"]="red"
    NOTALPHA["justify"]='center'
    NOTALPHA.grid(row=15,column=0,columnspan=2, sticky=W) 
    
    LLETTER=Label(root,text="#LLETTER  Matches any lowercase letters, [a-z]")
    LLETTER["foreground"]="red"
    LLETTER["justify"]='center'
    LLETTER.grid(row=16,column=0,columnspan=2, sticky=W) 
    
    ULETTER=Label(root,text="#ULETTER Matches uppercase letters,  [A-Z]")
    ULETTER["foreground"]="red"
    ULETTER["justify"]='center'
    ULETTER.grid(row=17,column=0,columnspan=2, sticky=W)

    ANY=Label(root,text="#ANY Matches any  characters many times , [.*]")
    ANY["foreground"]="red"
    ANY["justify"]='center'
    ANY.grid(row=18,column=0,columnspan=2, sticky=W)

    REPEAT=Label(root,text="#REPEAT match 1 or more repetitions of the preceding characters ")
    REPEAT["foreground"]="red"
    REPEAT["justify"]='center'
    REPEAT.grid(row=19,column=0,columnspan=2, sticky=W)


    
   


    

    CRTICA2=Label(root,text="----------------------------------------------------------------------------------------------------------")
    CRTICA2["foreground"]="red"
    CRTICA2["justify"]='center'
    CRTICA2.grid(row=20,column=0,columnspan=2, sticky=W) 
    
    
    website=Label(root,text="Copyright © 2014 hackspc.com All Rights Reserved")
    website["width"]=40
    website["justify"]='center'
    website.grid(row=22,column=0,columnspan=2, sticky=W) 
    
    root.mainloop() # Start the event loop wait to somethin happend e.x. press button , click button


main()




