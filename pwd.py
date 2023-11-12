from tkinter import *
from random import shuffle
import random
out=[]
b=['']
root=Tk()
for i in range(20):
    root.grid_rowconfigure(i,weight=1)
for j in range(20):
    root.grid_columnconfigure(j,weight=1)
f=Frame(root,highlightbackground='blue',width=10,highlightthickness=3)
f.grid(row=1,column=10,ipadx=20,ipady=20)
h=Label(root,text="WELCOME TO PASSWORK GENERATOR")
h.grid(row=0,column=10,padx=10,pady=10,ipadx=10,ipady=10)
l=Label(f,text="Enter the length of the password: ")
l.grid(row=3,column=7,padx=10,pady=10,ipadx=10,ipady=10)
g=Entry(f)
g.grid(row=3,column=9,padx=10,pady=10)
def click(event=None):
    i.config(state=DISABLED)
    a=['a','b','c','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','@','$','*','&']
    shuffle(a)
    c=int(g.get())
    for j in range(0,c):
        b=random.choice(a)
        out.append(b)
    output=''.join(out)
    o.config(text="Passwork Generated: "+output)
i=Button(f,text="Click to generate",command=click)
i.place(x=150,y=65)
o=Label(root,text="")
o.grid(row=5,column=10,padx=10,pady=10)
g.bind('<Return>', click)
root.mainloop()

'''
#without using tkinter
from random import shuffle
import random
out=[]
b=['']
u=int(input("Enter the length of the pwd need to generate: "))
a=['a','b','c','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','@','$','*','&']
shuffle(a)
for j in range(0,u):
    b=random.choice(a)
    out.append(b)
output=''.join(out)
print(output)'''
