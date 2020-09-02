import tkinter as tk    #22 min
from tkinter import ttk
from  tkinter import font, colorchooser, filedialog, messagebox
import os

main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title("Devansh Text Editor")


######################   main menu   ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--
main_menu= tk.Menu()
#file icons
new_icon= tk.PhotoImage(file="icons2/new.png")
open_icon= tk.PhotoImage(file="icons2/open.png")
save_icon= tk.PhotoImage(file="icons2/save.png")
save_as_icon= tk.PhotoImage(file="icons2/save_as.png")
exit_icon= tk.PhotoImage(file="icons2/exit.png")

file=tk.Menu(main_menu, tearoff=False)

file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N")
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O")
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S")
file.add_command(label="Save_As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S")
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q")

## EDIT
#edit Icons
copy_icon=tk.PhotoImage(file="icons2/copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

edit=tk.Menu(main_menu, tearoff=False)

edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V")
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X")
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X")
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F")


view=tk.Menu(main_menu, tearoff=False)
color_theme=tk.Menu(main_menu, tearoff=False)

#Cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)


 
######################   toolbar  ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--


######################   text editor   ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--


######################   status bar   ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--


######################   main menu functionality   ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--

main_application.config(menu=main_menu)
main_application.mainloop()
