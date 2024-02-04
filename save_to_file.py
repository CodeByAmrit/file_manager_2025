import customtkinter as tk
from File_Manager import resource_path

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extract values of Input 1 and Input 2 from the file
        input1_value = lines[0].split(':')[-1].strip()
        input2_value = lines[1].split(':')[-1].strip()

        return input1_value, input2_value

    except FileNotFoundError:
        print("File not found.")
        return None, None


class SaveToFileApp:
    def __init__(self, master):
        self.master = master
        master.title("Login ")
        self.file_path = resource_path("output.txt")

        self.entry1_label = tk.CTkLabel(master, text="Login Details")
        self.entry1_label.grid(row=0, column=0, columnspan = 2, padx=10, pady=10)

        # Create entry widgets
        self.entry1_label = tk.CTkLabel(master, text="Host :", width=100)
        self.entry1_label.grid(row=1, column=0)
        self.entry1 = tk.CTkEntry(master)
        self.entry1.grid(row=1, column=1)

        self.entry2_label = tk.CTkLabel(master, text="Port :", width=100)
        self.entry2_label.grid(row=2, column=0)
        self.entry2 = tk.CTkEntry(master)
        self.entry2.grid(row=2, column=1)

        # Create a "Save" button
        self.save_button = tk.CTkButton(master, text="Save", command=self.save_to_file)
        self.save_button.grid(row=3, column=0, columnspan = 2, padx=10, pady=10)

        # Create a label to display status
        self.status_label = tk.CTkLabel(master, text="")
        self.status_label.grid(row=4, column=0)

    def save_to_file(self):
        input1_text = self.entry1.get()
        input2_text = self.entry2.get()
        with open("_internal/output.txt", 'w') as file:
            file.write(f"Input 1: {input1_text}\n")
            file.write(f"Input 2: {input2_text}\n")
        self.status_label.configure(text=f"File saved to: {self.file_path}")
        self.master.quit()

def take_inputs():
    root = tk.CTk()
    root.geometry("250x250")
    root.iconbitmap(default=resource_path("icons/schoolLogo.ico"))
    app = SaveToFileApp(root)
    host, port = read_from_file(app.file_path)
    app.entry1.insert(0, host)
    root.mainloop()
    
if __name__ == "__main__":
    root = tk.CTk()
    app = SaveToFileApp(root)
   
    root.mainloop()
