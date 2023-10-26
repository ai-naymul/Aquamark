import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk, ImageDraw, ImageFont



window = tk.Tk()
window.geometry("800x700")

## Title Of the Project
window.title("Aquamark Pro")

text_input = tk.Entry()
type = type(text_input)
print=type
get_x = tk.Entry()
get_y = tk.Entry()

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, 'rb') as file:
            original_image = Image.open(file)
            max_width = 400
            max_height = 300
            original_image.thumbnail((max_width,max_height))
            photoimage = ImageTk.PhotoImage(original_image)

            draw = ImageDraw.Draw(original_image)
            
            text= text_input.get()
            font = ImageFont.truetype("arial.ttf", size=35)
            # text_width, text_height = draw.textsize(text, font=font)

            image_width, image_height = original_image.size
            # text_x = (image_width - text_width) /2
            # text_y = (image_height - text_height) / 2
            draw.text(xy=(int(get_x.get()),int(get_y.get())) ,text=text, fill="white", font=font)

            photoimage = ImageTk.PhotoImage(original_image)
            image_label.config(image=photoimage)
            image_upload.image = photoimage


## Welcome Message
welcome_message = tk.Label(text="Welcome To The Aquamark Pro", font=(25,15,'bold'))
welcome_message.grid(row=0, column=1)

enter_text = tk.Label(text="Enter Your Text Here")
enter_x_loc = tk.Label(text="Enter The X value")
enter_y_loc = tk.Label(text='Enter Y Value')

## Show the input label
text_input.grid(row=1, column=1)
get_x.grid(row=2,column=1)
get_y.grid(row=3,column=1)
enter_text.grid(row=1, column=0)
enter_x_loc.grid(row=2, column=0)
enter_y_loc.grid(row=3, column=0)
## Show Preview Image
image_label = tk.Label(window)
image_label.grid(row=4, column=1)
## Image uplaod button
image_upload = tk.Button(text="Upload you image here", command=open_file)
image_upload.grid(row=5, column=1)

update_image = tk.Button(text="Update", command=open_file)
update_image.grid(row=5, column=2)


window.mainloop()