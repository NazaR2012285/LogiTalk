from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x500")

image = Image.open('0-02-05-6976c656d0997fbc35ca8d91d033322789871884f842ea2ad5a7a10a57ddf424_655415ffe7a0fb89')
image_ctk = CTkImage(light_image=image,
                     size = (1000,1000))

label = CTkLabel(app, image=image_ctk,
                 compound='center',
                 text=''
                )


label.pack()


app.mainloop()