import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog 
import tkinter 
from Transformations import * 
import math
import tksheet
import geopandas 
from PIL import ImageTk, Image

def GUIWindow():
    root = Tk()
    j="Graphic User Interface"
    root.title(j)
    root.iconbitmap("./relaxing-cat.ico")
    root.geometry('1200x600')
    root.resizable(False,0)

    #asdsda = tkinter.Label(root, text="Designated Path").grid(column=0,row=2)
    PathText = Entry(root, width=450,borderwidth=3,state=NORMAL)
    PathText.grid(padx=15,pady=10,column=1,row=1,columnspan=3)
    PathText.insert(0,"(Input coordinates file path)")
    PathText.config(state="readonly")
    def Transform(SelectedButton):
        global SelectedFunction
        global NewPoints
        global TransformFun
        if SelectedButton == 1:
            print("1")
            NewPoints= Help()
        elif SelectedButton==2:
            print("2")
            NewPoints= Translation(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints    
        elif SelectedButton==3:
            print("3")
            NewPoints= Rotation(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==4:
            print("4")
            NewPoints= Scale(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==5:
            print("5")
            NewPoints= Similarity(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==6:
            print("6")
            NewPoints= Affine(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==7:
            print("7")
            NewPoints= Projected(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==8:
            print("8")
            NewPoints= EuclideanDistance(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        elif SelectedButton==9:
            print("9")
            NewPoints= AverageXY(Points)
            TransformFun=NewPoints[1]
            NewPoints=NewPoints[0]
            print(TransformFun)
            print(Points[1:])
            print(NewPoints[1:])
            return NewPoints
        else:
            print("Error, the script sucks!")
        #mylabel1 = Label(root, text=SelectedButton).grid()



     
    global SelectedFunction

    def Checked(value):
        #mylabel = Label(root, text=value).grid(column=1,row=3)
        global SelectedFunction
        global SelectedButton
        if value == 1:
            SelectedButton=1
            print("1")
            return SelectedButton
        elif value==2:
            SelectedButton=2
            print("2")
            return SelectedButton
        elif value==3:
            SelectedButton=3
            print("3")
            return SelectedButton
        elif value==4:
            SelectedButton=4
            print("4")
            return SelectedButton
        elif value==5:
            SelectedButton=5
            print("5")
            return SelectedButton
        elif value==6:
            SelectedButton=6
            print("6")
            return SelectedButton
        elif value==7:
            SelectedButton=7
            print("7")
            return SelectedButton
        elif value==8:
            SelectedButton=8
            print("8")
            return SelectedButton
        elif value==9:
            SelectedButton=9
            print("9")
            return SelectedButton
        else:
            print("Error, the script sucks!")
    
    global SelectedButton

    
    def OpenFileManually():
        FilePath="null"
        FilePath = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("ASCII type files", "*.txt;*.doc;*.docx")], 
        )
        print(type(FilePath))
        print(FilePath)

        data=open(FilePath,"r")
        global Points
        Points=[]
        for i in data:
            x=i.split(" ")
            Points.append(x)
        del i 
        data.close()
        for i in range(1,len(Points)):
            Points[i][0]=int(Points[i][0])
            Points[i][1]=float(Points[i][1])
            Points[i][2]=float(Points[i][2])
        del i
        PathText.config(state="normal")
        PathText.delete(0, tkinter.END)
        PathText.insert(0,FilePath)
        PathText.config(state="readonly")
    global Points
    

#    def CreateTXT(NewPoints,TransformFun):
#        print(TransformFun)
#        print(NewPoints)    
    def CreateTXT(TransformFun,NewPoints):
        file=open("Point_Data_"+TransformFun+".txt","w")
        file.write("id X(m) Y(m)\n")
        for i in range(1,len(NewPoints)):
            file.write(str(NewPoints[i][0])+" "+str("%.2f" %NewPoints[i][1])+" "+str("%.2f"  %NewPoints[i][2])+"\n")
        del i 
        file.write("\nEND")
        file.close
        print("file Successfully Created")
        tkinter.Label(root, text="  File Created Successfully  ").grid(column=1,row=21)
        return
    
    
    def ListInBox(NewPoints):
        Listroot = Tk()
        j="Transformed Points"
        Listroot.title(j)
        Listroot.iconbitmap("./relaxing-cat.ico")
        Listroot.geometry('450x450')
        Listroot.resizable(0,0)
        NewPointsSheet = tksheet.Sheet(Listroot)
        NewPointsSheet.grid(rowspan=200)
        NewPointsSheet.enable_bindings(("single_select",
                           "row_select",
                           "column_width_resize",
                           "arrowkeys",
                           "right_click_popup_menu",
                           "rc_select",
                           #"rc_insert_row",
                           #"rc_delete_row",
                           "copy",
                           #"cut",
                           #"paste",
                           #"delete",
                           #"undo",
                           #"edit_cell"
                           ))
        
        NewPointsSheet.set_sheet_data(NewPoints) 
        tkinter.Label(root, text="Points Printed Successfully").grid(column=1,row=21)

        Listroot.mainloop()


    def PointsPlotting(Points,NewPoints,TransformFun):
        #Plotroot = Tk()
        #j="Broken Dreams"
        #Plotroot.title(j)
        #Plotroot.iconbitmap("./relaxing-cat.ico")
        #Plotroot.geometry('750x300')
        #Plotroot.resizable(0,0)
        #tkinter.Label(Plotroot, text="I couldn't make it work :( \n Check the command prompt",font=("sans 40"),fg="#000000").pack(pady=70)
        #Plotroot.mainloop()  
                
        ShapefilePath = "./Shapefile/periphereies.shp" ##################################################################################### The name of the shapefile can be changed here. 
        gdf = geopandas.read_file(ShapefilePath)
        fig, ax = plt.subplots()
        gdf.plot(ax=ax,color="#8F8F8F",)
        for i in range(1,len(Points)):
            plt.plot(Points[i][1],Points[i][2],"+",color="#0000FF")
            plt.plot(NewPoints[i][1],NewPoints[i][2],"+",color="#FF0000")
        del i
        plt.legend(["Initial","Transformed"])
        plt.title("Greek Grid: 2100",fontdict = {"family":"fantasy","color":"#101099","size":20});
        font = {"family":"sans","color":"#040404","size":11}
        plt.xlabel("X (m)",fontdict = font);
        plt.ylabel("Y (m)",fontdict = font)
        plt.grid(color="#4E4E4E")
        
        FigCoor = plt.gcf()
        
        plt.show()
        plt.draw()
        
        FigurePath = "Figure_"+TransformFun+".png"
        FigCoor.savefig(FigurePath, dpi =300)

        #frame = tkinter.Frame(Plotroot, width=100, height=100)
        #frame.pack()
        #frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        #img = ImageTk.PhotoImage(Image.open("Output1.jpg"))
        #print(type(img))
        #photo = PhotoImage("Output1.jpg")
        #print(type(photo))
        #img1 = ImageTk.getimage( photo )
        img1=Image.open(FigurePath)
        img1.show()
                # Create a Label Widget to display the text or Image
        #label = tkinter.Label(Plotroot, image = img1)
        #label.pack()
        tkinter.Label(root, text="Points Plotted Successfully").grid(column=1,row=21)
        
      








    # Clear any existing items in the listbox
        #NewPointsBoxEntry.delete(0, tkinter.END)

    # Get the list from the entry widget and split it into elements
        #items = NewPointsBoxEntry.get().split(',')

    # Insert each item into the listbox
        #for item in items:
            #NewPointsBoxEntry.insert(tkinter.END, item)
        #print(NewPoints)





    Label(root,text="   Favicon by: https://www.freecatphotoapp.com/").grid(column=0,row=0)
    TransformBut = Button(root, text = "TRANSFORM" ,fg = "blue",bg="#FFAAAA" ,font=('sans 20'),command=lambda: Transform(SelectedButton),height=2,width=15).grid(column=1,row=0,padx=0,pady=20)#(column=2, row=0) 
    open_button = Button(root, text="Open ASCII File", command=OpenFileManually).grid(column=0,row=1,padx=0,pady=0)
    CoorType = tkinter.Label(root, text="Choose Designated Transformation:").grid(column=0,row=4,padx=20)
    global radioVar
    RadioVar = IntVar()
    RadioVar.set(1)
    RadioHelp = Radiobutton(root, text="Help            ",command=lambda: Checked(RadioVar.get()),value=1, variable=RadioVar).grid(column=0,row=5,padx=4,pady=0)
    RadioTranslations = Radiobutton(root, text="Translation ",command=lambda: Checked(RadioVar.get()),value=2, variable=RadioVar).grid(column=0,row=6,padx=0,pady=0)
    RadioRotations = Radiobutton(root, text="Rotation      ",command=lambda: Checked(RadioVar.get()),value=3, variable=RadioVar).grid(column=0,row=7,padx=0,pady=0)
    RadioDilations = Radiobutton(root, text="Scale             ",command=lambda: Checked(RadioVar.get()),value=4, variable=RadioVar).grid(column=0,row=8,padx=0,pady=0)
    RadioShearing = Radiobutton(root, text="Similarity      ",command=lambda: Checked(RadioVar.get()),value=5, variable=RadioVar).grid(column=0,row=9,padx=0,pady=0)
    RadioAffine = Radiobutton(root, text="Affine             ",command=lambda: Checked(RadioVar.get()),value=6, variable=RadioVar).grid(column=0,row=10,padx=0,pady=0)
    RadioReflections = Radiobutton(root, text="Projected       ",command=lambda: Checked(RadioVar.get()),value=7, variable=RadioVar).grid(column=0,row=11,padx=0,pady=0)
    #RadioEuclidean = Radiobutton(root, text="Euclidead Distance",command=lambda: Checked(RadioVar.get()),value=8, variable=RadioVar).grid(column=0,row=12,padx=0,pady=0)
    #RadioAverage = Radiobutton(root, text="Average X & Y",command=lambda: Checked(RadioVar.get()),value=9, variable=RadioVar).grid(column=0,row=13,padx=0,pady=0)
    #Radio = Radiobutton(root, text="asd",command=clicked).grid(column=0,row=14,padx=4,pady=0)
    ShowNewPoints = Button(root, text = "Show Transformed Points",command=lambda: ListInBox(NewPoints),fg = "#FFFFFF",bg="#000000" ,font=("sans 15")).grid(column=1,row=18,padx=0,pady=5)
    PlotNewPoints = Button(root, text = "Download & Open Image of Transformed Points",command=lambda: PointsPlotting(Points,NewPoints,TransformFun),fg = "#FFFFFF",bg="#000000" ,font=("sans 15")).grid(column=1,row=19,padx=0,pady=5)
    NewTXT = Button(root, text = "Create .txt File",fg = "#FFFF00",bg="#246DFF",font=("sans 15"), command =lambda: CreateTXT(TransformFun,NewPoints)).grid(column=1,row=20,padx=0,pady=10)
    tkinter.Label(root, text="Porjected Coordinate System: Greek Grid (2100)",fg = "#444444").grid(column =0,row = 30 ,pady=30) 
    #CAUTION!!! entering a very large number of rows may crash the programme
    #NewPointsBox = tkinter.Text(root).grid(column=1,row=2,rowspan=500)
    NewPointsBoxEntry = Entry(root, width=450,borderwidth=3,state=NORMAL)
    #NewPointsBoxEntry.grid(column=1,row=3,rowspan=5)
    NewPointsBoxEntry.insert(0," ") 
    #global RadioVar
    #NewPointsSheet = tksheet.Sheet(root)
    #Label(root, text="Transformed Coordinates").grid(column=1,row=29)
    #NewPointsSheet.grid(column=1,row=30)
    #NewPointsSheet.set_sheet_data("")
    #NewPointsSheet.enable_bindings(("single_select",
    #                   "row_select",
    #                   "column_width_resize",
    #                   "arrowkeys",
    #                   "right_click_popup_menu",
    #                   "rc_select",
    #                   "rc_insert_row",
    #                   "rc_delete_row",
    #                   "copy",
    #                   "cut",
    #                   "paste",
    #                   "delete",
    #                   "undo",
    #                   "edit_cell"))

    root.mainloop()


#C:\Users\User\AppData\Local\Temp\tmpy9_fuj7t.PNG


GUIWindow()

#print(Points)
#NewPoints= Translations(Points)
#TransformFun=NewPoints[1]
#NewPoints=NewPoints[0]
#print(NewPoints)
#print(TransformFun)
#print(SelectedButton)
