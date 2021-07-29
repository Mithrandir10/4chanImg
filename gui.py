from tkinter import *
from tkinter.ttk import *
from os import link, name
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import cv2
import urllib
import numpy as np
from functools import partial
import shutil
import glob
import threading
import string,re

class tcreator(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self,obj):
        if(self.name=="thread1"):
         while(obj.wcheck==1):
          obj.updater()
        elif(self.name=="thread2"):
            obj.mainwin()
class downloader():
  root = Tk()
  wcheck=1
  def mainwin(self):
   
   
   self.root.title("4chan Image Downloader")
   self.root.geometry("500x200+300+300")
   f1=Frame(self.root)
   f1.grid(column=0,row=0,padx=5,pady=10)
   mylabel=Label(f1,text="URL : ")
   y1=StringVar(f1,name="url")
   y2=StringVar(f1,name="filepath")
   link=Entry(f1,textvariable=y1)
   f2=Frame(self.root)
   f2.grid(column=0,row=1,padx=5,pady=10)
   label2=Label(f2,text="File Path : ")
   label2.pack(side=LEFT)
   fpath=Entry(f2,textvariable=y2)
   fpath.pack(expand=True,side=RIGHT)
   link.pack(side=RIGHT,expand=True)
   mylabel.pack(side=LEFT)
   f3=Frame(self.root)
   f3.grid(column=0,row=2,padx=5,pady=10)
   print(y1.get())

   submit=Button(f3,command=lambda: self.fchan(y1.get(),y2.get()),text="SUBMIT")
   submit.pack(pady=5)


   self.root.mainloop()
  def updater(self):
      print("test")
      self.root.update_idletasks()
  def fchan(self,x1,x2):

   rlist=self.bar()
   pbar=rlist[1]
   plabel=rlist[0]
   url=x1
   page_response = requests.get(url, timeout=240)
   page_content = BeautifulSoup(page_response.content, "lxml")
   div=page_content.find_all('div',class_='file')
   img_link=page_content.find_all('a',class_='fileThumb')
   name=page_content.find('span',class_="subject")
   
  
   print(img_link)
   j=0 
   nump=len(div)
   path2=x2
   try:
    os.chdir(path2)
   except:
    os.mkdir(x2)
    os.chdir(x2)
   for i in img_link:
       j=j+1
       k=i['href']
       print(k[-3:])
       ipath=f"https:{i}"
       pbar['value']=(j/nump)*100
       plabel['text']=f"{j} of {nump} downloaded"
       self.root.update_idletasks()
       self.root.update()
       if(k[-3:]=="ebm" or k[-3:]=="gif"):
            try:
              req = urllib.request.urlopen(f"https:{i['href']}")
              print(f"https:{i['href']}")
              vid=cv2.VideoCapture(f"https:{i['href']}")
              fps=vid.get(cv2.CAP_PROP_FPS)
              print(fps)
              w=vid.get(3)
              h=vid.get(4)
              fourcc = cv2.VideoWriter_fourcc(*'XVID')
              
             
              parent=x2
              new="Frames"
              dirpath=os.path.join(parent,new)
              os.mkdir(dirpath)
              fps=vid.get(cv2.CAP_PROP_FPS)
              print(fps)
              
              check,image = vid.read()
              count = 0
              while check:
                cv2.imwrite(f"{dirpath}/frame{count}.jpg", image)   
                check,image = vid.read()
                print(f'Frame number {count}: {check}')
                count += 1
              print("\nPlease Wait!!")
              
              t=0
              
              
              
              vimages=[]
              img=glob.glob(f"{dirpath}/*.jpg")
              def srtcrt(a):
                 x=len(dirpath)
                 return(int(a[(x+6):-4]))
              img.sort(key=srtcrt)
              for i in img:
                print(i)
              
                
              
              for i in img:
                  img1=cv2.imread(i)
                  h,w,layers=img1.shape
                  size=(w,h)
                  vimages.append(img1)
              
                  
              v_name=f'Vid{j}'
              try:
               vid=cv2.VideoWriter(f'{x2}/{v_name}.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,size)
              except:
                print("File not found")
                os.rmdir(dirpath)
                sys.exit()
              
              for i in range(len(vimages)):
                  vid.write(vimages[i])
              vid.release()
              shutil.rmtree(dirpath)
              print("DONE")
              print(f"OUTPUT : {v_name}")
            except:
              print("fail")
       else:
        req = urllib.request.urlopen(f"https:{i['href']}")
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        nme=str(name.contents)
        nme=re.sub(r'\W+', '',nme)
        try:
         print(f"{name.contents[0]}{j}.{k[-3:]}")
        except:
          print("exception")
        cv2.imwrite(f"{nme}{j}.{k[-3:]}", img)
   pbar.destroy()
   self.root.update()
   self.root.destroy()
   self.wcheck=0
  def bar(self):
   rlist=[]
   f3=Frame(self.root)
   f3.grid()
   plabel=Label(f3)
   plabel.pack(padx=5)
   pbar=Progressbar(f3,orient=HORIZONTAL,length=100,mode='determinate')
   pbar.pack(padx=10)
   rlist.append(plabel)
   rlist.append(pbar)
   return rlist
  
dloader=downloader()
thread2=tcreator("thread2")

thread2.run(dloader)



 
 