import time, os
from tkinter import *
from tkinter.font import Font

if os.path.isfile('init.txt'):
    save = list(open('init.txt', 'r'))
    for i in range(len(save)): save[i] = save[i].replace('\n', '')
    
else:
    save, writer = ['0', '0', '#FFFFFE'], open('init.txt', 'w')
    [writer.write(i+'\n') for i in save]
    writer.close()

def configure(event):
    def updatetimer():
        try:
            if len(colorInput.get()) == 7:
                bc = list(colorInput.get().upper())
                alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
                try:
                    bc[6] = 'E' if bc[6]=='F' else alphabet[alphabet.index(bc[6])+1] if alphabet.index(bc[6]) < len(alphabet)-1 else bc[6]
                except: bc[6] = str(int(bc[6])+1) if int(bc[6]) < 9 else '0' if int(bc[6]) == 9 else bc[6]

                bc = ''.join(bc)
                try:
                    labeltime.update()
                    labeltime.config(fg=colorInput.get(), bg=bc)
                    labeldate.update()
                    labeldate.config(fg=colorInput.get(), bg=bc)
                    am.config(fg=colorInput.get(), bg=bc)
                    pm.config(fg=colorInput.get(), bg=bc)
                    root.config(bg=bc)
                    root.wm_attributes("-transparentcolor", bc)
                    root.update()
                except:
                    pass
        except:
            pass
        
        labeldate.config(text=formatdate())
        labeltime.config(text=formattime())
        labeltime.update()
        labeldate.update()   
        root.geometry("556x180+"+str(xposbar.get())+'+'+str(yposbar.get()))

    def Done():
        global save
        save[0], save[1], save[2] = xposbar.get(), yposbar.get(), colorInput.get()
        writer = open('init.txt', 'w')
        [writer.write(str(i).upper()+'\n') for i in save]
        writer.close()
        conwin.destroy()
        looplol()
    
    conwin = Tk()
    conwin.geometry('500x200+500+500')
    conwin.config(bg='white')
    conwin.title('config')
    conwin.iconbitmap('icon.ico')

    labelfont = Font(size=15, family='Bahnschrift')
    entryfont = Font(size=15, family='Bahnschrift')
    okfont = Font(size=30, family='Bahnschrift SemiBold')
    
    colorLabel = Label(conwin, text='color: ', bg='white', font=labelfont)
    colorInput = Entry(conwin, font=entryfont, relief=FLAT, highlightbackground='black', width=9, highlightcolor='black', highlightthickness=2, justify=CENTER)
    colorshow = Canvas(conwin, height=20, width=20, highlightbackground='black')
    colorLabel.place(x=52, y=20)
    colorInput.place(x=100, y=20)
    colorshow.place(x=200, y=20)
    
    colorInput.insert(END,save[2])

    xposl = Label(conwin, text='x position: ', bg='white', font=labelfont)
    xposbar = Scale(conwin, orient=HORIZONTAL, bg='white', borderwidth=0, highlightthickness=2 , highlightbackground='black', sliderrelief=FLAT, fg='black', length=350, to=1920, showvalue=0)
    yposl = Label(conwin, text='y position: ', bg='white', font=labelfont)
    yposbar = Scale(conwin, orient=HORIZONTAL, bg='white', borderwidth=0, highlightthickness=2, length=350, to=1080, showvalue=0 , highlightbackground='black', sliderrelief=FLAT,)

    xposbar.set(save[0])
    yposbar.set(save[1])

    
    xposl.place(x=20, y=60)
    yposl.place(x=20, y=100)
    
    xposbar.place(x=100, y=62.5)
    yposbar.place(x=100, y=102.5)
    okbtnframe = Frame(conwin, height=36, width=79, bg='black')
    OKButton = Button(conwin, text='OK', command=Done, padx=20, relief=FLAT, font=okfont)
    okbtnframe.place(x=210.5, y=148)
    OKButton.place(x=212.5, y=150)
    
    while True:
        try:
            try:
                if len(colorInput.get())==7:
                    colorshow.config(bg=colorInput.get())
                    colorshow.update()
                    updatetimer()
                else:
                    colorshow.update()
                    updatetimer()
            except:
                colorshow.update()
                updatetimer()
        except:
            try:
                updatetimer()
            except:
                pass
def key_pressed(event):
    root.destroy()
    quit()
    
def formattime():
    global ampm
    ctime = time.localtime(time.time())
    minute = ctime.tm_min
    minute = '0'+str(ctime.tm_min) if minute < 10 else minute
    if ctime.tm_hour < 12:
        return str(ctime.tm_hour)+':'+str(minute)+'AM'
    elif ctime.tm_hour == 12:
        return str(ctime.tm_hour)+':'+str(minute)+'PM'
    else:
        return str(ctime.tm_hour-12)+':'+str(minute)+'PM'

def formatdate():
    ctime = time.localtime(time.time())
    wdaylst, monthlst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    wday, month = wdaylst[ctime.tm_wday], monthlst[ctime.tm_mon-1]
    return '- '+wday+' '+str(ctime.tm_mday)+' '+month+' '+str(ctime.tm_year)+' -'

root = Tk()
timefont = Font(size=70, family='Bahnschrift SemiLight Condensed')
datefont = Font(size=20, family='Bahnschrift Light')
labeltime = Label(root, text=formattime(), bg='white', font=timefont, fg=str(save[2]))
labeldate = Label(root, text=formatdate(), bg='white', font=datefont, fg=str(save[2]))
root.overrideredirect(True)
rootxpad=int(save[0])
rootypad=int(save[1])
root.geometry("556x180+"+str(rootxpad)+'+'+str(rootypad))
root.config(bg='white')
root.wm_attributes("-transparentcolor", "white")
root.bind("<F12>", key_pressed)
root.bind("<F9>", configure)
labeltime.place(x=250, y=50, anchor='center')
labeldate.place(x=250, y=120, anchor='center')

try:
    if len(save[2]) == 7:
        bc = list(save[2])
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
        try:
            bc[6] = 'E' if bc[6]=='F' else alphabet[alphabet.index(bc[6])+1] if alphabet.index(bc[6]) < len(alphabet)-1 else bc[6]
        except: bc[6] = str(int(bc[6])+1) if int(bc[6]) < 9 else '0' if int(bc[6]) == 9 else bc[6]

        bc = ''.join(bc)
        try:
            labeltime.update()
            labeltime.config(fg=save[2], bg=bc)
            labeldate.update()
            labeldate.config(fg=save[2], bg=bc)
            am.config(fg=save[2], bg=bc)
            pm.config(fg=save[2], bg=bc)
            root.config(bg=bc)
            root.wm_attributes("-transparentcolor", bc)
            root.update()
        except:
            pass
except:
    pass

def looplol():
    while True:
        try:
            labeltime.update()
            labeltime.config(text=formattime())
            labeldate.update()
            labeldate.config(text=formatdate())
        except:
            quit()

looplol()

quit()
