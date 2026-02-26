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

    