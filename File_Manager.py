import sys, os, time
from tkinter import ttk
from tkinter.ttk import OptionMenu
from customtkinter import *
from PIL import Image
import threading
from open_details import *

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
                
        # image creations
        self.logo = createImage(resource_path("icons/1.png"), 120, 120)
        self.home_logo = createImage(resource_path("icons/home.png"), 22, 22)
        self.student_logo = createImage(resource_path("icons/user-add.png"), 22, 22)
        self.setting_logo = createImage(resource_path("icons/settings.png"), 22, 22)
        self.cap_logo = createImage(resource_path("icons/student.png"), 22, 22)
        self.download_logo = createImage(resource_path("icons/download.png"), 24, 24)
        self.upload_logo = createImage(resource_path("icons/upload.png"), 24, 24)
        
        
        self.left_frame = CTkFrame(self, fg_color='#F9F9F9')
        self.left_frame.pack(side='left', fill='both')
        
        self.right_frame = CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        #logo Place
        self.placeLogo = CTkLabel(self.left_frame, image=self.logo, text="")
        self.placeLogo.pack(pady=20)
        
        # menu left side
        self.dashboardBtn = self.create_menu_btn(self.left_frame, "Dashboard", self.home_logo, cmd=self.create_dashboard_window)
        self.dashboardBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.registerBtn = self.create_menu_btn(self.left_frame, "New Student", self.student_logo, cmd = self.create_register_window)
        self.registerBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.studentListBtn = self.create_menu_btn(self.left_frame, "View Students", self.cap_logo, cmd=self.create_search_window)
        self.studentListBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.settingBtn = self.create_menu_btn(self.left_frame, "Setting", self.setting_logo)
        self.settingBtn.pack(side="bottom", pady=10)
        
        # self.create_search_window()
        # self.create_dashboard_window()
        
        # ------------------------------ Loading Frmes and all -------------------------------- >

        self.logoframe = CTkFrame(self, width=1200, height=600, fg_color="white")
        self.logoframe.place(x=0, y=0)
        self.logoframe.grid_propagate(False)
        self.logoframe.pack_propagate(False)
        self.splashLogo = createImage(resource_path("icons/1.png"), 200,200)
        self.spalsh = CTkLabel(self.logoframe,text="", image=self.splashLogo, height=300, width=300, corner_radius=50)
        self.spalsh.pack()
        
        self.loading = CTkProgressBar(self.logoframe, width=300,)
        self.loading.pack()
        self.loading.set(0)
        
        
        
    def serach_thread(self):
        self.searchBtn.configure(state='disabled')
        process1 = threading.Thread(target=self.search_students)
        if not process1.is_alive():
            process1.start()
     
    def create_dashboard_window(self):
        pass
              
    def create_register_window(self):
        self.right_frame.destroy()
        self.right_frame = CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        self.scrollFrameAdd = CTkFrame(
            master=self.right_frame, bg_color="white", fg_color="white"
        )
        self.scrollFrameAdd.pack(fill="both", expand=True)
        
        
        self.RegisterBtn = CTkButton(
            self.scrollFrameAdd, text="Register", command=lambda: database.insert(self), fg_color=btn_color
        )

        head  = CTkLabel(self.scrollFrameAdd, text="Register New Student", font=("Calibri bold", 18))
        head.pack(pady=20)
        
        # Personal Infor
        self.addTopFrame = CTkFrame(
            self.scrollFrameAdd,
            border_width=1,
            border_color="#E3E3E3",
            corner_radius=5,
            bg_color="white",
            fg_color="white",
        )
        self.addTopFrame.pack(fill="both", pady=15, padx=15)
        
        self.student_photo = upload.ProfilePicEditor(self.addTopFrame)
        self.RegisterBtn.pack()
        
        # heading of addTopFrame
        headingTop = self.customLabel(self.scrollFrameAdd, "Personal Information")
        headingTop.place(x=30, y=70)
        
        # adding entry name
        self.labelofName = self.customLabel(self.addTopFrame, "NAME")
        self.labelofName.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))
        self.entryofName = self.customInput(self.addTopFrame)
        self.entryofName.grid(row=1, column=0, sticky="w", padx=(30, 10), pady=(0, 20))
        # adding entry class
        self.labelofFather = self.customLabel(self.addTopFrame, "Father's Name")
        self.labelofFather.grid(row=0, column=1, sticky="w", padx=20, pady=(10, 0))
        self.entryofFather = self.customInput(self.addTopFrame)
        self.entryofFather.grid(
            row=1, column=1, sticky="w", padx=(30, 10), pady=(0, 20)
        )
        self.labelofMother = self.customLabel(self.addTopFrame, "Mother's Name")
        self.labelofMother.grid(row=0, column=2, sticky="w", padx=20, pady=(10, 0))
        self.entryofMother = self.customInput(self.addTopFrame)
        self.entryofMother.grid(
            row=1, column=2, sticky="w", padx=(30, 10), pady=(0, 20)
        )
        self.labelofSRN_no = self.customLabel(self.addTopFrame, "SRN Number")
        self.labelofSRN_no.grid(row=0, column=3, sticky="w", padx=20, pady=(10, 0))
        self.entryofSRN_no = self.customInput(self.addTopFrame)
        self.entryofSRN_no.grid(
            row=1, column=3, sticky="w", padx=(30, 10), pady=(0, 20)
        )
        self.labelofPEN_no = self.customLabel(self.addTopFrame, "PEN Number")
        self.labelofPEN_no.grid(row=2, column=0, sticky="w", padx=20, pady=(10, 0))
        self.entryofPEN_no = self.customInput(self.addTopFrame)
        self.entryofPEN_no.grid(row=3, column=0, sticky="w", padx=(30, 0), pady=(0, 20))
        
        self.labelofAdmission = self.customLabel(self.addTopFrame, "Admission Number")
        self.labelofAdmission.grid(row=2, column=1, sticky="w", padx=20, pady=(10, 0))
        self.entryofAdmission = self.customInput(self.addTopFrame)
        self.entryofAdmission.grid(
            row=3, column=1, sticky="w", padx=(30, 0), pady=(0, 20)
        )
        
        self.labelofRoll = self.customLabel(self.addTopFrame, "Roll Number")
        self.labelofRoll.grid(row=4, column=0, sticky="w", padx=20, pady=(10, 0))
        self.entryofRoll = self.customInput(self.addTopFrame)
        self.entryofRoll.grid(
            row=5, column=0, sticky="w", padx=(30, 0), pady=(0, 20)
        )
        
        self.labelofClass = self.customLabel(self.addTopFrame, "Class")
        self.labelofClass.grid(row=2, column=2, sticky="w", padx=20, pady=(10, 0))
        self.entryofClass = CTkComboBox(
            self.addTopFrame,
            values=self.class_name_list,
        )
        self.entryofClass.grid(row=3, column=2, sticky="w", padx=(30, 0), pady=(0, 20))
        
        self.labelofSession = self.customLabel(self.addTopFrame, "Session")
        self.labelofSession.grid(row=2, column=3, sticky="w", padx=20, pady=(10, 0))
        
        self.entryofSession = CTkComboBox(
            self.addTopFrame,
            values=self.session_list,
        )
        self.entryofSession.grid(row=3, column=3, sticky="w", padx=(30, 0), pady=(0, 20))
                     
    def create_search_window(self):
        self.right_frame.destroy()     
        
        self.right_frame = CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
                
        self.main_progress = CTkProgressBar(self.right_frame, width=1200)
        self.main_progress.pack(side="bottom")
        self.main_progress.set(0)
        # right conent 
        CTkLabel(self.right_frame, text="Search Students", font=("Calibri ", 22), anchor=W).pack(pady=(20, 0), padx=10, fill='both')
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
            command=self.serach_thread
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
                         text_color='black', hover_color=hovercolor, anchor=W, image=img, command=cmd)
        return temp
    
    def customInput(self, frame):
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
        return inputEntry
     
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
        self.searchBtn.configure(state='normal')
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
        self.temp.pack(padx=10, pady=0, ipadx=1,ipady=4, anchor=W)
        
        self._tick = CTkCheckBox(
            master=self.temp,
            width=20,
            text="",
            checkbox_height=15,
            checkbox_width=15,
            corner_radius=3,
            border_width=0.5,
        )
        self._tick.place(x=6, y=20)
        self._tick.configure(
            command=lambda tick=self._tick: self.select_click(data, tick)
        )
        self.ListofCheckBox.append(self._tick)
        
        self._1 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[0]).split(" ")[0], width=120, font=("Calibri bold", 15)
        )
        self._1.grid(row=0, column=1, sticky="s", pady=1, padx=0)
        self._2 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[1]).split(" ")[0], width=120, font=("Calibri ", 13)
        )
        self._2.grid(row=0, column=2, sticky="s", pady=1, padx=0)
        self._3 = CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[2]).split(" ")[0], width=100, font=("Calibri ", 13)
        )
        self._3.grid(row=0, column=3, sticky="s", pady=1, padx=0)
        self._4 = CTkLabel(master=self.temp, text=str(data[3]).split(" ")[0], width=140, text_color='gray',  font=("Calibri ", 13))
        self._4.grid(row=1, column=1, sticky="s", pady=1, padx=0)
        self._5 = CTkLabel(master=self.temp, text=data[4], width=140, font=("Calibri ", 13))
        self._5.grid(row=0, column=4, sticky="s", pady=1, padx=0)
        self._6 = CTkLabel(master=self.temp, text=data[5], width=100, font=("Calibri ", 13))
        self._6.grid(row=0, column=5, sticky="s", pady=1, padx=0)
        self._7 = CTkLabel(master=self.temp, text=data[6], width=100, font=("Calibri ", 13))
        self._7.grid(row=0, column=6, sticky="s", pady=1, padx=(0, 0))
        self.temp.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.temp.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
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
    
        self.temp.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._1.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._2.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._3.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._4.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._5.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._6.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        self._7.bind("<Double-Button-1>", lambda event: modify_record(self, data_list=data))
        
        self.pdf_download_btn = CTkButton(
            master=self.temp,
            width=50, height=50,
            fg_color=btn_color,
            text="",
            compound="left",
            text_color='white',
            font=("calibri bold", 16),
            image=self.download_logo,
            command=lambda: database.retrieve_pdf_file(srn_no=str(data[3])),
        )
        self.pdf_download_btn.grid(row=0, column=7, rowspan=2, sticky="s", padx=2, pady=6)
        
        self.pdf_upload_btn = CTkButton(
            master=self.temp,
            width=50, height=50,
            text="",
            compound="left",
            text_color='white',
            font=("calibri bold", 16),
            image=self.upload_logo,
            fg_color="#ABDEF5",
            command=lambda: self.open_Pdf_file(srn=str(data[3])),
        )
        self.pdf_upload_btn.grid(row=0, column=8, rowspan=2, sticky="s", padx=2, pady=6)
        
        self.user_pic_label = CTkLabel(self.temp, text="",  
                                       width=50, height=50, corner_radius=5)
        self.user_pic_label.grid(row=0, column=0, rowspan=2, pady=0.5, padx=25)
        threading.Thread(target=self.getPic, args=(self.user_pic_label, data)).start()
         
        self.update_idletasks()

        
        
    def getPic(self, obj, data):
        img = database.show_images_from_db(str(data[3]),60,76,)
        obj.configure(image=img)
        
    def open_Pdf_file(self, srn):
        # Create a new CTkFileDialog widget
        self.file_dialog = filedialog.askopenfilename(filetypes=[("pdf", "*.pdf")])

        try:
            database.insert_pdf_file(srn, self.file_dialog)
        except Exception as e:
            print(e)
    
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
       
def destroy():
    for i in range(40):
        root.loading.set((i/100)*4)
        root.update_idletasks()
    root.logoframe.destroy()
    
def loading_and_destory():
    import mysql_conn as database
          
        
if __name__ == "__main__":
    try:
        root = main_gui()
        root.after(500, loading_and_destory)
        root.after(2000, destroy)
        root.mainloop()

    except Exception as e:
        print(f"Error: {e}")
        
        
        