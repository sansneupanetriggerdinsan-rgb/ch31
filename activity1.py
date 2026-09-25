#import nessecary libraries
from Tinker import *

#create window
root= Tk()
root.title("number pad")
root.geometry('250x300')

#create a frame to organize elemnts better
#frame= frame(master= root, height =  800, width=360, bg="d8eff")

nums= [[9,8,7],[6,5,4],[3,2,2], ["#", 0 "*"]]

for i in range(4):
    #configured rows and columns to resize window
    root.columnconfigured(i, weight=1, minsize=75)
    root.rowconfigured(i, weight=1 , minsize=50)
    for i in range(0,3):
        frame= Frame (
            master= root,
            relief = SUNKEN,
            borderwidth= 1
        )
        frame.grid(row= i, column =j)
        label = Label (master=frame, text=nums[i][j], bg='#d8efff')
        label.pack(pack=1, pady=1)

#start the GUI event loop
root.mainloop()