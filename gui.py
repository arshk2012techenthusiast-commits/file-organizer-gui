import tkinter as tk
from tkinter import filedialog, messagebox
import os  # We use this to find the exact folder path

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("450x150")
        
        self.label = tk.Label(root, text="Select the folder to organize:", font=("Arial", 11))
        self.label.pack(pady=10)
        
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, fill="x")
        
        self.path_entry = tk.Entry(self.frame, font=("Arial", 10))
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.browse_btn = tk.Button(self.frame, text="Browse", command=self.browse)
        self.browse_btn.pack(side="right")
        
        self.go_btn = tk.Button(root, text="Organize!", font=("Arial", 10, "bold"), bg="green", fg="white", command=self.run_logic)
        self.go_btn.pack(pady=15)

    def browse(self):
        selected = filedialog.askdirectory()
        if selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, selected)

    def run_logic(self):
        chosen_path = self.path_entry.get().strip()
        if not chosen_path:
            messagebox.showwarning("Error", "Please choose a path first!")
            return
            
        try:
            # 1. Dynamically find the folder where gui.py is stored
            gui_dir = os.path.dirname(os.path.abspath(__file__))
            
            # 2. Combine that folder path with your logic file name
            logic_file_path = os.path.join(gui_dir, "file organizer.py")
            
            # 3. Inject the path into your code's environment
            context = {"path": chosen_path}
            
            # 4. Read and execute the file using its absolute path
            with open(logic_file_path, "r") as f:
                exec(f.read(), context, context)
                
            messagebox.showinfo("Success", "Done organizing!")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()