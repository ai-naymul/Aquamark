import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk

def open_file():
    file = filedialog.askopenfilename()
    if file:
        image = Image.open(file)
        max_width = 400
        max_height = 300
        image.thumbnail((max_width,max_height))
        photoimage = ImageTk.PhotoImage(image)
        image_label.config(image=photoimage)
        image_upload.image = photoimage


window = tk.Tk()
window.geometry("800x700")

## Title Of the Project
window.title("Aquamark Pro")



## Welcome Message
welcome_message = tk.Label(text="Welcome To The Aquamark Pro", font=(25,15,'bold'))
welcome_message.pack(padx=150)

## Show Preview Image
image_label = tk.Label(window)
image_label.pack(padx=100,pady=100)
## Image uplaod button
image_upload = tk.Button(text="Upload you image here", command=open_file)
image_upload.pack(padx=100)


window.mainloop()