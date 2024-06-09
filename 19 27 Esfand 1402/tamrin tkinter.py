from tkinter import *
root = Tk()
for i in range(10):
    for j in range(10):
        Button(root, text=i*10+j, font=('', 28), bg='black', fg='white').place(x=j*60, y=i*60, width=60, height=60)
root.mainloop()