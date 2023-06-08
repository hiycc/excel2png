import tkinter as tk
from tkinter import filedialog

def browse_file():
    filepath = filedialog.askopenfilename()
    print(filepath)

root = tk.Tk()
root.title("文件上传GUI")

button = tk.Button(root, text="上传文件", command=browse_file)
button.pack()

root.mainloop()
