#Import the required libraries

from tkinter import *

from tkinter.ttk import *

#Create an instance of tkinter frame

win= Tk()

#Set the geometry of frame

win.geometry("350x200")

#Define a function

def start():

   task=10

   x=0

   while(x<task):

      time.sleep(1)

      bar['value']+=10

      x+=1

      win.update_idletasks()    

bar= Progressbar(win, orient=HORIZONTAL, length=300)

bar.pack(pady=20)

#Create a button

Button(win, text="Download", command=start).pack(pady=20)

win.mainloop()
