import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

lost_items = []
found_items = []
user_info = {"name": "", "college": ""}
image_path = None


class LostFoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AK's Lost & Found App")
        self.root.geometry("600x500")

        self.colleges = [
            "HITAM", "MLRIT", "MREC", "NRCM", "CMR",
            "GRRR", "CBIT", "MGIT", "VJIT", "SRCM", "St. Peters"
        ]

        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Your Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Select Your College:").pack(pady=5)
        self.selected_college = tk.StringVar(value=self.colleges[0]) 
        tk.OptionMenu(self.root, self.selected_college, *self.colleges).pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        name = self.name_entry.get().strip()
        college = self.selected_college.get().strip()

        if name and college:
            user_info["name"] = name
            user_info["college"] = college
            self.main_screen()
        else:
            messagebox.showerror("Error", "Please enter both name and college.")

    def main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome {user_info['name']} from {user_info['college']}", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.root, text="Report Lost Item", command=lambda: self.report_item(lost_items)).pack(pady=10)
        tk.Button(self.root, text="Report Found Item", command=lambda: self.report_item(found_items)).pack(pady=10)

    def report_item(self, item_list):
        self.clear_screen()

        tk.Label(self.root, text="Item Name:").pack(pady=5)
        self.item_name_entry = tk.Entry(self.root)
        self.item_name_entry.pack(pady=5)

        tk.Label(self.root, text="Location:").pack(pady=5)
        self.location_entry = tk.Entry(self.root)
        self.location_entry.pack(pady=5)

        tk.Label(self.root, text="Contact Info:").pack(pady=5)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.pack(pady=5)

        tk.Button(self.root, text="Attach Image", command=self.attach_image).pack(pady=10)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Submit", command=lambda: self.submit_item(item_list)).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Back", command=self.main_screen).grid(row=0, column=1, padx=10)

    def submit_item(self, item_list):
        global image_path
        item_name = self.item_name_entry.get().strip()
        location = self.location_entry.get().strip()
        contact = self.contact_entry.get().strip()

        if item_name and location and contact:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item_list.append((user_info["name"], user_info["college"], item_name, location, contact, timestamp, image_path))
            messagebox.showinfo("Success", "Item reported successfully!")
            self.main_screen()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def attach_image(self):
        global image_path
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if path:
            image_path = path
            messagebox.showinfo("Image Selected", f"Image path: {image_path}")
if __name__ == "__main__":
    root = tk.Tk()
    app = LostFoundApp(root)
    root.mainloop()
