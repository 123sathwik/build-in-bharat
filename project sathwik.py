from googletrans import Translator
from gtts import gTTS
import os
from tkinter import *
top=Tk()
top.title("BUILD IN BHARAT PROJECT")
def hty():
    x=y.get()
    translator=Translator()
    e=translator.translate(x,dest="hi").text
    z.delete(0,"end")
    z.insert(0,e)
    language="hi"
    my_obj=gTTS(text=e,lang=language,slow=False)
    my_obj.save("wave.save")
    os.system("wave.save")
def qwe():
    k=p.get()
    translator=Translator()
    q=translator.translate(k,dest="te").text
    h.delete(0,"end")
    h.insert(0,q)
    re=gTTS(text=q,lang="te",slow=False)
    re.save("sathwika.save")
    os.system("sathwika.save")
def asd():
    d=j.get()
    translator=Translator()
    o=translator.translate(d,dest="ta").text
    f.delete(0,"end")
    f.insert(0,o)
    juy=gTTS(text=o,lang="ta",slow=False)
    juy.save("appua.save")
    os.system("appua.save")
def clear():
    y.delete(0,"end")
def clear1():
    p.delete(0,"end")
def clear2():
    j.delete(0,"end")
image1=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\download (1).png")
im=image1.subsample(5,5)
l1=Label(top,text="TRANSLATOR FROM ENGLISH TO HINDI",image=im,compound=RIGHT,bg="yellow",fg="black")
l1.pack()
y=Entry(top)
y.pack()
z=Entry(top)
z.pack()
image2=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\Screenshots\images.png")
im1=image2.subsample(4,4)
b1=Button(top,text="TEXT AND VOICE TRANSLATION",image=im1,compound=LEFT,command=hty)
b1.pack()
image9=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\Screenshots\download.png")
img9=image9.subsample(5,5)
b4=Button(top,image=img9,command=clear)
b4.pack()
image3=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\Screenshots\images (2).png")
img3=image3.subsample(5,5)
l2=Label(top,text="TRANSLATOR FROM ENGLISH TO TELUGU",image=img3,compound=RIGHT,bg="yellow",fg="black")
l2.pack()
p=Entry(top)
p.pack()
h=Entry(top)
h.pack()
image4=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\images.png")
img4=image4.subsample(4,4)
b2=Button(top,text="TEXT AND VOICE TRANSLATION",image=img4,compound=LEFT,command=qwe)
b2.pack()
b5=Button(top,image=img9,command=clear1)
b5.pack()
image5=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\qwe.png")
img5=image5.subsample(5,5)
l3=Label(top,text="TRANSLATOR FROM ENGLISH TO TAMIL",image=img5,compound=RIGHT,bg="yellow",fg="black")
l3.pack()
j=Entry(top)
j.pack()
f=Entry(top)
f.pack()
image6=PhotoImage(file=r"C:\Users\Sathwik\Documents\New folder\OneDrive\Pictures\images (1).png")
img6=image6.subsample(4,4)
b3=Button(top,text="TEXT AND VOICE TRANSLATION",image=img6,compound=LEFT,command=asd)
b3.pack()
b6=Button(top,image=img9,command=clear2)
b6.pack()
top.mainloop()
    
