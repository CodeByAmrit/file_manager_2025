import os, tempfile, sys
import customtkinter as ctk
from tkinter import filedialog, Canvas, messagebox
from PIL import ImageTk, Image
from mysql_conn import conn


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ProfilePicEditor:
    def saveBtn(self, srn):
        ctk.CTkButton(self.userPhotoFrame, text="save",command=lambda : self.update_photo(srn)).pack()
        
    def __init__(self, root):
        self.root = root
        img_resized = Image.open(resource_path("icons/upload_icon.png")).resize(
            (200, 200), Image.Resampling.LANCZOS
        )
        self.icon = ImageTk.PhotoImage(img_resized)

        self.img_path = ""
        self.img_original = Image.open(resource_path("icons/default.jpg"))
        self.img_preview = None
        self.scale_factor = 1.0
        self.position = (0, 0)

        self.userPhotoFrame = ctk.CTkFrame(
            self.root, width=300, height=380, fg_color="white", corner_radius=12
        )
        self.userPhotoFrame.grid(
            row=0, column=4, columnspan=3, rowspan=6, padx=44, pady=8
        )

        self.canvas = Canvas(
            self.userPhotoFrame,
            width=300,
            height=380,
            bg="white",
            background="white",
        )
        self.canvas.pack(pady=8, padx=8)

        self.canvas.create_image(50, 100, anchor="nw", image=self.icon)

        self.btn_upload = ctk.CTkButton(
            self.userPhotoFrame, text="Choose Photo", command=self.upload_image
        )
        self.btn_upload.pack(pady=3)

    def resize_and_save_temp(self, image_path, new_size, ext):
        original_image = Image.open(image_path)
        resized_image = original_image.resize(new_size)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
        resized_image.save(temp_file.name)
        return temp_file.name

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg")]
        )
        extension = str("." + file_path.split(".")[-1])

        file_path = self.resize_and_save_temp(file_path, [300, 380], extension)

        if file_path:
            self.img_path = file_path
            self.img_original = Image.open(file_path)

            self.show_image()

    def show_image(self):
        if self.img_original:
            img_resized = self.img_original.resize((300, 380), Image.Resampling.LANCZOS)
            self.img_preview = ImageTk.PhotoImage(img_resized)

            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor="nw", image=self.img_preview)

            self.canvas.bind("<B1-Motion>", self.move_image)
            self.canvas.bind("<MouseWheel>", self.scale_image)

    def move_image(self, event):
        dx = event.x - self.position[0]
        dy = event.y - self.position[1]
        self.position = (event.x, event.y)

        self.canvas.move("all", dx, dy)

    def scale_image(self, event):
        factor = 1.2 if event.delta > 0 else 0.8
        self.scale_factor *= factor

        self.canvas.scale("all", 0, 0, factor, factor)

    def crop_and_save(self, srn):
        if self.img_original:
            x, y = self.canvas.coords("all")[:2]
            x = -x / self.scale_factor
            y = -y / self.scale_factor

            img_cropped = self.img_original.crop(
                (x, y, x + 300 / self.scale_factor, y + 380 / self.scale_factor)
            )

            # conn = sqlite3.connect(resource_path("database/student_database.db"))
            
            cursor = conn.cursor(prepared=True)

            img_bytes = img_cropped.tobytes()

            try:
                cursor.execute(
                    "INSERT INTO photo (id, image) VALUES (?, ?)",
                    (
                        srn,
                        img_bytes,
                    ),
                )
                conn.commit()

                # print("Image cropped and saved to database.")
                os.remove(self.img_path)
                return 1
            except conn.IntegrityError as e:

                return e
            except Exception as e:

                return e
            
    def update_photo(self, srn_no):
        res = self.delete_photo(srn_no)
        if res == 1:
            update_status = self.crop_and_save(srn_no)
            if update_status == 1:
                messagebox.showinfo("Database status",f"Photo for user {srn_no} is updated.")
        else:
            return 0

    def delete_photo(self, srn_no):
        # conn = sqlite3.connect(resource_path("database/student_database.db"))
        cursor = conn.cursor(prepared=True)
        try:
            cursor.execute(
                "DELETE FROM photo WHERE id = ?",
                (srn_no,),
            )
            conn.commit()
            return 1
        
        except Exception as e:
            messagebox.showerror(f"Database Error", f"SQLite error: {e}\n")
            return 0



            
    def show_images_from_db(self):
        # conn = sqlite3.connect(resource_path("database/student_database.db"))
        cursor = conn.cursor(prepared=True)

        cursor.execute("SELECT image FROM photo")
        rows = cursor.fetchall()

        if rows:
            window = ctk.CTkToplevel(self.root)
            window.title("Images from Database")

            for row in rows:
                img_bytes = row[0]
                img = Image.frombytes("RGB", (300, 380), img_bytes)

                img_resized = img.resize((250, 330), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img_resized)

                label = ctk.CTkLabel(window, image=img_tk, text="")
                label.image = img_tk
                label.pack(padx=5, pady=5)



if __name__ == "__main__":
    root = ctk.CTk()
    app = ProfilePicEditor(root)
    root.mainloop()
