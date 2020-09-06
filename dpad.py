import tkinter as tk    
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

## EDIT
#edit Icons
copy_icon=tk.PhotoImage(file="icons2/copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

edit=tk.Menu(main_menu, tearoff=False)

### view icon
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon= tk.PhotoImage(file="icons2/status_bar.png")


view=tk.Menu(main_menu, tearoff=False)

###### Color Theme  ####
light_default_icon=tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons2/light_plus.png")
dark_icon=tk.PhotoImage(file="icons2/dark.png")
red_icon=tk.PhotoImage(file="icons2/red.png")
monokai_icon=tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file="icons2/night_blue.png")

color_theme=tk.Menu(main_menu, tearoff=False)

theme_choice= tk.StringVar()
color_icons = (light_default_icon,light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict={
    "Light Default": ("#000000", "#ffffff"),
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Red": ("#2d2d2d", "#ffe8e8"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2")
}



#Cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)


 
######################   toolbar  ############### ############################

tool_bar= ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# Font Box
font_tuple= tk.font.families()
font_family= tk.StringVar()
font_box= ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"]= font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)


# Size Box
size_var=tk.IntVar()
font_size= ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
font_size["values"]= tuple(range(8,80,2))
font_size.current(3)  #12 is at index 4
font_size.grid(row=0, column=1, padx=5)

# Bold Button..
bold_icon= tk.PhotoImage(file="icons2/bold.png")
bold_btn= ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Italic Button
italic_icon= tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#underline button
underline_icon= tk.PhotoImage(file="icons2/underline.png")
underline_btn= ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# Font color button
font_color_icon= tk.PhotoImage(file="icons2/font_color.png")
font_color_btn= ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# align left button

align_left_icon= tk.PhotoImage(file="icons2/align_left.png")
align_left_btn= ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center button
align_center_icon= tk.PhotoImage(file="icons2/align_center.png")
align_center_btn= ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

#align right button
align_right_icon= tk.PhotoImage(file="icons2/align_right.png")
align_right_btn= ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# ---------&&&&&&&&&&& End main menu ------------------------------------------=--

######################   text editor   ############### ############################
text_editor=tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar= tk.Scrollbar(main_application)  # to add scroll bar
text_editor.focus_set() # cursor position
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)  #gridding scrollbar
text_editor.pack(fill= tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality
current_font_family= "Arial"
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family= font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(event=None):
    global current_font_size
    current_font_size= size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))
font_box.bind("<<ComboboxSelected>>", change_font)

font_size.bind("<<ComboboxSelected>>", change_font_size)


text_editor.configure(font=("Arial", 12))




# ---------&&&&&&&&&&& End main menu ------------------------------------------=--


######################   status bar   ############### ############################ BUTTON 

status_bar=ttk.Label(main_application, text= "Status Bar")
status_bar.pack(side=tk.BOTTOM)

# ---------&&&&&&&&&&& End main menu ------------------------------------------=--

## file commands

file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N")
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O")
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S")
file.add_command(label="Save_As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S")
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q")

## edit command

edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V")
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X")
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X")
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F")

## view check button commands

view.add_checkbutton(label="Tool Bar", image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", image=status_bar_icon, compound=tk.LEFT)

## Color Theme commands
count= 0
for i in color_dict:
    color_theme.add_radiobutton(label= i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count+=1

######################   main menu functionality   ############### ############################
# ---------&&&&&&&&&&& End main menu ------------------------------------------=--

main_application.config(menu=main_menu)
main_application.mainloop()
