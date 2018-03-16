import Tkinter
from Tkinter import *
top = Tkinter.Tk()


def send_data():      
    
    addr = Entry1.get()
    print(addr)
    
    quant = Scale1.get()
    print(quant)
    



top.geometry("600x753+703+110")
top.title("New Toplevel 1")
top.configure(background="#7e5169")
top.configure(highlightbackground="#d92b74")
top.configure(highlightcolor="black")

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#d9d9d9' # X11 color: 'gray85' 
font10 = "-family {DejaVu Sans} -size 20 -weight normal -slant"  \
  " roman -underline 0 -overstrike 0"
font11 = "-family {DejaVu Sans} -size 15 -weight bold -slant "  \
  "roman -underline 0 -overstrike 0"
font9 = "-family {DejaVu Sans} -size 10 -weight normal -slant "  \
  "roman -underline 0 -overstrike 0"
  
  
  
  
Button1 = Button(top)
Button1.place(relx=0.18, rely=0.73, height=150, width=377)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(background="#78d9d9")
Button1.configure(disabledforeground="#00a3a3")
Button1.configure(font=font11)
Button1.configure(foreground="#640050")
Button1.configure(highlightbackground="#00c9d9")
Button1.configure(padx="1m")
Button1.configure(text='''SEND''')
Button1.configure(command=send_data)



Entry1 = Entry(top)
Entry1.place(relx=0.07, rely=0.12,height=180, relwidth=0.86)
Entry1.configure(background="white")
Entry1.configure(font="font9")
Entry1.configure(selectbackground="#c4c4c4")



ADDRESS = Label(top)
ADDRESS.place(relx=0.32, rely=0.04, height=38, width=226)
ADDRESS.configure(activebackground="#f9f9f9")
ADDRESS.configure(font=font9)
ADDRESS.configure(text='''ADDRESS''')



Scale1 = Scale(top)
Scale1.place(relx=0.08, rely=0.49, relwidth=0.85, relheight=0.0
      , height=132)
Scale1.configure(activebackground="#d9d9d9")
Scale1.configure(borderwidth="5")
Scale1.configure(font=font10)
Scale1.configure(foreground="#960000")
Scale1.configure(highlightcolor="#000069")
Scale1.configure(length="500")
Scale1.configure(orient="horizontal")
Scale1.configure(relief=RIDGE)
Scale1.configure(sliderlength="50")
Scale1.configure(tickinterval="1.0")
Scale1.configure(to="10.0")
Scale1.configure(troughcolor="#00404b")
Scale1.configure(width=50)



ADDRESS1 = Label(top)
ADDRESS1.place(relx=0.3, rely=0.41, height=38, width=226)
ADDRESS1.configure(activebackground="#f9f9f9")
ADDRESS1.configure(font=font9)
ADDRESS1.configure(text='''QUANTITY''')



top.mainloop()
