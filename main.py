import os
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 



class Dialog(ctk.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("EloyPad")
        self.geometry("600x200")
        self.resizable(0,0)
        self.initialize_gui()

    def cancel(self):
        app.wm_attributes("-disabled", False)
        self.destroy()

    def no_save(self):
        self.destroy()
        app.destroy()

    def save(self):
        app.wm_attributes("-disabled", False)
        app.save_file()
        self.destroy()
        

    def initialize_gui(self):
        

        self.label = ctk.CTkLabel(self,text = "Do you want to save the changes made to untitled?",font= ("Arial",18))
        self.label.place(x = 100,y = 50)

        self.buton_cancel = ctk.CTkButton(self,text= "Cancel",command= self.cancel)
        self.buton_cancel.place(x = 50,y = 100)

        self.buton_no_save = ctk.CTkButton(self,text= "No Save",command= self.no_save)
        self.buton_no_save.place(x = 220,y = 100)

        self.buton_save = ctk.CTkButton(self,text = "Save",command= self.save)
        self.buton_save.place(x = 400,y = 100)

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

        self.saved = False
        self.file = None

        self.toplevel_window = None

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

        self.protocol("WM_DELETE_WINDOW",lambda: self.exit())

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
        self.saved = True
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
        
        if len(self.text_area.get("0.0","end")) == 1:
            
            self.destroy()
        else:
       
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                if self.saved == False:
                    self.wm_attributes("-disabled", True)
                    self.toplevel_window = Dialog(self)  # create window if its None or destroyed
                else:
                    self.destroy()
            else:
                self.toplevel_window.focus()  # if window exists focus it


            



    def help(self):
        messagebox.showinfo("EloyPad","This simple Notepad developed by Eloy Salazar")

app = App()
app.mainloop()