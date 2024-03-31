from tkinter import Tk
from PIL import Image, ImageTk
root = Tk()

# raveshe 1 ke faghat file haye ico ro mitoone.
# root.iconbitmap("c.ico")

# raveshe 2 ke file haye png ro mikhoone. vali khode ico ro nemitoone.
# photo = PhotoImage(file = 'c.png')
# root.iconphoto(False, photo)

# raveshe 3 ke ba pillow hast va kheyli az format ha ro poshtibani mikone.
# ico = Image.open('c.png')
# ico = Image.open('c.ico')
# ico = Image.open('b.jpg')
ico = Image.open('pypi.png')
photo = ImageTk.PhotoImage(ico)
root.iconphoto(False, photo)

root.mainloop()