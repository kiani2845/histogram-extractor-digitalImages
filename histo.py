#by hamed kiani
import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# خواندن تصویر
def open_image():
    # باز کردن دیالوگ فایل برای انتخاب تصویر
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # خواندن تصویر
        img = cv2.imread(file_path, 0)
        
        # نمایش تصویر در رابط کاربری
        img_cv = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img_pil = Image.fromarray(img_cv)
        img_tk = ImageTk.PhotoImage(image=img_pil)
        img_label.config(image=img_tk)
        img_label.image = img_tk
        
        # محاسبه و نمایش هیستوگرام
        histr = cv2.calcHist([img], [0], None, [256], [0, 256])
        ax.clear()
        ax.plot(histr)
        ax.set_title('Image Histogram')
        ax.set_xlabel('Image Pixle')
        ax.set_ylabel('Ferequency')
        canvas.draw()


# ایجاد پنجره
root = tk.Tk()
root.title("نمایش تصویر و هیستوگرام")

# دکمه برای باز کردن تصویر
open_button = tk.Button(root, text="باز کردن تصویر", command=open_image)
open_button.pack()

# برچسب برای نمایش تصویر
img_label = tk.Label(root)
img_label.pack()

# نمایش هیستوگرام
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# شروع برنامه
root.mainloop()