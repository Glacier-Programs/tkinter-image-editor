import tkinter as tk

screen = tk.Tk()
screen.title('Images')
screen.geometry('800x810')

canvas = tk.Canvas(screen,height=790,width=800,bg='white')
canvas.pack()

def Open():
    try:
        file = entry.get()
        file = open(file,'r')
        file.seek(0)
        length = int(file.readline())
        for i in range(1,length+1):
            line = file.readline(i)
            lineData = line.split()
            
    except FileNotFoundError:
        canvas.create_text(400,400,text='FILE NOT FOUND')

frame = tk.Frame(screen)
lbl = tk.Label(frame,text='File Name')
lbl.pack(side=tk.LEFT)
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)
button = tk.Button(frame,text='Open',command=Open)
button.pack(side=tk.LEFT)
frame.pack(fill=tk.X)

screen.mainloop()