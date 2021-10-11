from tkinter import *
root =Tk()
root.title("Carbon Emission Calculator")
root.geometry("2560x1600")


#main title
main_title = Label(root, text="Carbon Emissions from Zoom Calls", font="Arial 25").pack(pady=75, padx=0)


#defining selections for radio buttons
x = IntVar()
y = IntVar()


#type of call
type_of_call = Label(root, text="Number of participants", font="Arial 20").pack(pady = 10)
Radiobutton(root,text= "1:1 call", variable= x, value=1).pack()
Radiobutton(root,text= "Group call", variable= x, value=2).pack()


#call quality
call_quality = Label(root, text="Call Quality", font="Arial 20").pack(pady = (40,10))
Radiobutton(root,text= "Default", variable= y, value=1).pack()
Radiobutton(root,text= "720p HD", variable= y, value=2).pack()
Radiobutton(root,text= "1080p HD", variable= y, value=3).pack()


#call duration
duration_of_call = Label(root, text="Duration of Call (in hours)", font="Arial 20").pack(pady = (40,10))
e = Entry(root, width = 10)
e.pack(pady = (0,40))



#calculations

bandwidth = 0;

#submit button!
def onclick():
    duration = float(e.get())
    
    if x.get() == 1:
        if y.get() == 1:
            bandwidth = 0.54
        elif y.get() == 2:
            bandwidth = 1.08
        else:
            bandwidth = 1.62
    elif x.get() == 2:
        if y.get() == 1:
            bandwidth = 0.81
        elif y.get() == 2:
            bandwidth = 1.35
        else:
            bandwidth = 2.475
            
    final = Label(root, text= "The amount of CO2 generated from this call is " + str(round(bandwidth * duration * 0.06 * 0.4085, 3)) + "kg").pack()




submit_button= Button(root, text="Calculate", command = onclick).pack()



root.mainloop()