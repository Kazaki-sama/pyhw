'''
Coursework starter template provided by Girish Lukka

Add your student details in this section:

StudentID: w2055174 StudentName: "Savya Bikram Shah"

You must write your code in this file under the section provided
'''


import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import shutil

# Global variables section - add variables that are required

path = 'images/' # folder that has all the images
friend_widgets = {}

# functions and sub-functions to manage the various buttons and user inter-action
# see the coursework sepcification

def showFriends():
    profilePictures = [f for f in os.listdir('images/') if f.endswith('.png')]
    profilePictures.sort() 
    
    i = 0
    for profilePicture in profilePictures:
        img = Image.open(os.path.join('images/', profilePicture))
        img = img.resize((100, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        curr_name = os.path.splitext(profilePicture)[0].capitalize()
        
        pfp = Button(mainBody, image=img, compound='top',command=lambda curr_name=curr_name, col=i: friendButton(curr_name, col))
        pfp.image = img
        pfp.grid(row=0, column=i, padx=20, pady=5)
        
        name = Label(mainBody, text=curr_name + "\'s Friends", relief='sunken', bd=6, font=('Callibri', 11))
        name.grid(row=1, column=i)
    
        i += 1
    mainBody.pack()
    clear_all_button.config(state='active', fg='dark blue')
    show_friends_button.config(state='disabled')
    
        


def friendButton(curr_name,col):
    
    if col in friend_widgets:
        for widget in friend_widgets[col]:
            widget.destroy()   
    else:
        friend_widgets[col] = []         
    j = 2 
    l = col + 1
    dir_path = 'images/' + curr_name.lower() + '/'
    if not os.path.exists(dir_path):
        messagebox.showinfo(" ",f"Friends Folder doesn't exist for {curr_name}.")
    

    elif os.path.exists(dir_path):    
        friendImages = [f for f in os.listdir(dir_path) if f.endswith('.png')]
        if not friendImages:
             messagebox.showinfo(" ",f"Friends Folder does exist for {curr_name} but no image in folder.")
        for friendImage in friendImages:
            file_path = os.path.join(dir_path, friendImage)
            if os.path.isfile(file_path):
                img = Image.open(file_path)
                img = img.resize((50, 50), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                    
                friend = Label(mainBody, image=img, compound='top')
                friend.image = img
                friend.grid(row=j, column=col, padx=20, pady=5)
                    
                friendName = os.path.splitext(friendImage)[0].capitalize()
                friendNameLabel = Label(mainBody, text=friendName, relief='sunken', bd=6, font=('Callibri', 11), bg='black',foreground='white',padx=2)
                friendNameLabel.grid(row=j+1, column=col)
                j += 2
                    
                friend_widgets[col].extend([friend, friendNameLabel])
            else:
                l += 1
    else:
        j += 1 
        
    

        

def clearAll():
    for widget in mainBody.winfo_children():
        widget.destroy()
    show_friends_button.config(state='normal')
    clear_all_button.config(state='disabled')
    mainBody.pack_forget()

def delFriend():
    file_path = filedialog.askopenfilename(initialdir=path, title="Select Friend Image to Delete", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if file_path:
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this friend image?")

        if confirm:
            os.remove(file_path)
            messagebox.showinfo("Success", "Friend image deleted successfully.")
            clearAll()
            showFriends()

def addFriend():
    file_path = filedialog.askopenfilename(title="Select Friend Image to Add", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if file_path:
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to add this friend image?")
        
        if confirm:
            shutil.copy(file_path, path)
            messagebox.showinfo("Success", "Friend image added successfully.")
            clearAll()
            showFriends()
       
            



def quitApp():
    confirm_quit = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
    if confirm_quit:
        myApp.quit()

# There will be some other functions to handle the user interactions like clearing friend'sfriends, create frames, etc

# Basic Window for your app
myApp = Tk()
myApp.title("Image display app by: Subham Maharjan")
myApp.geometry("1200x800")
myApp.configure(background='Teal')

# Code to configure styles for your ttk widgets
# write code below to create styles for you buttons, labels, frames, etc



# Create a frame(mainMenu) that will hold buttons to manage the app.
mainMenu = Frame(myApp, background='cyan')
mainMenu.pack(fill='x')

titleFrame = Frame(mainMenu,background='cyan')
titleFrame.pack(side="top", fill="x")

appMenu = Label(titleFrame, text="AppMenu",background='cyan',font='Callibri 8')
appMenu.pack(side="left", anchor='n')

line = Canvas(titleFrame, width=1000, height=2, bg='black',highlightthickness=0)
line.pack( fill="x",pady=10)
# create buttons that have been described in the coursework specification and add to the frame above
show_friends_button = Button(mainMenu, text="Show Friends", height=3, width=30,font=('Callibri',9,'bold'),fg='dark blue',command=showFriends)  
show_friends_button.pack(side="left",expand=True,pady=10)

clear_all_button = Button(mainMenu, text="Clear All", height=3, width=30,font=('Callibri',9,'bold'),fg='dark blue',command=clearAll,state='disabled')  
clear_all_button.pack(side="left",expand=True,pady=10)

delete_friend_button = Button(mainMenu, text="Delete Friend", height=3, width=30,font=('Callibri',9,'bold'),fg='dark blue',command=delFriend)  
delete_friend_button.pack(side="left",expand=True,pady=10)

add_new_friend_button = Button(mainMenu, text="Add Friend",  height=3, width=30,font=('Callibri',9,'bold'),fg='dark blue',command=addFriend)  
add_new_friend_button.pack(side="left",expand=True,pady=10)

quit_button = Button(mainMenu, text="Quit", command=quitApp, height=3, width=30,font=('Callibri',9,'bold'),fg='dark blue')
quit_button.pack(side="left",expand=True,pady=10)


mainBody = Frame(myApp)
mainBody.pack()

myApp.mainloop()