import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk, ImageDraw, ImageFont
# Constant 
ORIGINAl_IMAGE = None

## Define the tkinter 
window = tk.Tk()
window.geometry("800x700")

## Title Of the Project
window.title("Aquamark Pro")

# Get inputs from user
text_input = tk.Entry()
type = type(text_input)
get_x = tk.Entry()
get_y = tk.Entry()
get_text_color = tk.Entry()
def open_file():
    file = filedialog.askopenfilename()
    global ORIGINA_IMAGE
    if file:
        with open(file, 'rb') as file:
            ORIGINAl_IMAGE = Image.open(file)
            max_width = 400
            max_height = 300
            ORIGINAl_IMAGE.thumbnail((max_width,max_height))
            photoimage = ImageTk.PhotoImage(ORIGINAl_IMAGE)

            draw = ImageDraw.Draw(ORIGINAl_IMAGE)
            
            text= text_input.get()
            font = ImageFont.truetype("arial.ttf", size=35)
            draw.text(xy=(int(get_x.get()),int(get_y.get())) ,text=text, fill=get_text_color.get(), font=font)

            photoimage = ImageTk.PhotoImage(ORIGINAl_IMAGE)
            image_label.config(image=photoimage)
            image_upload.image = photoimage
            return ORIGINAl_IMAGE
def save_file():
    global ORIGINAl_IMAGE
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
    if file_path:
        ORIGINAl_IMAGE.save(file_path)
        saved_message.config(text="Watermarked Image Saved Successfull")

## Welcome Message
welcome_message = tk.Label(text="Welcome To The Aquamark Pro", font=(25,15,'bold'))
welcome_message.grid(row=0, column=1)

enter_text = tk.Label(text="Enter Your Text Here")
enter_x_loc = tk.Label(text="Enter The X value")
enter_y_loc = tk.Label(text='Enter Y Value')
enter_text_color = tk.Label(text="Enter The Color Of The Text")
saved_message = tk.Label()
## Show the input label
text_input.grid(row=1, column=1)
get_x.grid(row=2,column=1)
get_y.grid(row=3,column=1)
get_text_color.grid(row=4,column=1)
enter_text.grid(row=1, column=0)
enter_x_loc.grid(row=2, column=0)
enter_y_loc.grid(row=3, column=0)
enter_text_color.grid(row=4, column=0)
## Show Preview Image
image_label = tk.Label(window)
image_label.grid(row=5, column=1)
## Image uplaod button
image_upload = tk.Button(text="Upload you image here", command=open_file)
image_upload.grid(row=6, column=1)

save_image = tk.Button(text="Save", command=save_file)
save_image.grid(row=6, column=2)

saved_message.grid(row=7,column=1)


window.mainloop()