import sys, os
from tkinter import ttk, messagebox, filedialog, StringVar
from tkinter.ttk import OptionMenu
from customtkinter import *
from PIL import Image
import mysql_conn as database
import multiprocessing
import time, random

hovercolor = "#579BE3"
btn_color = "#098FF0"

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def open_window_in_center(root ,width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x_position}+{y_position}")

def createImage(path, w, h):
        temp = CTkImage(
            light_image=Image.open(path), dark_image=Image.open(path), size=(w, h)
        )
        return temp
    
class main_gui(CTk):
    def __init__(self):
        super().__init__()
        self.title("File Manager 2025")
        self.iconbitmap(default=resource_path("icons/schoolLogo.ico"))
        open_window_in_center(self, 1200, 600)
        self.configure(fg_color='white')
        
        self.List_of_Entry = []
        self.List_of_Search = []
        self.list_of_selected_student = []
        self.ListofCheckBox = []
        
        self.class_name_list = [ "NURSERY", "KG", "1ST", "2ND", "3RD", "4TH", "5TH", "6TH", "7TH", "8TH", "9TH", "10TH", "11TH", "12TH"]
        self.session_list = [str(str(i) + " - " + str(i+1)) for i in range(2010, 2030)]
        
        
        self.left_frame = CTkFrame(self, fg_color='white')
        self.left_frame.pack(side='left', fill='both')
        
        self.right_frame = CTkFrame(self, fg_color='white',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        # image creations
        self.logo = createImage(resource_path("icons/logo.png"), 80, 80)
        self.home_logo = createImage(resource_path("icons/home.png"), 22, 22)
        self.student_logo = createImage(resource_path("icons/user.png"), 22, 22)
        self.setting_logo = createImage(resource_path("icons/settings.png"), 22, 22)
        self.cap_logo = createImage(resource_path("icons/student.png"), 22, 22)
        self.user = createImage(resource_path("icons/display.png"), 40, 40)
        
        #logo Plce
        self.placeLogo = CTkLabel(self.left_frame, image=self.logo, text="")
        self.placeLogo.pack(pady=20)
        
        # menu left side
        self.dashboardBtn = self.create_menu_btn(self.left_frame, "Dashboard", self.home_logo)
        self.dashboardBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.registerBtn = self.create_menu_btn(self.left_frame, "New Student", self.student_logo)
        self.registerBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.storeBtn = self.create_menu_btn(self.left_frame, "Store Marks", self.cap_logo)
        self.storeBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.settingBtn = self.create_menu_btn(self.left_frame, "Setting", self.setting_logo)
        self.settingBtn.pack(side="bottom", pady=10)
        
        # right conent 
        CTkLabel(self.right_frame, text="Dashboard", font=("Calibri ", 28), anchor=W).pack(pady=(20, 0), padx=10, fill='both')
        self.TopFrame = CTkFrame(self.right_frame, fg_color='white')
        self.TopFrame.pack(fill='both')
        

        # adding entry name
        self.labelofName = self.customLabel(self.TopFrame, "NAME")
        self.labelofName.grid(row=0, column=0, sticky="w", padx=(20, 10), pady=(10, 0))
        self.searchName = self.customInput2(self.TopFrame)
        self.searchName.grid(row=1, column=0, sticky="w", padx=(20, 10), pady=(0, 20))

        # adding entry Father Name
        self.labelofFather = self.customLabel(self.TopFrame, "Father's Name")
        self.labelofFather.grid(row=0, column=1, sticky="w", padx=(10, 10), pady=(10, 0))
        self.searchFather = self.customInput2(self.TopFrame) 
        self.searchFather.grid(row=1, column=1, sticky="w", padx=(10, 10), pady=(0, 20))

        # adding entry SRN No
        self.labelofSRN_No = self.customLabel(self.TopFrame, "SRN No")
        self.labelofSRN_No.grid(row=0, column=2, sticky="w", padx=(10, 10), pady=(10, 0))
        self.searchSRN_No = self.customInput2(self.TopFrame)
        self.searchSRN_No.grid(row=1, column=2, sticky="w", padx=(10, 10), pady=(0, 20))

        # adding entry PEN No
        self.labelofPEN_No = self.customLabel(self.TopFrame, "PEN No")
        self.labelofPEN_No.grid(row=0, column=3, sticky="w", padx=(10, 10), pady=(10, 0))
        self.searchPEN_No = self.customInput2(self.TopFrame)
        self.searchPEN_No.grid(row=1, column=3, sticky="w", padx=(10, 10), pady=(0, 20))

        # adding entry Admission No
        self.labelofAdmission = self.customLabel(self.TopFrame, "Admission No")
        self.labelofAdmission.grid(row=0, column=4, sticky="w", padx=(10, 10), pady=(10, 0))
        self.searchAdmission = self.customInput2(self.TopFrame)
        self.searchAdmission.grid(
            row=1, column=4, sticky="w", padx=(10, 10), pady=(0, 20)
        )
        # adding entry Roll no
        self.labelofRoll = self.customLabel(self.TopFrame, "Roll No")
        self.labelofRoll.grid(row=0, column=5, sticky="w", padx=(10, 10), pady=(10, 0))
        self.searchRoll = self.customInput2(self.TopFrame)
        self.searchRoll.grid(
            row=1, column=5, sticky="w", padx=(10, 10), pady=(0, 20)
        )
        
        # adding entry Class
        self.labelofClass = self.customLabel(self.TopFrame, "Class")
        self.labelofClass.grid(row=2, column=0, sticky="w", padx=(10, 10), pady=(10, 0))
        
        
        self.searchClass = CTkComboBox(
            self.TopFrame,
            values=self.class_name_list,
        )
        self.searchClass.grid(row=3, column=0, sticky="w", padx=(10, 10), pady=(0, 20))
        self.searchClass.set("")

        
        # adding Label Session
        self.labelofSession = self.customLabel(self.TopFrame, "Session")
        self.labelofSession.grid(row=2, column=1, sticky="w", padx=(10, 10), pady=(10, 0))
        
        # session Search
        self.searchSession = CTkComboBox(
            self.TopFrame,
            values = self.session_list,
        )
        self.searchSession.grid(row=3, column=1, sticky="w", padx=(10, 10), pady=(0, 20))
        self.searchSession.set("")
        
        self.searchReset = CTkButton(
            self.TopFrame,
            text="Reset",
            command=lambda: self.reset_search(self.List_of_Search),
            fg_color="#B4BAC7",
            width=20,
        )
        self.searchReset.grid(row=3, column=2, sticky="w", padx=(80,0), pady=(0, 20))
        
        self.searchBtn = CTkButton(
            self.TopFrame,
            text_color='white',
            text="Search",
            width=20,
            fg_color=btn_color,
            command=self.search_students
        )
        self.searchBtn.grid(row=3, column=2, sticky="w", padx=10, pady=(0, 20))

        path = resource_path('icons/increase.png')
        inc_image = CTkImage(
            light_image=Image.open(path), dark_image=Image.open(path), size=(22, 22)
        )
        # promtote btn
        self.class_promote_btn = CTkButton(
            self.TopFrame,
            text="Promote",
            text_color='white',
            width=20,
            image=inc_image,
            fg_color=btn_color,
            command=lambda: database.promote(self.list_of_selected_student, self.class_name_list, 1, self)
        )
        self.class_promote_btn.grid(row=3, column=4, sticky="w", padx=10, pady=(0, 20))
        
        path2= resource_path('icons/decrease.png')
        inc_image2 = CTkImage(
            light_image=Image.open(path2), dark_image=Image.open(path2), size=(22, 22)
        )
        
        # demote btn
        self.class_demote = CTkButton(
            self.TopFrame,
            text="Demote",
            text_color='white',
            width=20,
            image=inc_image2,
            fg_color=btn_color,
            command=lambda: database.promote(self.list_of_selected_student, self.class_name_list, -1, self)
        )
        self.class_demote.grid(row=3, column=5, sticky="w", padx=10, pady=(0, 20))
        
        self.scroll_frame = CTkScrollableFrame(self.right_frame, fg_color='white' )
        self.scroll_frame.pack(fill='both', expand=True)
        
    def reset_search(self, list):
        for entry in list:
            entry.delete(0, END)
        self.searchClass.set("")
        self.searchSession.set("")
        self.list_of_selected_student.clear()    
        
    def on_enter(self, obj):
        obj.configure(border_color="#20A1FF", fg_color="#ADDFFF")

    def on_leave(self, obj):
        obj.configure(border_color="#D9D9D9", fg_color="white")    
    
    def select_click(self, data, tick):
        if tick.get() == 1:
            self.list_of_selected_student.append([data[3], data[6]])
            
        else:
            self.list_of_selected_student.remove(data[3])    
    
    def customLabel(self, frame, txt):
        temp = CTkLabel(master=frame, text=txt, font=("Calibri", 16), bg_color="white")
        return temp
    
    def create_menu_btn(self, frame, txt, img="", cmd=""):
        temp = CTkButton(frame, text=txt, corner_radius=6, width=150, height=35, fg_color='white',
                         text_color='black', hover_color=hovercolor, anchor=W, image=img)
        return temp
    
    
    
    def customInput2(self, frame):
        # Create a custom style for the round-cornered Entry
        style = ttk.Style()
        style.configure(
            "Round.TEntry",
            padding=10,
            borderwidth=5,
            relief="flat",
            background="#f0f0f0",
            bordercolor="#20A1FF",
            focuscolor="none",
        )
        inputEntry = ttk.Entry(
            frame, style="Round.TEntry", font=("Verdana", 12), takefocus=True
        )
        self.List_of_Entry.append(inputEntry)
        
        self.List_of_Search.append(inputEntry)
        return inputEntry
    
    def create_record(self, data_list):
        self.clear_frame()
        if len(data_list) > 0:
            for data in data_list:
                self.make_record_frame(data=data)

    def clear_frame(self):
        children = self.scroll_frame.winfo_children()
        for widget in children:
            widget.destroy()

    def search_students(self):
        self.list_of_selected_student.clear()
        self.list_of_student = database.search_students(
            name=self.searchName.get(),
            father_name=self.searchFather.get().upper(),
            clas=self.searchClass.get().upper(),
            srn_no=self.searchSRN_No.get().upper(),
            pen_no=self.searchPEN_No.get().upper(),
            admission_no=self.searchAdmission.get().upper(),
            session=self.searchSession.get().upper(),
            roll=self.searchRoll.get().upper(),
        )
        self.create_record(self.list_of_student)
        # print(self.list_of_student)
        
    def make_record_frame(self, data):
        self.temp = CTkFrame(
            self.scroll_frame,
            height=60,
            corner_radius=0,
            border_color="#D9D9D9",
            border_width=0.4,
            bg_color="white",
            fg_color="white",
        )
        self.temp.grid(row=0, column = 0, padx=10, pady=10, ipadx=2)
        
        self._tick = CTkCheckBox(
            master=self.temp,
            width=20,
            text="",
            checkbox_height=15,
            checkbox_width=15,
            corner_radius=3,
            border_width=0.5,
        )
        self._tick.grid(row=0, column=0, pady=0.5, padx=(16, 16))
        self._tick.configure(
            command=lambda tick=self._tick: self.select_click(data, tick)
        )
        self.ListofCheckBox.append(self._tick)
        
        self._1 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[0]), width=120
        )
        self._1.grid(row=0, column=1, sticky="s", pady=1, padx=0)
        self._2 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=data[1], width=120
        )
        self._2.grid(row=0, column=2, sticky="s", pady=1, padx=0)
        self._3 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=data[2], width=100
        )
        self._3.grid(row=0, column=3, sticky="s", pady=1, padx=0)
        self._4 = CTkLabel(master=self.temp, text=data[3], width=100)
        self._4.grid(row=0, column=4, sticky="s", pady=1, padx=0)
        self._5 = CTkLabel(master=self.temp, text=data[4], width=100)
        self._5.grid(row=0, column=5, sticky="s", pady=1, padx=0)
        self._6 = CTkLabel(master=self.temp, text=data[5], width=100)
        self._6.grid(row=0, column=6, sticky="s", pady=1, padx=0)
        self._7 = CTkLabel(master=self.temp, text=data[6], width=100)
        self._7.grid(row=0, column=7, sticky="s", pady=1, padx=(0, 0))
        self._1.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._1.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._2.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._2.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._3.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._3.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._4.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._4.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._5.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._5.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._6.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._6.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self._7.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self._7.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
    
        self._1.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._2.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._3.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._4.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._5.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._6.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        self._7.bind("<Double-Button-1>", lambda event: self.modify_record(data))
        # self.pdf_logo = createImage(resource_path("icons/pdf-file.png"), 24, 24)
        # self.pdf_eye = CTkButton(
        #     master=self.temp,
        #     text="View Pdf",
        #     compound="left",
        #     text_color='white',
        #     font=("calibri bold", 16),
        #     width=140,
        #     # image=self.pdf_logo,
        #     command=lambda: database.retrieve_pdf_file(srn_no=str(data[3])),
        # )
        # self.pdf_eye.grid(row=0, column=8, sticky="s", pady=1, padx=(0, 0))
    
def main_program():
    root = main_gui()
    
    root.mainloop()
    
class SplashScreen(CTk):
    def __init__(self, i):
        super().__init__()
        self.overrideredirect(1)
        self.configure(fg_color='blue')
        self.wm_attributes("-transparentcolor", "blue")
        self.title("Splash Screen")
        self.iconbitmap(default=resource_path("icons/schoolLogo.ico"))
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position to center the window
        x_position = (screen_width - self.winfo_reqwidth()) // 2
        y_position = (screen_height - self.winfo_reqheight()) // 2

        # Set window position
        self.geometry("+{}+{}".format(x_position, y_position))
        self.splashLogo = createImage(resource_path(f"icons/{i}.png"), 200,200)
        label = CTkLabel(self,text="", image=self.splashLogo, height=300, width=300, corner_radius=50)
        label.pack(pady=50)
       
        
        
        
if __name__ == "__main__":
    a = random.randrange(1, 4)
    splash_screen = SplashScreen(a)

    # Create a separate process for the main program
    main_process = multiprocessing.Process(target=main_program)

    try:
        # Start the splash screen
        splash_screen.update()
        splash_screen.after(5000, splash_screen.destroy)
        splash_screen.mainloop()

        # Start the main program in a separate process
        main_process.start()
        main_process.join()  # Wait for the main process to finish

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Ensure that the main process is terminated
        if main_process.is_alive():
            main_process.terminate()
        
        
        