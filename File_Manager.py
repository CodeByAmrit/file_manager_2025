import sys, os
from tkinter import ttk
import customtkinter 
from PIL import Image
import threading
from open_details import *
import json
from datetime import datetime

# pip install -r requirements.txt   ---- run this command to install all dependent librariess
hovercolor = "#579BE3"
btn_color = "#098FF0"

current_year = datetime.now().year

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
    temp = customtkinter.CTkImage(
        light_image=Image.open(path), dark_image=Image.open(path), size=(w, h)
    )
    return temp
        
class main_gui(customtkinter.CTk):
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
        
        self.class_name_list = [ "NURSERY", "KG", "1ST", "2ND", "3RD", "4TH", "5TH", "6TH", "7TH", "8TH", "9TH", "10TH"]
        self.session_list = [str(str(i) + " - " + str(i+1)) for i in range(2010, 2030)]
        self.subjects_list = ["ENGLISH", "HINDI", "MATHS", "SCIENCE", "SOCIAL SCIENCE", "EVS", "SANSKRIT", "COMPUTER", "GK", "DRAWING"]
                
        # image creations
        self.logo = createImage(resource_path("icons/1.png"), 120, 120)
        self.home_logo = createImage(resource_path("icons/home.png"), 22, 22)
        self.student_logo = createImage(resource_path("icons/user-add.png"), 22, 22)
        self.setting_logo = createImage(resource_path("icons/settings.png"), 22, 22)
        self.cap_logo = createImage(resource_path("icons/student.png"), 22, 22)
        self.paper_logo = createImage(resource_path("icons/document.png"), 22, 22)
        self.download_logo = createImage(resource_path("icons/download.png"), 24, 24)
        self.upload_logo = createImage(resource_path("icons/upload.png"), 24, 24)
        self.pdf_logo = createImage(resource_path("icons/pdf-file.png"), 25, 25)
        self.delete_logo = createImage(resource_path("icons/trash.png"), 25, 25)
        self.excel_logo = createImage(resource_path("icons/xls.png"), 24, 24)
        self.inc_image = createImage(resource_path('icons/increase.png'), 22, 22)
        self.inc_image2= createImage(resource_path('icons/decrease.png'), 22, 22)
        
        self.left_frame = customtkinter.CTkFrame(self, fg_color='#F9F9F9')
        self.left_frame.pack(side='left', fill='both')
        
        self.right_frame = customtkinter.CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        #logo Place
        self.placeLogo = customtkinter.CTkLabel(self.left_frame, image=self.logo, text="")
        self.placeLogo.pack(pady=20)
        
        # menu left side
        self.dashboardBtn = self.create_menu_btn(self.left_frame, "Dashboard", self.home_logo, cmd=self.create_dashboard_window)
        self.dashboardBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.registerBtn = self.create_menu_btn(self.left_frame, "New Student", self.student_logo, cmd = self.create_register_window)
        self.registerBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.studentListBtn = self.create_menu_btn(self.left_frame, "View Students", self.cap_logo, cmd=self.create_search_window)
        self.studentListBtn.pack(ipady=4, ipadx = 8, pady=4)
        self.question_paper_btn = self.create_menu_btn(self.left_frame, "Question Papers", self.paper_logo, cmd=self.create_question_paper_window)
        self.question_paper_btn.pack(ipady=4, ipadx = 8, pady=4)
        self.settingBtn = self.create_menu_btn(self.left_frame, "Setting", self.setting_logo, cmd=self.open_settings_window)
        self.settingBtn.pack(side="bottom", pady=10)
        
        # self.create_search_window()
        # self.create_dashboard_window()
        
        # ------------------------------ Loading Frmes and all -------------------------------- >

        self.logoframe = customtkinter.CTkFrame(self, width=1200, height=600, fg_color="white")
        self.logoframe.place(x=0, y=0)
        self.logoframe.grid_propagate(False)
        self.logoframe.pack_propagate(False)
        self.splashLogo = createImage(resource_path("icons/1.png"), 200,200)
        self.spalsh = customtkinter.CTkLabel(self.logoframe,text="", image=self.splashLogo, height=300, width=300, corner_radius=50)
        self.spalsh.pack(pady=(100, 10))
        
        self.loading = customtkinter.CTkProgressBar(self.logoframe, width=300,)
        self.loading.pack()
        self.loading.set(0)
        customtkinter.CTkLabel(self.logoframe, text="Connecting to database ...").pack(pady=5)
      
    def serach_thread(self):
        # self.process1 = threading.Thread(target=self.search_students)
        # if not self.process1.is_alive():
        #     self.process1.start()
        self.search_students()
     
    def create_dashboard_window(self):
        self.right_frame.destroy()
        self.right_frame = customtkinter.CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        # ========= database values to get =============
        self.s_total = str(database.count_students("students"))
        self.p_total = str(database.count_students("pdf_files"))
        self.no_of_students_classwise = database.get_students_count_by_class(str(current_year) +" - "+ str(current_year+1))
        
        self.top_title = customtkinter.CTkLabel(self.right_frame, text='Dashboard',font=("Calibri ", 30))
        self.top_title.pack(anchor = customtkinter.W, ipadx=20, padx=20, pady=(30,0))
        
        mid = customtkinter.CTkFrame(self.right_frame, fg_color='#FBFBFB')
        mid.pack(anchor = customtkinter.W, padx=20, pady=10)
        
        # Total Student Widget
        self.total_student_frame = customtkinter.CTkFrame(mid, width=200, height=80, 
                                    fg_color="#F5F5F5", corner_radius=10, border_width=0.8, border_color='#D4D4D4')
        self.total_student_frame.pack(padx=20, pady=20, side="left")
        self.total_student_frame.pack_propagate(False)
                
        self.total_no_student = customtkinter.CTkLabel(self.total_student_frame, text=self.s_total, font=("Calibri bold", 50),)
        self.total_no_student.pack(side='bottom', pady=1)
        customtkinter.CTkLabel(self.total_student_frame, text="Total Students", text_color="gray",font=("Calibri bold", 15)).place(x=10, y=2)
        
        # Total PDF Widget
        self.total_document_frame = customtkinter.CTkFrame(mid, width=200, height=80, 
                                    fg_color="#F5F5F5", corner_radius=10, border_width=0.8, border_color='#D4D4D4')
        self.total_document_frame.pack(padx=20, pady=20, side="left")
        self.total_document_frame.pack_propagate(False)
                
        self.total_no_pdf = customtkinter.CTkLabel(self.total_document_frame, text=self.p_total, font=("Calibri bold", 50),)
        self.total_no_pdf.pack(side='bottom', pady=1)
        self.total_no_pdf2 = customtkinter.CTkLabel(self.total_document_frame, text="/"+self.s_total, font=("Calibri bold", 20),text_color="gray")
        self.total_no_pdf2.place(x=140, y=40)
        customtkinter.CTkLabel(self.total_document_frame, text="PDF File", text_color="gray",font=("Calibri bold", 15)).place(x=10, y=2)
        
        # graph
        self.graph_frame = customtkinter.CTkFrame(self.right_frame, width=720, height=300, corner_radius=5, fg_color='white')
        self.graph_frame.pack_propagate(False)
        self.graph_frame.pack(anchor = customtkinter.W, padx=40, pady=10, ipadx=20)
        
        for i in range(len(self.no_of_students_classwise)):
            customtkinter.CTkFrame(self.graph_frame, width=40, height=self.no_of_students_classwise[i][1]*3, fg_color="#6ac5fe", corner_radius=1).grid(row = 0, column= i, padx=5, pady=(5,2), sticky="S")
            l = customtkinter.CTkLabel(self.graph_frame, width=40, text=str(self.class_name_list[i]))
            l.grid(row=3, column=i, padx=5,pady=5)
            l.grid_propagate(False)
            # customtkinter.CTkFrame(self.graph_frame, width=40, height=random.randint(120, 200), fg_color="#6ac5fe").pack(side="left", padx=5,pady=(15,2), anchor=customtkinter.S)
        
        
        
              
    def create_register_window(self):
        self.right_frame.destroy()
        self.right_frame = customtkinter.CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
        
        self.scrollFrameAdd = customtkinter.CTkFrame(
            master=self.right_frame, bg_color="white", fg_color="white"
        )
        self.scrollFrameAdd.pack(fill="both", expand=True)
        
        
        self.RegisterBtn = customtkinter.CTkButton(
            self.scrollFrameAdd, text="Register", command=lambda: database.insert(self), fg_color=btn_color
        )

        head  = customtkinter.CTkLabel(self.scrollFrameAdd, text="Register New Student", font=("Calibri bold", 18))
        head.pack(pady=20)
        
        # Personal Infor
        self.addTopFrame = customtkinter.CTkFrame(
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
        self.entryofClass = customtkinter.CTkComboBox(
            self.addTopFrame,
            values=self.class_name_list,
        )
        self.entryofClass.grid(row=3, column=2, sticky="w", padx=(30, 0), pady=(0, 20))
        
        self.labelofSession = self.customLabel(self.addTopFrame, "Session")
        self.labelofSession.grid(row=2, column=3, sticky="w", padx=20, pady=(10, 0))
        
        self.entryofSession = customtkinter.CTkComboBox(
            self.addTopFrame,
            values=self.session_list,
        )
        self.entryofSession.grid(row=3, column=3, sticky="w", padx=(30, 0), pady=(0, 20))
                     
    def create_search_window(self):
        self.right_frame.destroy()     
        
        self.right_frame = customtkinter.CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
       
        # right conent 
        customtkinter.CTkLabel(self.right_frame, text="Search Students", font=("Calibri ", 22), anchor=customtkinter.W).pack(pady=(20, 0), padx=10, fill='both')
        self.TopFrame = customtkinter.CTkFrame(self.right_frame, fg_color='white')
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
        
        
        self.searchClass = customtkinter.CTkComboBox(
            self.TopFrame,
            values=self.class_name_list,
        )
        self.searchClass.grid(row=3, column=0, sticky="w", padx=(10, 10), pady=(0, 20))
        self.searchClass.set("")

        
        # adding Label Session
        self.labelofSession = self.customLabel(self.TopFrame, "Session")
        self.labelofSession.grid(row=2, column=1, sticky="w", padx=(10, 10), pady=(10, 0))
        
        # session Search
        self.searchSession = customtkinter.CTkComboBox(
            self.TopFrame,
            values = self.session_list,
        )
        self.searchSession.grid(row=3, column=1, sticky="w", padx=(10, 10), pady=(0, 20))
        self.searchSession.set("")
        
        self.searchReset = customtkinter.CTkButton(
            self.TopFrame,
            text="Reset",
            command=lambda: self.reset_search(self.List_of_Search),
            fg_color="#B4BAC7",
            width=20,
        )
        self.searchReset.grid(row=3, column=2, sticky="w", padx=(80,0), pady=(0, 20))
        
        self.searchBtn = customtkinter.CTkButton(
            self.TopFrame,
            text_color='white',
            text="Search",
            width=20,
            fg_color=btn_color,
            command=self.serach_thread
        )
        self.searchBtn.grid(row=3, column=2, sticky="w", padx=10, pady=(0, 20))
        
        self.switch_photo = customtkinter.CTkSwitch(
            self.TopFrame,
            text="Show Photo"
        )
        self.switch_photo.grid(row=3, column=3, sticky="w", padx=10, pady=(0, 20))
        
        self.excelBtn = customtkinter.CTkButton(
            self.TopFrame,
            text="",
            width=30,
            height=30,
            fg_color="white",
            hover_color="lightgray",
            image=self.excel_logo,
            command=self.export_excel_file
        )
        self.excelBtn.grid(row=3, column=5, sticky="e", padx=10, pady=(0, 20))

        
        # promtote btn
        self.class_promote_btn = customtkinter.CTkButton(
            self.TopFrame,
            text="Promote",
            text_color='white',
            width=20,
            image=self.inc_image,
            fg_color=btn_color,
            command=lambda: database.promote(self.list_of_selected_student, self.class_name_list, 1, self)
        )
        self.class_promote_btn.grid(row=3, column=4, sticky="w", padx=10, pady=(0, 20))
        
        
        # demote btn
        self.class_demote = customtkinter.CTkButton(
            self.TopFrame,
            text="Demote",
            text_color='white',
            width=20,
            image=self.inc_image2,
            fg_color=btn_color,
            command=lambda: database.promote(self.list_of_selected_student, self.class_name_list, -1, self)
        )
        self.class_demote.grid(row=3, column=5, sticky="w", padx=10, pady=(0, 20))
        
        self.scroll_frame = customtkinter.CTkScrollableFrame(self.right_frame, fg_color='white' )
        self.scroll_frame.pack(fill='both', expand=True)
            
    def create_question_paper_window(self):
        self.right_frame.destroy()     
        
        self.right_frame = customtkinter.CTkFrame(self, fg_color='#FBFBFB',)
        self.right_frame.pack(side='left', expand=True, fill='both')
        self.left_frame.pack_propagate(False)
       
        # right conent 
        customtkinter.CTkLabel(self.right_frame, text="Question Paper", font=("Calibri ", 22), anchor=customtkinter.W).pack(pady=(20, 0), padx=10, fill='both')
        self.TopFrame = customtkinter.CTkFrame(self.right_frame, fg_color='white')
        self.TopFrame.pack(fill='both')
        
        # adding entry Class
        self.labelofClass = self.customLabel(self.TopFrame, "Class")
        self.labelofClass.grid(row=2, column=0, sticky="w", padx=(10, 10), pady=(10, 0))
        
        self.questionClass = customtkinter.CTkComboBox(
            self.TopFrame,
            values=self.class_name_list,
        )
        self.questionClass.grid(row=3, column=0, sticky="w", padx=(10, 10), pady=(0, 20))
        self.questionClass.set("")

        # adding Label Session
        self.labelofSession = self.customLabel(self.TopFrame, "Session")
        self.labelofSession.grid(row=2, column=1, sticky="w", padx=(10, 10), pady=(10, 0))
        
        # session Search
        self.questionSession = customtkinter.CTkComboBox(
            self.TopFrame,
            values = self.session_list,
        )
        self.questionSession.grid(row=3, column=1, sticky="w", padx=(10, 10), pady=(0, 20))
        self.questionSession.set("")
        
        # adding Label term
        self.labelofTerm = self.customLabel(self.TopFrame, "Term")
        self.labelofTerm.grid(row=2, column=2, sticky="w", padx=(10, 10), pady=(10, 0))
        
        # term question
        self.questionTerm = customtkinter.CTkComboBox(
            self.TopFrame,
            values = ["1st", "2nd", "3rd"],
        )
        self.questionTerm.grid(row=3, column=2, sticky="w", padx=(10, 10), pady=(0, 20))
        self.questionTerm.set("")
        
        #subjects btn
        self.questionSubject = customtkinter.CTkComboBox(
            self.TopFrame,
            values = self.subjects_list,
        )
        self.questionSubject.grid(row=3, column=3, sticky="w", padx=(10, 10), pady=(0, 20))
        
        # reset button
        self.questionReset = customtkinter.CTkButton(
            self.TopFrame,
            text="Reset",
            command=lambda: self.reset_search(self.List_of_Search),
            fg_color="#B4BAC7",
            width=20,
        )
        self.questionReset.grid(row=3, column=4, sticky="w", padx=(80,0), pady=(0, 20))
        
        # Search Quesetion Paper Btn
        self.searchBtn = customtkinter.CTkButton(
            self.TopFrame,
            text_color='white',
            text="Search",
            width=20,
            fg_color=btn_color,
            command=self.search_question_paper
        )
        self.searchBtn.grid(row=3, column=4, sticky="w", padx=10, pady=(0, 20))

        # Add Question Paper btn
        self.addPaperBtn = customtkinter.CTkButton(
            self.TopFrame,
            text="Upload Paper ",
            text_color='white',
            width=20,
            fg_color=btn_color,
            command=self.open_question_paper_file
        )
        self.addPaperBtn.grid(row=4, column=0, sticky="w", padx=10, pady=(0, 20))
        
        self.scroll_frame = customtkinter.CTkScrollableFrame(self.right_frame, fg_color='white' )
        self.scroll_frame.pack(fill='both', expand=True)
            
    def reset_search(self, list):
        for entry in list:
            entry.delete(0, END)
        try:    
            self.searchClass.set("")
            self.searchSession.set("")
            self.list_of_selected_student.clear()    
        except:
            self.questionClass.set("")
            self.questionSession.set("")
            self.questionTerm.set("")
            self.questionSubject.set("")
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
        temp = customtkinter.CTkLabel(master=frame, text=txt, font=("Calibri", 16), bg_color="white")
        return temp
    
    def create_menu_btn(self, frame, txt, img="", cmd=""):
        temp = customtkinter.CTkButton(frame, text=txt, corner_radius=6, width=150, height=35, fg_color='white',
                         text_color='black', hover_color=hovercolor, anchor=customtkinter.W, image=img, command=cmd)
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
            if self.switch_photo.get() == 1:
                for data in data_list:
                    self.make_record_frame(data=data)
            else:
                for data in data_list:
                    self.make_record_frame_simple(data=data)
                    
    def clear_frame(self):
        children = self.scroll_frame.winfo_children()
        for widget in children:
            widget.destroy()

    def export_excel_file(self):
        self.list_of_selected_student.clear()
        self.list_of_student = database.export_excel_sheet(
            name=self.searchName.get(),
            father_name=self.searchFather.get().upper(),
            clas=self.searchClass.get().upper(),
            srn_no=self.searchSRN_No.get().upper(),
            pen_no=self.searchPEN_No.get().upper(),
            admission_no=self.searchAdmission.get().upper(),
            session=self.searchSession.get().upper(),
            roll=self.searchRoll.get().upper(),
            excel=True,
        )
        
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
        
    def make_record_frame_simple(self, data):
        self.temp = customtkinter.CTkFrame(
            self.scroll_frame,
            corner_radius=0,
            border_color="#D9D9D9",
            border_width=0.4,
            fg_color="white",
            height=40,
        )

        self._tick = customtkinter.CTkCheckBox(
            master=self.temp,
            width=20,
            text="",
            checkbox_height=15,
            checkbox_width=15,
            corner_radius=3,
            border_width=0.5,
        )
        self._1 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[0]).split(" ")[0], width=120, font=("Calibri bold", 15)
        )
        self._2 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[1]).split(" ")[0], width=120, font=("Calibri ", 13)
        )
        self._3 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[2]).split(" ")[0], width=100, font=("Calibri ", 13)
        )
        self._4 = customtkinter.CTkLabel(master=self.temp, text=data[3], width=140, text_color='gray',  font=("Calibri ", 13), anchor="w")
        self._5 = customtkinter.CTkLabel(master=self.temp, text=data[4], width=100, font=("Calibri ", 13), anchor="w")
        self._6 = customtkinter.CTkLabel(master=self.temp, text=data[5], width=100, font=("Calibri ", 13), anchor="w")
        self._7 = customtkinter.CTkLabel(master=self.temp, text=data[6], width=100, font=("Calibri ", 13))
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
        
        self.pdf_download_btn = customtkinter.CTkButton(
            master=self.temp,
            fg_color=btn_color,
            text="Save PDF",
            text_color='white',
            font=("calibri bold", 16),
            command=lambda: database.retrieve_pdf_file(srn_no=str(data[3])),
        )
        
        
        self._tick.place(x=6, y=10)
        self._tick.configure(
            command=lambda tick=self._tick: self.select_click(data, tick)
        )
        self.ListofCheckBox.append(self._tick)
        self.temp.pack(padx=10, pady=0, ipady=4, fill='both')
        self._1.pack(side="left", pady=1, padx=(40,0))
        self._2.pack(side="left", pady=1, padx=0)
        self._3.pack(side="left", pady=1, padx=0)
        self._4.pack(side="left", pady=1, padx=0)
        self._5.pack(side="left", pady=1, padx=0)
        self._6.pack(side="left", pady=1, padx=0)
        self._7.pack(side="left", pady=1, padx=(0, 0))
        self.pdf_download_btn.pack(side="left",  padx=2, pady=3)
        
    def make_record_frame(self, data):
        self.temp = customtkinter.CTkFrame(
            self.scroll_frame,
            height=60,
            corner_radius=0,
            border_color="#D9D9D9",
            border_width=0.4,
            bg_color="white",
            fg_color="white",
        )
        self.temp.pack(padx=10, pady=0, ipadx=1,ipady=4, anchor=customtkinter.W)
        
        self._tick = customtkinter.CTkCheckBox(
            master=self.temp,
            width=20,
            text="",
            checkbox_height=15,
            checkbox_width=15,
            corner_radius=3,
            border_width=0.5,
        )
        
        
        self._1 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[0]).split(" ")[0], width=120, font=("Calibri bold", 15)
        )
        self._2 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[1]).split(" ")[0], width=120, font=("Calibri ", 13)
        )
        self._3 = customtkinter.CTkLabel(
            master=self.temp, justify="left", anchor="w", text=str(data[2]).split(" ")[0], width=100, font=("Calibri ", 13)
        )
        self._4 = customtkinter.CTkLabel(master=self.temp, text="SRN:  "+ str(data[3]), width=140, text_color='gray',  font=("Calibri ", 13), anchor="w")
        self._5 = customtkinter.CTkLabel(master=self.temp, text=data[4], width=140, font=("Calibri ", 13), anchor="w")
        self._6 = customtkinter.CTkLabel(master=self.temp, text=data[5], width=100, font=("Calibri ", 13), anchor="w")
        self._7 = customtkinter.CTkLabel(master=self.temp, text=data[6], width=100, font=("Calibri ", 13))
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
        
        self.pdf_download_btn = customtkinter.CTkButton(
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
        
        self.pdf_upload_btn = customtkinter.CTkButton(
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
        
        self.user_pic_label = customtkinter.CTkLabel(self.temp, text="",  
                                       width=50, height=50, corner_radius=5)
        
        self._tick.place(x=6, y=20)
        self._tick.configure(
            command=lambda tick=self._tick: self.select_click(data, tick)
        )
        self.ListofCheckBox.append(self._tick)
        
        self._1.grid(row=0, column=1, sticky="W", pady=1, padx=0)
        self._2.grid(row=0, column=2, sticky="W", pady=1, padx=0)
        self._3.grid(row=0, column=3, sticky="W", pady=1, padx=0)
        self._4.grid(row=1, column=1, sticky="W", pady=1, padx=0, columnspan=2)
        self._5.grid(row=0, column=4, sticky="W", pady=1, padx=0)
        self._6.grid(row=0, column=5, sticky="W", pady=1, padx=0)
        self._7.grid(row=0, column=6, sticky="W", pady=1, padx=(0, 0))
        self.pdf_download_btn.grid(row=0, column=7, rowspan=2, sticky="s", padx=2, pady=6)
        self.pdf_upload_btn.grid(row=0, column=8, rowspan=2, sticky="s", padx=2, pady=6)
        self.user_pic_label.grid(row=0, column=0, rowspan=2, pady=0.5, padx=25)
        self.update_idletasks()
        threading.Thread(target=self.getPic, args=(self.user_pic_label, data)).start()
         
    def getPic(self, obj, data):
        img = database.show_images_from_db(str(data[3]),60,76,)
        obj.configure(image=img)
        
    def open_Pdf_file(self, srn):
        # Create a new customtkinter.CTkFileDialog widget
        self.file_dialog = filedialog.askopenfilename(filetypes=[("pdf", "*.pdf")])
        try:
            database.insert_pdf_file(srn, self.file_dialog)
        except Exception as e:
            print(e)
 
    def search_question_paper(self):
        self.list_of_question_paper = database.search_paper(
                clas = self.questionClass.get(),
                session= self.questionSession.get(),
                term = self.questionTerm.get(),
                subjects = self.questionSubject.get()
            )
        self.create_record_question(self.list_of_question_paper)
      
    def create_record_question(self, data_list):
            self.clear_frame()
            if len(data_list) > 0:
                for data in data_list:
                    self.make_record_frame_question(data=data) 
                    
           
    def make_record_frame_question(self, data):
                
        self.temp = customtkinter.CTkFrame(
            self.scroll_frame,
            corner_radius=0,
            border_color="#D9D9D9",
            border_width=0.4,
            bg_color="white",
            fg_color="white",
        )
        self.temp.pack(padx=5, pady=0, fill='both')
        
        customtkinter.CTkLabel(self.temp, text=" ", image = self.pdf_logo).pack(padx=20, side='left')
        self.clas_label0 = customtkinter.CTkLabel(self.temp, text = data[0]+" - ")
        self.clas_label0.pack(padx = 2, pady=0, side='left')
        
        self.clas_label1= customtkinter.CTkLabel(self.temp, text = data[1])
        
        self.clas_label2 = customtkinter.CTkLabel(self.temp, text = data[2]+"  Term")
        
        self.clas_label3 = customtkinter.CTkLabel(self.temp, text = data[3])
        self.clas_label3.pack(padx = 2, pady=0, side='left')
        self.clas_label2.pack(padx = 2, pady=0, side='left')
                
        self.ques_pdf_delete_btn = customtkinter.CTkButton(self.temp, text="", fg_color = "red",hover_color='darkred', image=self.delete_logo, width=40, command=lambda: database.delete_pdf_question((data)))
        self.ques_pdf_delete_btn.pack(padx = 20, pady=10, side='right')
        
        self.ques_pdf_save_btn = customtkinter.CTkButton(self.temp, text="Save",fg_color=btn_color, width=60, text_color='white', command=lambda: database.save_as_pdf_question((data)))
        self.ques_pdf_save_btn.pack(padx = 20, pady=10, side='right')
        
        self.temp.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.temp.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        
        self.clas_label1.pack(padx = 20, pady=10, side='right')
        self.clas_label0.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.clas_label0.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self.clas_label1.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.clas_label1.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self.clas_label2.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.clas_label2.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        self.clas_label3.bind("<Enter>", lambda event, obj=self.temp: self.on_enter(obj))
        self.clas_label3.bind("<Leave>", lambda event, obj=self.temp: self.on_leave(obj))
        
        
    def open_question_paper_file(self, c=None, s=None, t=None, subject=None):
        c = self.questionClass.get()
        s = self.questionSession.get()
        t = self.questionTerm.get()
        subject = self.questionSubject.get()
        
        if c == "" or s == "" or t == "":
            database.rise_error()
            return
        # Create a new customtkinter.CTkFileDialog widget
        self.file_dialog = filedialog.askopenfilename(filetypes=[("pdf", "*.pdf")])
        try:
            database.insert_question_paper_file(c, s, t, subject, self.file_dialog)
        except Exception as e:
            print(e)
            
    def open_settings_window(self):
        self.settings_window = customtkinter.CTkToplevel()
        self.settings_window.grab_set()
        self.settings_window.title("Settings")
        self.settings_window.geometry("300x150")  # Adjust window size as needed

        self.dpi_label = customtkinter.CTkLabel(
            master=self.settings_window, text="Font DPI Scale:"
        )
        self.dpi_label.pack(anchor=customtkinter.N,padx=5, side="left")

        self.dpi_entry = customtkinter.CTkEntry(
            master=self.settings_window, justify="center"
        )
        self.dpi_entry.insert(0, str(dpi_value))  # Set initial value
        self.dpi_entry.pack(pady=10)

        def save_and_reload():
            global dpi_value
            try:
                new_dpi_value = int(self.dpi_entry.get())
                if new_dpi_value > 0:
                    dpi_value = new_dpi_value
                    with open(resource_path("dpi_settings.json"), "w") as f:
                        json.dump({"dpi": dpi_value}, f)

                    customtkinter.set_widget_scaling(dpi_value / 96)
                    root.update()  # Reapply font scaling to main window
                    self.settings_window.destroy()
                else:
                    customtkinter.CTkMessageBox.show_error(
                        "Invalid DPI", "Please enter a positive DPI value."
                    )
            except ValueError:
                customtkinter.CTkMessageBox.show_error(
                    "Invalid Input", "Please enter a valid integer value."
                )
        self.save_button = customtkinter.CTkButton(
        master=self.settings_window, text="Save and Reload", command=save_and_reload)
        self.save_button.pack()
        


   
def main_program():
    root = main_gui()
    
    root.mainloop()
    
class SplashScreen(customtkinter.CTk):
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
        label = customtkinter.CTkLabel(self,text="", image=self.splashLogo, height=300, width=300, corner_radius=50)
        label.pack(pady=50)
       
def destroy():
    for i in range(40):
        root.loading.set((i/100)*4)
        root.update_idletasks()
    root.logoframe.destroy()
    root.create_dashboard_window()
    
def loading_and_destory():
    import mysql_conn as database
          
        
if __name__ == "__main__":
    try:
        with open(resource_path("dpi_settings.json"), "r") as f:
            dpi_settings = json.load(f)
            dpi_value = dpi_settings.get("dpi", 96)  # Default to 96 if not found
    except FileNotFoundError:
        dpi_value = 96
        
    try:
        customtkinter.set_widget_scaling(dpi_value / 96)
        root = main_gui()
        root.after(500, loading_and_destory)
        root.after(1000, destroy)
        root.mainloop()

    except Exception as e:
        print(f"Error: {e}")
        
        
        