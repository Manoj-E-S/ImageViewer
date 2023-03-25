#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image

counter = 0

def after(imgContainer):
    global counter
    imgContainer[counter].grid_forget()
    counter = (counter + 1) if (counter < len(imgContainer)-1) else 0
    imgContainer[counter].grid(row=0, column=0, columnspan=3)
    status = Label(window, text=f"Image {counter+1} of {len(imgContainer)}  ", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def previous(imgContainer):
    global counter
    imgContainer[counter].grid_forget()
    counter = (counter - 1) if (counter > 0) else (len(imgContainer)-1)
    imgContainer[counter].grid(row=0, column=0, columnspan=3)
    status = Label(window, text=f"Image {counter+1} of {len(imgContainer)}  ", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


window = Tk()
window.title("Image Viewer")


# Create Images

images = []
for i in range(1, 7):
    im = Image.open(f'/home/manoj/PythonGui/ImgViewer/Images/Image{i}.jpg')
    
    width = int(1920/3.5)
    wfraction = width/float(im.size[0])
    height = int(float(wfraction)*float(im.size[1]))
    
    images.append(ImageTk.PhotoImage(im.resize((width, height))))


# Create Labels to hold images and place them in the window

labels = []
for img in images:
    labels.append(Label(window, image=img))

labels[0].grid(row=0, column=0, columnspan=3)


# Status bar

status = Label(window, text=f"Image {counter+1} of {len(labels)}  ", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Frame object

frame = LabelFrame(window, text="", padx=0, pady=0)
frame.grid(row=1, column=1, padx=5, pady=5)


# Create and Display Buttons

aft = Button(frame, text=">>", command=lambda x = labels: after(x), padx=10, pady=10)
prev = Button(frame, text="<<", command=lambda x = labels: previous(x), padx=10, pady=10)
Exit = Button(frame, text="Quit", command=window.quit, padx=20 ,pady=10)

aft.grid(row=0, column=3)
prev.grid(row=0, column=1)
Exit.grid(row=0, column=2, pady=5)


# Radio Buttons: Like, Save

# v1 = IntVar();
# v1.set(0)

# like = Radiobutton(frame, text="Like", variable=v1, value=1)
# like.grid(row=0, column=0, padx=10)

# Save = Radiobutton(frame, text="Save", variable=v1, value=2)
# Save.grid(row=0, column=4, padx=10)

window.mainloop()
