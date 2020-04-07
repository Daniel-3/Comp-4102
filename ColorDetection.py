import Tkinter
import argparse
from PIL import Image, ImageTk
from sys import argv
import pandas as pd
import tkMessageBox
#an application through which you can automatically get the name
# of the color by clicking on them.  W
class Display:
    def __init__(self,fileName):
        self.window = Tkinter.Tk(className=" Color Detection")
        self.image = Image.open(fileName)
        self.canvas = Tkinter.Canvas(self.window, width=self.image.size[0], height=self.image.size[1])
        self.canvas.pack()
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(self.image.size[0]//2, self.image.size[1]//2,image=self.image_tk)
        self.canvas.bind("<Double-Button-1>", self.callback)
        # Read the CSV file with pandas:
        self.colors=pd.read_csv("colors.csv")
        Tkinter.mainloop()
    #Set a mouse callback event on a window:
    def callback(self,event):
        pixel=self.draw("doubleClick",event.x, event.y)
        colorName=""
        maxDistance=10000000000000
        #
        for index, row in self.colors.iterrows():
            currentDistance=self.distance(pixel,(row['r'],row['g'],row['b']))
            if(maxDistance>currentDistance):
                maxDistance = currentDistance
                colorName=row['Color']
        tkMessageBox.showinfo("Color", colorName)
    #
    def distance(self, color1,color2):
        return abs(color1[0]-color2[0])+abs(color1[1]-color2[1])+abs(color1[2]-color2[2])
    #  It will calculate the rgb values of the pixel which we double click.
    # The function parameters have the event name, (x,y) coordinates of the mouse
    # position, etc
    def draw(self,eventName,x,y):
        if(eventName=="doubleClick"):
            return self.image.getpixel((x,y))
        else:
            return (-1,-1,-1)



#
parser = argparse.ArgumentParser()
parser.add_argument("image")
args = parser.parse_args()
display=Display(args.image)
