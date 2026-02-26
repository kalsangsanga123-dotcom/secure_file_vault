from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
# Import the functions we created in vault_logic
import vault_logic 

class SecureVault:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Secure Vault")
        self.root.geometry("450x400")
        self.password = None 
        
        self.status = Label(root, text="🔒 LOCKED", fg="red", font=("Arial", 12, "bold"))
        self.status.pack(pady=10)
        
        frame = Frame(root)
        frame.pack(pady=10)
        Button(frame, text="🔓 Unlock", command=self.unlock, width=12).grid(row=0, column=0, padx=5)
        Button(frame, text="🔒 Lock", command=self.lock, width=12).grid(row=0, column=1, padx=5)
        Button(frame, text="➕ Add File", command=self.add_file, width=12).grid(row=1, column=0, padx=5, pady=5)
        Button(frame, text="⬇️ Retrieve", command=self.retrieve, width=12).grid(row=1, column=1, padx=5, pady=5)
        
        Label(root, text="Stored Files:").pack()
        self.listbox = Listbox(root, width=50, height=12)
        self.listbox.pack(pady=10)
        self.update_status()

    def update_status(self):
        if self.password:
            self.status.config(text="🔓 UNLOCKED", fg="green")
            state = NORMAL
            unlock_state = DISABLED
        else:
            self.status.config(text="🔒 LOCKED", fg="red")
            self.listbox.delete(0, END)
            self.listbox.insert(END, "Unlock vault to view files")
            state = DISABLED
            unlock_state = NORMAL

        for btn_frame in self.root.winfo_children():
            if isinstance(btn_frame, Frame):
                for b in btn_frame.winfo_children():
                    if b.cget("text") == "🔓 Unlock":
                        b.config(state=unlock_state)
                    else:
                        b.config(state=state)

    def unlock(self):
        pwd = simpledialog.askstring("Unlock", "Enter password:", show="*")
        if pwd and vault_logic.verify_password(pwd):
            self.password = pwd
            self.update_status()
            self.refresh_list()
            messagebox.showinfo("Success", "Vault unlocked!")
        else:
            messagebox.showerror("Error", "Wrong password!")

    def lock(self):
        self.password = None
        self.update_status()
        messagebox.showinfo("Locked", "Password cleared from memory")

    def refresh_list(self):
        if not self.password: return
        self.listbox.delete(0, END)
        try:
            meta = vault_logic.load_metadata(self.password)
            if not meta:
                self.listbox.insert(END, "No files stored")
                return
            for name, info in meta.items():
                self.listbox.insert(END, f"{name} ({info['size']} bytes)")
        except Exception as e:
            self.listbox.insert(END, f"Error: {str(e)}")

    