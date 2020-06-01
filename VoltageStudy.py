import tkinter as tk
import time
class schematic_symbols:
    def __init__(self,object_type,x1,y1,boxsize,nLabel,resistance="undefinded",current="undefinded"):
        self.canvas=canvas
        self.x1=x1
        self.y1=y1
        self.boxsize=boxsize
        self.nLable=nLabel
        self.resistance=resistance
        self.current=current
        x2 = x1+boxsize
        y2 = y1+boxsize
        self.x2=x2
        self.y2=y2
        xAvg = (x1+x2)/2
        yAvg = (y1+y2)/2
        self.xAvg = xAvg
        self.yAvg = yAvg
        shrink = boxsize / 4
        u_name = canvas.create_text(x2 + 2, yAvg, text=nLabel, anchor='w')
        r_name = canvas.create_text(x2 + 2, yAvg + 10, text=resistance, anchor='w')
        c_name = canvas.create_text(x2 + 2, yAvg + 20, text=current, anchor='w')
        if object_type == "Earth":
            part1 = canvas.create_oval(x1,y1,x2,y2)
            part2 = canvas.create_line(x1,yAvg,x2,yAvg)
            part3 = canvas.create_line(xAvg,y1,xAvg,yAvg)
            line45 = boxsize/3*0.707
            shift45 = boxsize/3
            moveX = boxsize/6
            part4 = canvas.create_line(xAvg-line45-shift45+moveX,yAvg+line45,xAvg-shift45+moveX,yAvg)
            part5 = canvas.create_line(xAvg-line45+moveX,yAvg+line45,xAvg+moveX,yAvg)
            part6 = canvas.create_line(xAvg-line45+shift45+moveX,yAvg+line45,xAvg+shift45+moveX,yAvg)
            self.parts = [u_name,r_name,c_name,part1,part2,part3,part4,part5,part6]
        if object_type=="Alt":
            part1 = canvas.create_rectangle(x1, y1, x2, y2)
            part2 = canvas.create_rectangle(x1 + shrink, y1 + shrink, x2 - shrink, y2 - shrink)
            part3 = canvas.create_line(xAvg, y2 - shrink, xAvg, y2)
            self.parts = [u_name,r_name,c_name, part1,part2, part3]
        if object_type=="Bft":
            part1 = canvas.create_rectangle(x1, y1, x2, y2)
            part2 = canvas.create_line(xAvg, y1, xAvg, y2)
            self.parts = [u_name,r_name,c_name, part1,part2]
        if object_type=="Lamp":
            part1 = canvas.create_oval(x1, y1, x2, y2)
            part2 = canvas.create_line(xAvg, y1, xAvg, y1 + boxsize / 4)
            part3 = canvas.create_line(xAvg, y2 - boxsize / 4, xAvg, y2)
            part4 = canvas.create_arc(xAvg - boxsize / 8, yAvg - boxsize / 8 + boxsize / 8, xAvg + boxsize / 8,
                                      yAvg + boxsize / 8 + boxsize / 8, start=90, extent=180, style="arc")
            part5 = canvas.create_arc(xAvg - boxsize / 8, yAvg - boxsize / 8 - boxsize / 8, xAvg + boxsize / 8,
                                      yAvg + boxsize / 8 - boxsize / 8, start=270, extent=180, style="arc")
            self.parts = [u_name,c_name,r_name, part1,part2, part3, part4, part5]
        screen_objects.append(self)
    def move(self,e):
        print(e.x,e.y)
        for part in self.parts:
            canvas.move(part, e.x-self.x1, e.y-self.y1 )
        self.x1 = e.x
        self.y1 = e.y
    def rename_unit(self,e):
        print('rename unit')

    def change_resistance(self,e):
        print('reneme res')
        #new_resistance = canvas.Entry(top,'Enter resistance')
        #new_resistance.pack
        #self.resistance = new_resistance
    def change_current(self,e):
        print('rename current')
        #new_current=canvas.Entry(top,'Enter current')
        #new_current.pack
        #self.current = new_current

def create_earth():

    #unit_name = tk.Entry(canvas,width=50)
    #unit_name.pack
    #unit_name.get()
    #earth(150, 1, 25, 'Earth1')
    schematic_symbols('Earth',150,1,25,'Earth2')
def create_alt():
    #alt(100,100,25,'Alt1')
    schematic_symbols('Alt',100,100,25,'Alt2')
def create_bft():
    #bft(1,150,25,'Bft1')
    schematic_symbols('Bft',1,150,25,'Bft2')
def create_lamp():
    #lamp(150,150,25,'Lamp1')
    schematic_symbols('Lamp',150,150,25,'Lamp2')
def mouse_location(e):
    global move_box
    global connect_box
    global label_box
    global res_box
    global cur_box
    canvas.delete(move_box)
    canvas.delete(connect_box)
    canvas.delete(label_box)
    canvas.delete(res_box)
    canvas.delete(cur_box)
    for part in screen_objects:
        #print(part.nLable, part.x1, part.y1, part.boxsize)
        if part.x1 < e.x and e.x < part.x1+part.boxsize/2 and part.y1 < e.y and e.y < part.y1+part.boxsize/2:
            #print("move location")
            move_box = canvas.create_rectangle(e.x-5,e.y-5,e.x+5,e.y+5,outline="red",fill='red')
            canvas.bind('<B1-Motion>', part.move)
        if part.xAvg-2 < e.x and e.x < part.xAvg+2  and part.y1-2 < e.y and e.y < part.y1+2:
            #print("connection location")
            connect_box = canvas.create_rectangle(e.x-5,e.y-5,e.x+5,e.y+5,outline="green",fill='green')
        if part.xAvg-2 < e.x and e.x < part.xAvg+2  and part.y2-2 < e.y and e.y < part.y2+2:
            #print("connection location")
            connect_box = canvas.create_rectangle(e.x-5,e.y-5,e.x+5,e.y+5,outline="green",fill='green')
        if part.x2 < e.x and e.x < part.x2+4 and part.yAvg -2 < e.y and e.y <part.yAvg+2:
            label_box = canvas.create_rectangle(e.x - 5, e.y - 5, e.x + 5, e.y + 5, outline="green", fill='green')
            canvas.bind('<ButtonRelease-1>', part.rename_unit)
        if part.x2 < e.x and e.x < part.x2+4 and part.yAvg + 10 -2 < e.y and e.y <part.yAvg + 10 +2:
            res_box = canvas.create_rectangle(e.x - 5, e.y - 5, e.x + 5, e.y + 5, outline="green", fill='green')
            canvas.bind('<ButtonRelease-1>', part.change_resistance)
        if part.x2 < e.x and e.x < part.x2+4 and part.yAvg +20 -2 < e.y and e.y <part.yAvg + 20 +2:
            cur_box = canvas.create_rectangle(e.x - 5, e.y - 5, e.x + 5, e.y + 5, outline="green", fill='green')
            canvas.bind('<ButtonRelease-1>', part.change_current)
#u_name = canvas.create_text(x2 + 2, yAvg, text=nLabel, anchor='w')
 #       r_name = canvas.create_text(x2 + 2, yAvg + 10, text=resistance, anchor='w')
  #      c_name = canvas.create_text(x2 + 2, yAvg + 20, text=current, anchor='w')

root = tk.Tk()
label = tk.Label(root, text="Voltage Calculator")
label.pack(side='top')

frame = tk.Frame(root, width=800, height=600)

leftFrame =tk.Frame(root, width=500, height=600)
leftFrame.pack(side='left', anchor='n', fill=tk.Y, expand=True)

rightFrame =tk.Frame(root, width=500, height=600)
rightFrame.pack(side='right', anchor='n', fill=tk.Y, expand=True)

canvas=tk.Canvas(leftFrame,  relief='raised', borderwidth=1,width=500,height=600)
canvas.pack(side='left', anchor='n')

global screen_objects
screen_objects = []

move_box = canvas.create_rectangle(10,10,10,10,outline="#f11")
connect_box = canvas.create_rectangle(10,10,10,10,outline="#f11")
label_box = canvas.create_rectangle(10,10,10,10,outline="#f11")
res_box = canvas.create_rectangle(10,10,10,10,outline="#f11")
cur_box = canvas.create_rectangle(10,10,10,10,outline="#f11")

button_earth =tk.Button(rightFrame, text='Earth',command=create_earth)
button_alt =tk.Button(rightFrame, text='Alt',command=create_alt)
button_bft =tk.Button(rightFrame, text='Bft',command=create_bft)
button_lamp= tk.Button(rightFrame, text='Lamp',command=create_lamp)
buttonQuit = tk.Button(rightFrame, text='Quit', command=root.destroy)

button_earth.pack(side='top')
button_alt.pack(side='top')
button_bft.pack(side='top')
button_lamp.pack(side='top')
buttonQuit.pack(side='top')

canvas.bind('<Motion>', mouse_location)
canvas.bind()

root.mainloop()