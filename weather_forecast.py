# Weather forecast
import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

# Define window
root = tkinter.Tk()
root.title('Weather forecast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0, 0)

#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun', 14)
small_font = ('Simsun', 10)

#Create frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
input_frame.pack(pady=15)

# Output frame layout


# Run root windows
root.mainloop()