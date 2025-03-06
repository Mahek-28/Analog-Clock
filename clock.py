from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
class Clock:
    def __init__(self,root):
       self.root=root
       self.root.title("GUI Analog Clock")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="#021e2f")
       title=Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)

       self.lbl=Label(self.root,bg="white",bd=10,relief=RAISED)
       self.lbl.place(x=450,y=150,height=400,width=400)
    #  self.clock_image()
       self.working()

    def clock_image(self,hr,min_,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        #=====For Clock Image
        bg=Image.open("clock.png")
        bg=bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))
        # Formula To Rotate the Clock
        # angle_in_radius = angle_in_degrees * math.pi/ 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x - line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)
        #=====Hour Line Image
        origin=200,200
        draw.line((origin,200+35*sin(radians(hr)),200-35*cos(radians(hr))),fill="black",width=4)    
        #=====Minute Line Image
        draw.line((origin,200+55*sin(radians(min_)),200-55*cos(radians(min_))),fill="blue",width=3)
        #=====Second Line Image
        draw.line((origin,200+70*sin(radians(sec)),200-70*cos(radians(sec))),fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")
    
    def working(self):
        h=datetime.now().hour
        m=datetime.now().minute
        s=datetime.now().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec)
        self.clock_image(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
root=Tk()
obj=Clock(root)
root.mainloop()