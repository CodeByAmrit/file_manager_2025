import os, sys
from tkinter import ttk, filedialog, END
from customtkinter import CTkToplevel, CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel, TRUE, CTkComboBox, CTkScrollableFrame
from PIL import Image
import mysql_conn as database
import user_pic_upload as upload


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def create_word_file(data, data1, data2, data3, data4):
    replacements = {"SName": str(data[0]), "SClass": str(data[3]), "SSec": " ",
                  "SRoll": str(data[2]), "SParent": str(data[1]), "SSession": str(data[5]),
                  
                  "Eng1": str(data1[0]), "Hindi1": str(data1[1]), "Maths1": str(data1[2]), "Sst1": str(data1[3]), "Science1": str(data1[4]), "Comp1": str(data1[5]), "Draw1": str(data1[6]),"Gn1": str(data1[7]), "Grand1": str(data1[8]), "%1": str(data1[9]), "Rank1": str(data1[10]),
                  "Eng2": str(data2[0]), "Hindi2": str(data2[1]), "Maths2": str(data2[2]), "Sst2": str(data2[3]), "Science2": str(data2[4]), "Comp2": str(data2[5]), "Draw2": str(data2[6]),"Gn2": str(data2[7]), "Grand2": str(data2[8]), "%2": str(data2[9]), "Rank2": str(data2[10]),
                  "Eng3": str(data3[0]), "Hindi3": str(data3[1]), "Maths3": str(data3[2]), "Sst3": str(data3[3]), "Science3": str(data3[4]), "Comp3": str(data3[5]), "Draw3": str(data3[6]),"Gn3": str(data3[7]), "Grand3": str(data3[8]), "%3": str(data3[9]), "Rank3": str(data3[10]),
                  "maxEng": str(data4[0]), "maxHindi": str(data4[1]), "maxMaths": str(data4[2]), "maxSst": str(data4[3]), "maxScience": str(data4[4]), "maxComputer": str(data4[5]), "maxDrawing": str(data4[6]),"maxGN": str(data4[7]), "maxTotal": str(data4[8]), "maxPercentage": str("100"), "maxRank": str(data4[10]),
                   "attendance": data4[9],
                    }
    user_home = os.path.expanduser("~")
    savePath = os.path.join(user_home, "Documents/files")
    try:
        database.replace_text_in_docx(resource_path("bajranj.docx"), replacements)
                
    except Exception as e:
        print(f"Error in worker process: {e}")



class modifyDetails(CTkFrame):
    def open_Pdf_file(self, srn):
        self.file_dialog = filedialog.askopenfilename(filetypes=[("pdf", "*.pdf")])

        try:
            database.insert_pdf_file(srn, self.file_dialog)
        except Exception as e:
            print(e)

    def runUpdate(self):
        database.update_student(
            self.Name.get(),
            self.Father.get(),
            self.Mother.get(),
            self.SRN.get(),
            self.PEN.get(),
            self.Admission.get(),
            self.Clas.get(),
            self.session.get(),
            self.Roll.get(),
        )

    def createImage(self, path, w, h):
        temp = CTkImage(
            light_image=Image.open(path), dark_image=Image.open(path), size=(w, h)
        )
        return temp
    
    def custom_terms_input1(self, frame):
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
            frame, style="Round.TEntry", font=("Verdana", 12), takefocus=True, width=5
        )
        self.marks_input_list1.append(inputEntry)
        return inputEntry
    
    def custom_terms_input2(self, frame):
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
            frame, style="Round.TEntry", font=("Verdana", 12), takefocus=True, width=5
        )
        self.marks_input_list2.append(inputEntry)
        return inputEntry
    
    def custom_terms_input3(self, frame):
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
            frame, style="Round.TEntry", font=("Verdana", 12), takefocus=True, width=5
        )
        self.marks_input_list3.append(inputEntry)
        return inputEntry
    
    def custom_terms_input4(self, frame):
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
            frame, style="Round.TEntry", font=("Verdana", 12), takefocus=True, width=5
        )
        self.marks_input_list4.append(inputEntry)
        return inputEntry
    
    def insert_in_marks1(self):
        
        list1 = []
        list1.append(self.english_first_entry.get())
        list1.append(self.hindi_first_entry.get())
        list1.append(self.maths_first_entry.get())
        list1.append(self.sst_first_entry.get())
        list1.append(self.science_first_entry.get())
        list1.append(self.computer_first_entry.get())
        list1.append(self.drawing_first_entry.get())
        list1.append(self.general_first_entry.get())
        list1.append(self.grand_first_entry.get())
        list1.append(self.percentage_first_entry.get())
        list1.append(self.rank_first_entry.get())
        
        database.insert_into_marks1(self,self.SRN.get(), list1)
        # print(self.SRN.get(), list1)
        
    def insert_in_marks2(self):
        
        list2 = []
        list2.append(self.english_second_entry.get())
        list2.append(self.hindi_second_entry.get())
        list2.append(self.maths_second_entry.get())
        list2.append(self.sst_second_entry.get())
        list2.append(self.science_second_entry.get())
        list2.append(self.computer_second_entry.get())
        list2.append(self.drawing_second_entry.get())
        list2.append(self.general_second_entry.get())
        list2.append(self.grand_second_entry.get())
        list2.append(self.percentage_second_entry.get())
        list2.append(self.rank_second_entry.get())
        
        database.insert_into_marks2(self,self.SRN.get(), list2)
        # print(self.SRN.get(), list2)
        
    def insert_in_marks3(self):
        list3 = []
        list3.append(self.english_third_entry.get())
        list3.append(self.hindi_third_entry.get())
        list3.append(self.maths_third_entry.get())
        list3.append(self.sst_third_entry.get())
        list3.append(self.science_third_entry.get())
        list3.append(self.computer_third_entry.get())
        list3.append(self.drawing_third_entry.get())
        list3.append(self.general_third_entry.get())
        list3.append(self.grand_third_entry.get())
        list3.append(self.percentage_third_entry.get())
        list3.append(self.rank_third_entry.get())
        
        database.insert_into_marks3(self,self.SRN.get(), list3)
        # print(self.SRN.get(), list1)
        
    def insert_in_maximum(self):
        listmax = []
        listmax.append(self.english_max_entry.get())
        listmax.append(self.hindi_max_entry.get())
        listmax.append(self.maths_max_entry.get())
        listmax.append(self.sst_max_entry.get())
        listmax.append(self.science_max_entry.get())
        listmax.append(self.computer_max_entry.get())
        listmax.append(self.drawing_max_entry.get())
        listmax.append(self.general_max_entry.get())
        listmax.append(self.grand_max_entry.get())
        listmax.append(self.percentage_max_entry.get())
        listmax.append(self.rank_max_entry.get())
        
        database.insert_into_maximum(self,self.SRN.get(), listmax)
        # print(self.SRN.get(), list1)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.marks_input_list1 = []
        self.marks_input_list2 = []
        self.marks_input_list3 = []
        self.marks_input_list4 = []
        
        self.class_name_list = [ "NURSERY", "KG", "1ST", "2ND", "3RD", "4TH", "5TH", "6TH", "7TH", "8TH", "9TH", "10TH", "11TH", "12TH"]
        self.session_list = [str(str(i) + " - " + str(i+1)) for i in range(2010, 2030)]
        
        self.pdf_logo_upload = self.createImage(
            resource_path("icons/pdf-upload.png"), 24, 24
        )
        
        self.trashLogo = self.createImage(resource_path("icons/trash.png"), 24, 24)
        self.close_logo = self.createImage(resource_path("icons/arrow.png"), 24, 24)
        
        self.file_dialog = None

        self.label = CTkLabel(
            self,
            text="Edit Student Details",
            bg_color="white",
            fg_color="#0E4175",
            text_color="white",
            corner_radius=4,
        )
        self.label.pack(fill="both", padx=20, pady=10)

        self.framePhoto = CTkFrame(self, fg_color="white", width=150)
        self.framePhoto.pack(fill="both", expand=TRUE, pady=10, padx=(20, 20), side='left')

        self.frame = CTkFrame(self, fg_color="white")
        self.frame.pack(fill="both", expand=TRUE, pady=10, padx=(0, 20), side='left')

        self.userPic = CTkLabel(self.framePhoto, text="")
        self.userPic.pack(pady=10, padx=20)

        self.change_photo = CTkButton(
            self.framePhoto,
            text="Change Photo",
            compound="left",
            fg_color="#098FF0"
        )
        self.change_photo.pack(pady=10, padx=20)
        
        self.Save_photo = CTkButton(
            self.framePhoto,
            text="Save Photo",
            compound="left",
            fg_color="#098FF0"
        )
        self.Save_photo.pack(pady=10, padx=20)
        
        
        
        self.deleteRecord = CTkButton(
            self.framePhoto,
            text="Delete Record",
            image=self.trashLogo,
            compound="left",
            fg_color="red",
            text_color="white",
        )
        self.deleteRecord.pack(pady=10, padx=20)

        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Name",
            bg_color="lightgray",
            width=120,
        ).grid(row=0, column=0, padx=(30, 0), pady=(20,0))
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Father's Name",
            bg_color="lightgray",
            width=120,
        ).grid(row=1, column=0, padx=(30, 0))
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Mother's Name",
            bg_color="lightgray",
            width=120,
        ).grid(row=2, column=0, padx=(30, 0))
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="SRN No",
            bg_color="lightgray",
            width=120,
        ).grid(row=3, column=0, padx=(30, 0))
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="PEN No",
            bg_color="lightgray",
            width=120,
        ).grid(row=4, column=0, padx=(30, 0))
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Admission No",
            bg_color="lightgray",
            width=120,
        ).grid(row=5, column=0, padx=(30, 0))
        
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Class",
            bg_color="lightgray",
            width=120,
        ).grid(row=6, column=0, padx=(30, 0))
        
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Session",
            bg_color="lightgray",
            width=120,
        ).grid(row=7, column=0, padx=(30, 0))
        
        CTkLabel(
            self.frame,
            fg_color="white",
            justify="left",
            anchor="w",
            text="Roll Number",
            bg_color="lightgray",
            width=120,
        ).grid(row=8, column=0, padx=(30, 0))
        
        self.Name = CTkEntry(
            self.frame,
        )
        self.Father = CTkEntry(
            self.frame,
        )
        self.Mother = CTkEntry(
            self.frame,
        )
        self.SRN = CTkEntry(
            self.frame,
        )
        self.PEN = CTkEntry(
            self.frame,
        )
        self.Admission = CTkEntry(
            self.frame,
        )
        self.Roll = CTkEntry(
            self.frame,
        )
        
        self.Clas = CTkComboBox(
            self.frame,
            values=self.class_name_list,
        )
        
        self.session = CTkComboBox(
            self.frame,
            values=self.session_list,
        )
        
        self.Name.grid(padx=(30, 20), pady=5, row=0, column=1)
        self.Father.grid(padx=(30, 20), pady=5, row=1, column=1)
        self.Mother.grid(padx=(30, 20), pady=5, row=2, column=1)
        self.SRN.grid(padx=(30, 20), pady=5, row=3, column=1)
        self.PEN.grid(padx=(30, 20), pady=5, row=4, column=1)
        self.Admission.grid(padx=(30, 20), pady=5, row=5, column=1)
        self.Clas.grid(padx=(30, 20), pady=5, row=6, column=1)
        self.session.grid(padx=(30, 20), pady=5, row=7, column=1)
        self.Roll.grid(padx=(30, 20), pady=5, row=8, column=1)

        self.UploadPDF_btn = CTkButton(
            self.frame,
            text="Upload PDF",
            width=120,
            image=self.pdf_logo_upload,
            compound="left",
            fg_color="#098FF0",
            command=lambda: self.open_Pdf_file(str(self.SRN.get())),
        )
        self.UploadPDF_btn.grid(row=9, column=0, padx=(20, 0), pady=10)

        self.refreshImg = self.createImage(resource_path("icons/refresh.png"), 16, 16)
        self.UpdateBtn = CTkButton(
            self.frame,
            text="Change Details",
            width=120,
            image=self.refreshImg,
            fg_color="#098FF0",
            command=self.runUpdate,
        )
        self.UpdateBtn.grid(row=9, column=1, padx=(20, 0), pady=10)
        
        self.generate_btn = CTkButton(
            self.frame,
            text="Create Certificate",
            width=120,
            fg_color="#098FF0"
            
        )
        self.generate_btn.grid(row=10, column=0, padx=(20, 0), pady=10)
        
        self.term_frame = CTkScrollableFrame(master=self, fg_color='white', width=600)
        self.term_frame.pack(side='left', padx=(0,20), fill="both", pady=10)
        # self.term_frame.pack_propagate(False)
        # self.term_frame.grid_propagate(False)
        
        # First Term 
        self.first_term_frame = CTkFrame(
            self.term_frame,
            border_width=1,
            border_color="#E3E3E3",
            corner_radius=5,
            bg_color="white",
            fg_color="white",
        )
        self.first_term_frame.pack(fill="both", pady=15, padx=15)
        self.first_term_frame.pack_propagate(False)

        self.label1 = CTkLabel(
            master=self.term_frame,
            text="First Term Marks",
            font=("Calibri", 16)
        )
        self.label1.place(x=30,y=3)

        
        self.english_first_label = CTkLabel(master=self.first_term_frame, text="English")
        self.english_first_label.grid(row=0, column=0, padx=10, pady=(8,0)) 
        
        self.hindi_first_label = CTkLabel(master=self.first_term_frame, text="Hindi")
        self.hindi_first_label.grid(row=0, column=1, padx=10, pady=(8,0)) 
        
        self.maths_first_label = CTkLabel(master=self.first_term_frame, text="Maths")
        self.maths_first_label.grid(row=0, column=2, padx=10, pady=(8,0)) 
        
        self.sst_first_label = CTkLabel(master=self.first_term_frame, text="SSt")
        self.sst_first_label.grid(row=0, column=3, padx=10, pady=(8,0)) 
        
        self.science_first_label = CTkLabel(master=self.first_term_frame, text="Science")
        self.science_first_label.grid(row=0, column=4, padx=10, pady=(8,0)) 
        
        self.computer_first_label = CTkLabel(master=self.first_term_frame, text="Computer")
        self.computer_first_label.grid(row=0, column=5, padx=10, pady=(8,0)) 
        
        self.drawing_first_label = CTkLabel(master=self.first_term_frame, text="Drawing")
        self.drawing_first_label.grid(row=0, column=6, padx=10, pady=(8,0)) 
        
        self.general_first_label = CTkLabel(master=self.first_term_frame, text="GK")
        self.general_first_label.grid(row=2, column=0, padx=10, pady=(8,0)) 
        
        self.grand_first_label = CTkLabel(master=self.first_term_frame, text="Grand Total")
        self.grand_first_label.grid(row=2, column=1, padx=10, pady=(8,0)) 
        
        self.percentage_first_label = CTkLabel(master=self.first_term_frame, text="% age")
        self.percentage_first_label.grid(row=2, column=2, padx=10, pady=(8,0)) 
        
        self.rank_first_label = CTkLabel(master=self.first_term_frame, text="Rank")
        self.rank_first_label.grid(row=2, column=3, padx=10, pady=(8,0)) 
        
        # -------------------- Button Save >>>>>>>>>>>>>>>
        self.first_calculate_btn = CTkButton(master=self.first_term_frame, text='Calculate', width=20, fg_color="#098FF0")
        self.first_calculate_btn.grid(row=3, column=4, padx=10, pady=10) 
        
        self.first_save_btn = CTkButton(master=self.first_term_frame, text='Save', width=20, command=self.insert_in_marks1, fg_color="#098FF0")
        self.first_save_btn.grid(row=3, column=6, padx=10, pady=10) 
                
        # -----------------  Entry --------------------- >
        self.english_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.english_first_entry.grid(row=1, column=0, padx=10, pady=4) 
        
        self.hindi_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.hindi_first_entry.grid(row=1, column=1, padx=10, pady=4) 
        
        self.maths_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.maths_first_entry.grid(row=1, column=2, padx=10, pady=4) 
        
        self.sst_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.sst_first_entry.grid(row=1, column=3, padx=10, pady=4) 
        
        self.science_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.science_first_entry.grid(row=1, column=4, padx=10, pady=4) 
        
        self.computer_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.computer_first_entry.grid(row=1, column=5, padx=10, pady=4) 
        
        self.drawing_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.drawing_first_entry.grid(row=1, column=6, padx=10, pady=4) 
        
        self.general_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.general_first_entry.grid(row=3, column=0, padx=10, pady=4) 
        
        self.grand_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.grand_first_entry.grid(row=3, column=1, padx=10, pady=4) 
        
        self.percentage_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.percentage_first_entry.grid(row=3, column=2, padx=10, pady=4) 
        
        self.rank_first_entry = self.custom_terms_input1(self.first_term_frame)
        self.rank_first_entry.grid(row=3, column=3, padx=10, pady=4) 
        
        #---------------------------------------------------------------------
        
        # Second Term 
        self.second_term_frame = CTkFrame(
            self.term_frame,
            border_width=1,
            border_color="#E3E3E3",
            corner_radius=5,
            bg_color="white",
            fg_color="white",
        )
        self.second_term_frame.pack(fill="both", pady=15, padx=15)
        self.second_term_frame.pack_propagate(False)
        
        self.english_second_label = CTkLabel(master=self.second_term_frame, text="English")
        self.english_second_label.grid(row=0, column=0, padx=10, pady=(8,0)) 
        
        self.hindi_second_label = CTkLabel(master=self.second_term_frame, text="Hindi")
        self.hindi_second_label.grid(row=0, column=1, padx=10, pady=(8,0)) 
        
        self.maths_second_label = CTkLabel(master=self.second_term_frame, text="Maths")
        self.maths_second_label.grid(row=0, column=2, padx=10, pady=(8,0)) 
        
        self.sst_second_label = CTkLabel(master=self.second_term_frame, text="SSt")
        self.sst_second_label.grid(row=0, column=3, padx=10, pady=(8,0)) 
        
        self.science_second_label = CTkLabel(master=self.second_term_frame, text="Science")
        self.science_second_label.grid(row=0, column=4, padx=10, pady=(8,0)) 
        
        self.computer_second_label = CTkLabel(master=self.second_term_frame, text="Computer")
        self.computer_second_label.grid(row=0, column=5, padx=10, pady=(8,0)) 
        
        self.drawing_second_label = CTkLabel(master=self.second_term_frame, text="Drawing")
        self.drawing_second_label.grid(row=0, column=6, padx=10, pady=(8,0)) 
        
        self.general_second_label = CTkLabel(master=self.second_term_frame, text="GK")
        self.general_second_label.grid(row=2, column=0, padx=10, pady=(8,0)) 
        
        self.grand_second_label = CTkLabel(master=self.second_term_frame, text="Grand Total")
        self.grand_second_label.grid(row=2, column=1, padx=10, pady=(8,0)) 
        
        self.percentage_second_label = CTkLabel(master=self.second_term_frame, text="% age")
        self.percentage_second_label.grid(row=2, column=2, padx=10, pady=(8,0)) 
        
        self.rank_second_label = CTkLabel(master=self.second_term_frame, text="Rank")
        self.rank_second_label.grid(row=2, column=3, padx=10, pady=(8,0)) 
        
        # -------------------- Button Save >>>>>>>>>>>>>>>
        self.second_calculate_btn = CTkButton(master=self.second_term_frame, text='Calculate', width=20, fg_color="#098FF0")
        self.second_calculate_btn.grid(row=3, column=4, padx=10, pady=10) 
        
        self.second_save_btn = CTkButton(master=self.second_term_frame, text='Save', width=20, command=self.insert_in_marks2, fg_color="#098FF0")
        self.second_save_btn.grid(row=3, column=6, padx=10, pady=10) 
                
        # -----------------  Entry --------------------- >
        self.english_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.english_second_entry.grid(row=1, column=0, padx=10, pady=4) 
        
        self.hindi_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.hindi_second_entry.grid(row=1, column=1, padx=10, pady=4) 
        
        self.maths_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.maths_second_entry.grid(row=1, column=2, padx=10, pady=4) 
        
        self.sst_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.sst_second_entry.grid(row=1, column=3, padx=10, pady=4) 
        
        self.science_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.science_second_entry.grid(row=1, column=4, padx=10, pady=4) 
        
        self.computer_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.computer_second_entry.grid(row=1, column=5, padx=10, pady=4) 
        
        self.drawing_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.drawing_second_entry.grid(row=1, column=6, padx=10, pady=4) 
        
        self.general_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.general_second_entry.grid(row=3, column=0, padx=10, pady=4) 
        
        self.grand_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.grand_second_entry.grid(row=3, column=1, padx=10, pady=4) 
        
        self.percentage_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.percentage_second_entry.grid(row=3, column=2, padx=10, pady=4) 
        
        self.rank_second_entry = self.custom_terms_input2(self.second_term_frame)
        self.rank_second_entry.grid(row=3, column=3, padx=10, pady=4) 
        
        #------------------------ Final Trerm ---------------------------------------
        # final Term 
        self.third_term_frame = CTkFrame(
            self.term_frame,
            border_width=1,
            border_color="#E3E3E3",
            corner_radius=5,
            bg_color="white",
            fg_color="white",
        )
        self.third_term_frame.pack(fill="both", pady=15, padx=15)
        self.third_term_frame.pack_propagate(False)

        self.english_third_label = CTkLabel(master=self.third_term_frame, text="English")
        self.english_third_label.grid(row=0, column=0, padx=10, pady=(8,0)) 
        
        self.hindi_third_label = CTkLabel(master=self.third_term_frame, text="Hindi")
        self.hindi_third_label.grid(row=0, column=1, padx=10, pady=(8,0)) 
        
        self.maths_third_label = CTkLabel(master=self.third_term_frame, text="Maths")
        self.maths_third_label.grid(row=0, column=2, padx=10, pady=(8,0)) 
        
        self.sst_third_label = CTkLabel(master=self.third_term_frame, text="SSt")
        self.sst_third_label.grid(row=0, column=3, padx=10, pady=(8,0)) 
        
        self.science_third_label = CTkLabel(master=self.third_term_frame, text="Science")
        self.science_third_label.grid(row=0, column=4, padx=10, pady=(8,0)) 
        
        self.computer_third_label = CTkLabel(master=self.third_term_frame, text="Computer")
        self.computer_third_label.grid(row=0, column=5, padx=10, pady=(8,0)) 
        
        self.drawing_third_label = CTkLabel(master=self.third_term_frame, text="Drawing")
        self.drawing_third_label.grid(row=0, column=6, padx=10, pady=(8,0)) 
        
        self.general_third_label = CTkLabel(master=self.third_term_frame, text="GK")
        self.general_third_label.grid(row=2, column=0, padx=10, pady=(8,0)) 
        
        self.grand_third_label = CTkLabel(master=self.third_term_frame, text="Grand Total")
        self.grand_third_label.grid(row=2, column=1, padx=10, pady=(8,0)) 
        
        self.percentage_third_label = CTkLabel(master=self.third_term_frame, text="% age")
        self.percentage_third_label.grid(row=2, column=2, padx=10, pady=(8,0)) 
        
        self.rank_third_label = CTkLabel(master=self.third_term_frame, text="Rank")
        self.rank_third_label.grid(row=2, column=3, padx=10, pady=(8,0)) 
        
        # -------------------- Button Save >>>>>>>>>>>>>>>
        self.third_calculate_btn = CTkButton(master=self.third_term_frame, text='Calculate', width=20, fg_color="#098FF0")
        self.third_calculate_btn.grid(row=3, column=4, padx=10, pady=10) 
        
        self.third_save_btn = CTkButton(master=self.third_term_frame, text='Save', width=20, command=self.insert_in_marks3, fg_color="#098FF0")
        self.third_save_btn.grid(row=3, column=6, padx=10, pady=10) 
                
        # -----------------  Entry --------------------- >
        self.english_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.english_third_entry.grid(row=1, column=0, padx=10, pady=4) 
        
        self.hindi_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.hindi_third_entry.grid(row=1, column=1, padx=10, pady=4) 
        
        self.maths_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.maths_third_entry.grid(row=1, column=2, padx=10, pady=4) 
        
        self.sst_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.sst_third_entry.grid(row=1, column=3, padx=10, pady=4) 
        
        self.science_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.science_third_entry.grid(row=1, column=4, padx=10, pady=4) 
        
        self.computer_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.computer_third_entry.grid(row=1, column=5, padx=10, pady=4) 
        
        self.drawing_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.drawing_third_entry.grid(row=1, column=6, padx=10, pady=4) 
        
        self.general_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.general_third_entry.grid(row=3, column=0, padx=10, pady=4) 
        
        self.grand_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.grand_third_entry.grid(row=3, column=1, padx=10, pady=4) 
        
        self.percentage_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.percentage_third_entry.grid(row=3, column=2, padx=10, pady=4) 
        
        self.rank_third_entry = self.custom_terms_input3(self.third_term_frame)
        self.rank_third_entry.grid(row=3, column=3, padx=10, pady=4) 
        
        #------------------------ Max marks ---------------------------------------
        # max Term 
        self.max_term_frame = CTkFrame(
            self.term_frame,
            border_width=1,
            border_color="#E3E3E3",
            corner_radius=5,
            bg_color="white",
            fg_color="white",
        )
        self.max_term_frame.pack(fill="both", pady=15, padx=15)
        self.max_term_frame.pack_propagate(False)
        
        self.english_max_label = CTkLabel(master=self.max_term_frame, text="English")
        self.english_max_label.grid(row=0, column=0, padx=10, pady=(8,0)) 
        
        self.hindi_max_label = CTkLabel(master=self.max_term_frame, text="Hindi")
        self.hindi_max_label.grid(row=0, column=1, padx=10, pady=(8,0)) 
        
        self.maths_max_label = CTkLabel(master=self.max_term_frame, text="Maths")
        self.maths_max_label.grid(row=0, column=2, padx=10, pady=(8,0)) 
        
        self.sst_max_label = CTkLabel(master=self.max_term_frame, text="SSt")
        self.sst_max_label.grid(row=0, column=3, padx=10, pady=(8,0)) 
        
        self.science_max_label = CTkLabel(master=self.max_term_frame, text="Science")
        self.science_max_label.grid(row=0, column=4, padx=10, pady=(8,0)) 
        
        self.computer_max_label = CTkLabel(master=self.max_term_frame, text="Computer")
        self.computer_max_label.grid(row=0, column=5, padx=10, pady=(8,0)) 
        
        self.drawing_max_label = CTkLabel(master=self.max_term_frame, text="Drawing")
        self.drawing_max_label.grid(row=0, column=6, padx=10, pady=(8,0)) 
        
        self.general_max_label = CTkLabel(master=self.max_term_frame, text="GK")
        self.general_max_label.grid(row=2, column=0, padx=10, pady=(8,0)) 
        
        self.grand_max_label = CTkLabel(master=self.max_term_frame, text="Grand Total")
        self.grand_max_label.grid(row=2, column=1, padx=10, pady=(8,0)) 
        
        self.percentage_max_label = CTkLabel(master=self.max_term_frame, text="Attendance")
        self.percentage_max_label.grid(row=2, column=2, padx=10, pady=(8,0)) 
        
        self.rank_max_label = CTkLabel(master=self.max_term_frame, text="Rank")
        self.rank_max_label.grid(row=2, column=3, padx=10, pady=(8,0)) 
        
        # -------------------- Button Save >>>>>>>>>>>>>>>
        self.max_calculate_btn = CTkButton(master=self.max_term_frame, text='Calculate', width=20, fg_color="#098FF0")
        self.max_calculate_btn.grid(row=3, column=4, padx=10, pady=10) 
        
        self.max_save_btn = CTkButton(master=self.max_term_frame, text='Save', width=20, command=self.insert_in_maximum, fg_color="#098FF0")
        self.max_save_btn.grid(row=3, column=6, padx=10, pady=10) 
                
        # -----------------  Entry --------------------- >
        self.english_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.english_max_entry.grid(row=1, column=0, padx=10, pady=4) 
        
        self.hindi_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.hindi_max_entry.grid(row=1, column=1, padx=10, pady=4) 
        
        self.maths_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.maths_max_entry.grid(row=1, column=2, padx=10, pady=4) 
        
        self.sst_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.sst_max_entry.grid(row=1, column=3, padx=10, pady=4) 
        
        self.science_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.science_max_entry.grid(row=1, column=4, padx=10, pady=4) 
        
        self.computer_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.computer_max_entry.grid(row=1, column=5, padx=10, pady=4) 
        
        self.drawing_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.drawing_max_entry.grid(row=1, column=6, padx=10, pady=4) 
        
        self.general_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.general_max_entry.grid(row=3, column=0, padx=10, pady=4) 
        
        self.grand_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.grand_max_entry.grid(row=3, column=1, padx=10, pady=4) 
        
        self.percentage_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.percentage_max_entry.grid(row=3, column=2, padx=10, pady=4) 
        
        self.rank_max_entry = self.custom_terms_input4(self.max_term_frame)
        self.rank_max_entry.grid(row=3, column=3, padx=10, pady=4) 
        
        
        self.label2 = CTkLabel(
            master=self.term_frame,
            text="Second Term Marks",
            font=("Calibri", 16)
        )
        self.label2.place(x=30,y=185)
        
        self.label3 = CTkLabel(
            master=self.term_frame,
            text="Third Term Marks",
            font=("Calibri", 16)
        )
        self.label3.place(x=30,y=370)
        
        self.label4 = CTkLabel(
            master=self.term_frame,
            text="Maximum Marks",
            font=("Calibri", 16)
        )
        self.label4.place(x=30,y=555) 
        
        button = CTkButton(self, fg_color='white', hover_color='white',text='', corner_radius=0,
                           image=self.close_logo, command=self.close_self, width=50)
        button.place(x=0, y=0)
    
    def close_self(self):
        self.place_forget()
        self.destroy()
        
    
def photo_change(srn):
    photo_window = CTkToplevel()
    photo_window.grab_set()
    change_photo_gui = upload.ProfilePicEditor(photo_window)
    change_photo_gui.saveBtn(srn)
    
        
def modify_record(self, data_list):
    key = data_list[3]
    data = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    
    data.append(data_list[0])
    data.append(data_list[1])
    data.append(data_list[8])
    data.append(data_list[6])
    data.append(data_list[7])
    data.append(data_list[7])
    
    self.pop_up = modifyDetails(master=self, corner_radius=10, height=600)
    self.pop_up.place(x=20, y=20)
    # self.pop_up.title(str(data_list[0]) + " Details")
    self.pop_up.Name.insert(0, data_list[0])
    self.pop_up.Father.insert(0, data_list[1])
    self.pop_up.Mother.insert(0, data_list[2])
    self.pop_up.SRN.insert(0, key) 
    self.pop_up.PEN.insert(0, data_list[4])
    self.pop_up.Admission.insert(0, data_list[5])
    self.pop_up.Clas.set(str(data_list[6]))
    self.pop_up.session.set(str(data_list[7]))
    self.pop_up.Roll.insert(0, data_list[8])
    # self.pop_up.SRN.configure(state="disabled")
    img = database.show_images_from_db(str(key))
    self.pop_up.userPic.configure(
        image=img
    )
    self.pop_up.Save_photo.configure(
        command=database.save_image
    )
    
    
    self.pop_up.change_photo.configure(
        command=lambda: photo_change(str(key))
    )
    self.pop_up.deleteRecord.configure(
        command=lambda: database.deleteStudent(srn=str(key))
    )
    
    
    #get first term marks
    first_term_marks = list(database.get_first_term_marks(key))
    second_term_marks = list(database.get_second_term_marks(key))
    third_term_marks = list(database.get_third_term_marks(key))
    max_marks = list(database.get_max_term_marks(key))
    
    i=1
    if len(first_term_marks) != 0:  
        for obj in self.pop_up.marks_input_list1:
            obj.insert(0, first_term_marks[0][i])
            data1.append(first_term_marks[0][i])
            i+=1
        i = 1

    if len(second_term_marks) != 0:  
        for obj in self.pop_up.marks_input_list2:
            obj.insert(0, second_term_marks[0][i])
            data2.append(second_term_marks[0][i])
            i+=1
        i = 1
            
    if len(third_term_marks) != 0: 
        for obj in self.pop_up.marks_input_list3:
            obj.insert(0, third_term_marks[0][i])
            data3.append(third_term_marks[0][i])
            i+=1
        i = 1
        
    if len(max_marks) != 0:
        for obj in self.pop_up.marks_input_list4:
            obj.insert(0, max_marks[0][i])
            data4.append(max_marks[0][i])
            i+=1
        i = 1
    
    self.pop_up.generate_btn.configure(command=lambda: create_word_file(data, data1, data2, data3, data4))
    
    self.pop_up.first_calculate_btn.configure(command = lambda: calculate(self.pop_up.marks_input_list1, self.pop_up.marks_input_list4))
    self.pop_up.second_calculate_btn.configure(command = lambda: calculate(self.pop_up.marks_input_list2, self.pop_up.marks_input_list4))
    self.pop_up.third_calculate_btn.configure(command = lambda: calculate(self.pop_up.marks_input_list3, self.pop_up.marks_input_list4))
    self.pop_up.max_calculate_btn.configure(command = lambda: calculateMax(self.pop_up.marks_input_list4))
            
def calculate(input_list, max_list):
    total = 0
    i = 0
    for obj in input_list:
        try:
            if i < 8:
                value = int(obj.get())
                total  = total + value
                i += 1
            else:
                input_list[8].delete(0, END)
                input_list[8].insert(0, total)
                
                percent = (float(total) / float(max_list[8].get())) * 100
                
                input_list[9].delete(0, END)
                input_list[9].insert(0, percent)
                break
        except:
            i += 1
                
def calculateMax(input_list):
    total = 0
    i = 0
    for obj in input_list:
        try:
            if i < 8:
                value = int(obj.get())
                total  = total + value
                i += 1
            else:
                input_list[8].delete(0, END)
                input_list[8].insert(0, total)
                break
        except:
            i += 1
    