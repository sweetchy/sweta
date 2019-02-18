from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("800x600")
root.title('python')
root.config(background='red')
root.resizable()
#lebel widgit
title=Label(root,text="form",font=("Times New Roman",16),fg="blue",background="black")
title.grid(row=0,column=2) #or we can use title.grid(),or title.place()
root.resizable()
title=Label(root,text='enter ur name',font=("Times New Roman",16),fg="blue",background="black")
title.grid(row=1,column=1)
name=Entry(root,width=20,font=("",26),background='cyan')
name.grid(row=1,column=2,padx=10,pady=(20,0),columnspan=2)
title=Label(root,text='enter your age',font=("Times New Roman",16),fg="blue",background="black")
title.grid(row=3,column=1,padx=10,pady=(20,0))
age=Entry(root,width=20,font=("",26),background='cyan')
age.grid(row=3,column=2,padx=10,pady=(20,0),columnspan=2)
#radioButton widget

title=Label(root,text='select your gender',font=("times New Roman",16),fg="blue",background="black")
title.grid(row=4,column=1)
gender=StringVar()
male=Radiobutton(root,text="male",value='male',variable=gender,font=("",20),background='cyan')
male.grid(row=4,column=2,padx=10,pady=(20,0))
female=Radiobutton(root,text="female",value='female',variable=gender,font=("",20),background='cyan')
female.grid(row=4,column=3,padx=10,pady=(20,0))

#combobox widget
stream=ttk.Combobox(root,state='readonly',font=("",20),background='red',foreground='cyan')
stream.set("select your stream")
stream['values']=['BBA','BIM','BCA','BSCCSIT']
stream.grid(row=7,column=2,padx=10,pady=(20,0))

'''print(name.get())
    print(age.get())
    print(gender.get())
    print(stream.get())'''
def click():
  top=Toplevel(root)
  info=Label(top,text=name.get())
  info.grid(row=1,column=2)
  ag=Label(top,text=age.get())
  ag.grid(row=2,column=2)

#button widgit
submit=Button(root,text='SUBMIT',font=("Times New Roman",16),background="cyan",command=lambda:click())
submit.grid(row=8,column=2,padx=10,pady=(20,0))
root.mainloop()
