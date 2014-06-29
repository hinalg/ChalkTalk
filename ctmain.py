from Tkinter import *
import tkMessageBox
import pdb

lastx, lasty = 0, 0
startx, starty=0,0
color= "black"
shape= "line"

class Application(Frame):
    """ The standalone chalktalk appilcation."""

    def __init__(self,master):
        """Initialize the frame"""
        Frame.__init__(self,master)
        
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Empty for now"""
        #create the new recording button
        self.button1 =Button(self,text="New recording")
        self.button1["command"]= self.create_newrecording
        self.button1.grid()

        #Add audio button
        self.button2 = Button(self,text="Add audio")
        self.button2["command"]= self.add_audio
        self.button2.grid()

        #save recording
        self.button3= Button(self,text="save recording")
        self.button3["command"]= self.save_recording
        self.button3.grid()

        #Create a canvas
        self.canvas = Canvas(self,width=400,height=400,bg="white",relief=RAISED,bd=4)
        self.canvas.pack(fill="both",expand=True)
        self.canvas.grid()
        self.canvas.bind("<Button-1>",self.xy)
        #self.canvas.bind("<B1-Motion>", self.addLine)
        self.canvas.bind("<B1-ButtonRelease>", self.doneStroke)
        
        id = self.canvas.create_rectangle((10, 10, 30, 30), fill="red")
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("red"))
        id = self.canvas.create_rectangle((10, 35, 30, 55), fill="blue")
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("blue"))
        id = self.canvas.create_rectangle((10, 60, 30, 80), fill="black")
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("black"))
        
        id = self.canvas.create_rectangle((10, 85, 30, 105), fill="white")
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setShape("rectangle"))
        id = self.canvas.create_oval((10, 110, 30, 130), fill="white")
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setShape("oval"))
        id = self.canvas.create_line((10, 135, 30, 155), fill="black",width=5)
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setShape("line"))

    def setColor(self,newcolor):
        global color
        color = newcolor

    def doneStroke(self,event):
        self.canvas.itemconfigure('currentline', width=1)
        
    def setShape(self,newshape):
        global shape
        shape=newshape
        if shape=="rectangle":
            print "rect"
            self.canvas.bind("<ButtonPress-1>",self.noticestart)
            self.canvas.bind("<B1-Motion>",self.doNothing)
            self.canvas.bind("<ButtonRelease-1>",self.addRectangle)
        if shape=="oval":
            self.canvas.bind("<ButtonPress-1>",self.noticestart)
            self.canvas.bind("<B1-Motion>",self.doNothing)
            self.canvas.bind("<ButtonRelease-1>",self.addOval)
        if shape=="line":
            print "line"
            self.canvas.bind("<ButtonPress-1>",self.xy)
            self.canvas.bind("<B1-Motion>", self.addLine)
            self.canvas.bind("<ButtonRelease-1>",self.doNothing)
##        self.canvas.bind("<Button-1>",self.xy)    
        return


    def doNothing(self,event):
        pass
    
    def noticestart(self,event):
        global startx,starty
        startx, starty = event.x, event.y
        print "startx,starty:", startx, starty
        
        
    def xy(self,event):
        global lastx, lasty
        lastx, lasty = event.x, event.y
        print "updated lastx,lasty"
        
    def addLine(self,event):
        global lastx, lasty
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.canvas.create_line((lastx, lasty, x, y), fill=color, width=5)
        lastx, lasty = x, y

    def addRectangle(self,event):
        global startx,starty
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        print "x0,y0,x1,y1",startx, starty ,x , y        
        self.canvas.create_rectangle((startx, starty, x, y), fill="white", width=2)
        lastx, lasty = x, y
        
    def addOval(self,event):
        global lastx, lasty
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.canvas.create_oval((startx, starty, x, y), fill="white", width=5)
        lastx, lasty = x, y

    def save_recording(self):
        print "Here goes the code to save the recording"

    def add_audio(self):
        print "Here goes the code to add audio"

    def create_newrecording(self):
        print "Here goes the code to create a new recording"
        # first prompt warning to delete any existing drawing exists

        reply=tkMessageBox.askyesnocancel("Erase existing canvas",\
                                          "Pressing Yes will delete the existing canvas. \n Are you sure you want to create a new recording?")
        
        if reply:
            print "going to delete existing canvas"

            #set the stage to start a new recording 
            #while True:
                
        

root=Tk()
root.title("ChalkTalk")
root.geometry("500x500")

app=Application(root)
app.mainloop()
