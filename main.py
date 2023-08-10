import tkinter as tk

from tkinter import filedialog

from tkinter import messagebox

import customtkinter as ctk

import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Untitled - Notepad")
        self.geometry("800x600")
        self.resizable(0,0)
        self.initialize_gui()

    def initialize_gui(self):
        self.text_area = ctk.CTkTextbox(self,width=800,height=600,font= ("Arial",18))
        self.text_area.grid(row=0, column=0, sticky="nsew")

        self.file = None

        self.menu_bar = tk.Menu(self)
        self.config(menu= self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar,tearoff= 0)
        self.file_menu.add_command(label = "New",command= self.new_file)
        self.file_menu.add_command(label = "Open",command= self.open_file)
        self.file_menu.add_command(label = "Save",command= self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit",command= self.exit)
        self.menu_bar.add_cascade(label = "File",menu = self.file_menu)


        self.about_menu = tk.Menu(self.menu_bar,tearoff= 0)
        self.about_menu.add_command(label = "About",command = self.help)
        self.menu_bar.add_cascade(label = "Help",menu = self.about_menu)

    def new_file(self):
        self.title("Untitled - Notepad")
        self.text_area.delete(1.0,tk.END)

    def open_file(self):
        file = filedialog.askopenfile(defaultextension= ".txt",filetypes= [("All files","*.*"),("Text Documents", "*.txt"),("Python","*.py")])
        file = file.name

        if file == "":
            file = None
        else:
            self.title(os.path.basename(file) + "-  Notepad")  
            self.text_area.delete(1.0,tk.END)
            file = open(file,"rb")  
            self.text_area.insert(1.0,file.read())
            file.close()

    def save_file(self):
        if self.file == None:
            self.file = filedialog.asksaveasfilename(initialfile= "Untitled.txt",defaultextension= ".txt",filetypes= [("All files","*.*"),("Text Documents", "*.txt"),("Python","*.py")])
            
            if self.file == "":
                    self.file = None
            else:
                self.file = open(self.file,"w")
                self.file.write(self.text_area.get(1.0,tk.END))
                self.file.close()
                self.file = self.file.name
                self.title(os.path.basename(self.file) + " - Notepad")

        else:
            self.file = open(self.file,"w")
            self.file.write(self.text_area.get(1.0,tk.END))
            self.file.close()
      
    def exit(self):
        self.destroy()            

    def help(self):
        messagebox.showinfo("EloyPad","This simple Notepad developed by Eloy Salazar")

app = App()
app.mainloop()