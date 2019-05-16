from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Main import Main


root = Tk()
root.title("Carpooling Pick-Up")
root.resizable(False, False)
root.iconbitmap("./interfaceImages/icon.ico")
root.geometry("650x550")
root.config(bg="#31CABF")
root.config(relief="groove")
root.config(bd=15)

"""menuBar = Menu(root)
root.config(menu=menuBar)

helpOption = Menu(menuBar, tearoff=0)
helpOption.add_command(label="About Carpooling")
helpOption.add_command(label="Maps info")

menuBar.add_cascade(label="Help", menu=helpOption)"""

frame = Frame()
frame.pack(fill="both", expand="True")
frame.config(bg="#1DA79E")

icon = PhotoImage(file="./interfaceImages/imageIcon.png")
Label(frame, image=icon, bg="#1DA79E").grid(row=0, column=1, padx=10, pady=10, sticky="n")
Label(frame, text="Be Supportive", fg="white", bg="#1DA79E", font=("Times New Roman", 18)).grid(row=0, column=1, padx=10, pady=10)
Label(frame, text="Carpooling Pick-Up", fg="white", bg="#1DA79E", font=("Times New Roman", 25)).grid(row=0, column=0, padx=10, pady=10, sticky="n")


Label(frame, text="What do you want to do?", fg="white", bg="#1DA79E", font=("Times New Roman", 15)).place(x=185, y=230)
buttonRun = Button(frame, text="Run a file", bd=10, bg="white", fg="#1DA79E", font=("Times New Roman", 20), command=lambda:runAFile())    
buttonRun.place(x=230, y=300)
buttonExit = Button(frame, text="Exit", bd=10, bg="white", fg="#1DA79E", font=("Times New Roman", 20), command=lambda:exitRun())    
buttonExit.place(x=265, y=400)

def runAFile():
    frame.destroy()
    
    frame2 = Frame()
    frame2.pack(fill="both", expand="True")
    frame2.config(bg="#1DA79E")
    
    Label(frame2, image=icon, bg="#1DA79E").grid(row=0, column=1, padx=10, pady=10, sticky="n")
    Label(frame2, text="Be Supportive", fg="white", bg="#1DA79E", font=("Times New Roman", 18)).grid(row=0, column=1, padx=10, pady=10)
    Label(frame2, text="Carpooling Pick-Up", fg="white", bg="#1DA79E", font=("Times New Roman", 25)).grid(row=0, column=0, padx=10, pady=10, sticky="n")
    
    fileName = StringVar()  
    type1 = BooleanVar()
    type2 = BooleanVar()
    type3 = BooleanVar()    
          
    Label(frame2, text="Insert a file name", fg="white", bg="#1DA79E", font=("Times New Roman", 18)).place(x=30, y=220)
    fileEntry = Entry(frame2, textvariable=fileName)
    fileEntry.place(x=30, y=265)
    fileEntry.config(bg="white", fg="black", font=("Times New Roman", 15))
    ButtonRunFile = Button(frame2, text="Run", bd=10, bg="white", fg="#1DA79E", font=("Times New Roman", 15), command=lambda:run(fileName.get(), type1.get(), type2.get(), type3.get()))
    ButtonRunFile.place(x=300, y=250)
    Label(frame2, text="Or...", fg="white", bg="#1DA79E", font=("Times New Roman", 18)).place(x=30, y=320)
    ButtonOpenFile = Button(frame2, text="Open file", bd=10, bg="white", fg="#1DA79E", font=("Times New Roman", 15), command=lambda:openFile(type1.get(), type2.get(), type3.get()))
    ButtonOpenFile.place(x=140, y=360)
    Label(frame2, text="Select a map type: ", fg="white", bg="#1DA79E", font=("Times New Roman", 18)).place(x=350, y=320)
    Checkbutton(frame2, text="Type 1", fg="white", bg="#1DA79E", font=("Times New Roman", 15), variable=type1, onvalue=1, offvalue=0, command=lambda:test(type1, type2, type3)).place(x=370, y=370)
    Checkbutton(frame2, text="Type 2", fg="white", bg="#1DA79E", font=("Times New Roman", 15), variable=type2, onvalue=True, offvalue=False, command=lambda:test(type1, type2, type3)).place(x=370, y=410)
    Checkbutton(frame2, text="Type 3", fg="white", bg="#1DA79E", font=("Times New Roman", 15), variable=type3, onvalue=True, offvalue=False, command=lambda:test(type1, type2, type3)).place(x=370, y=450)
    buttonExitFrame2 = Button(frame2, text="Exit", bd=10, bg="white", fg="#1DA79E", font=("Times New Roman", 15), command=lambda:exitRun())    
    buttonExitFrame2.place(x=165, y=440)
    

def test(type1, type2, type3):
    print("type 1: "+ str(type1.get()))
    print("type 2: "+ str(type2.get()))
    print("type 3: "+ str(type3.get()))
    
def openFile(type1, type2, type3):
    if type1 is False and type2 is False and type3 is False:
        messagebox.showerror("Error", "you must select at least one type of map")
    else:     
        fileName = filedialog.askopenfilename(title="Open File", initialdir="./dataSets/")
        nCars = ""
        fileList = list(fileName)
        for i in range(76, 79):
            if fileList[i] != '-' and fileList[i] != 'p' and fileList[i] != '=':
                nCars += fileList[i]
        
        main = Main()
        main.main(fileName, int(nCars), type1, type2, type3)
        messagebox.showinfo("Answer", "Answer for p = " + str(main.getP()) + " is: "+str(main.getTotalNumberOfCars()))

def run(fileName, type1, type2, type3):
    if type1 is False and type2 is False and type3 is False:
        messagebox.showerror("Error", "you must select at least one type of map")
    else: 
        nCars = ""
        fileList = list(fileName)
        for i in range(28, 32):
            if fileList[i] != '-' and fileList[i] != 'p' and fileList[i] != '=':
                nCars += fileList[i]
        
        print(nCars)
        main = Main()
        main.main(fileName, int(nCars), type1, type2, type3)
        messagebox.showinfo("Answer", "Answer for p = " + str(main.getP()) + " is: "+str(main.getTotalNumberOfCars()))
    
def exitRun():
    answer = messagebox.askokcancel("Exit", "Ey!, are you sure about this?")
    if answer == True:
        root.destroy()

root.mainloop()