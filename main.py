import os
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("deadDirTracker")
root.geometry("400x50")

class deadDirScanCls():
    def scan(root):
        data = []
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:
                path = os.path.join(dirpath, name)
                try:
                    mtime = os.path.getmtime(path)
                    human_time = datetime.fromtimestamp(mtime).astimezone()
                    human_time = human_time.replace(microsecond=0)
                    formatted_human_time = human_time.strftime("%Y-%m-%d %H:%M:%S %z")
                    data.append((path, mtime, human_time.isoformat()))
                    # print(data)
                except (PermissionError, FileNotFoundError, OSError) as e:
                    print(f"Error: {e}")
                    continue
        data.sort(key=lambda item: item[1])
        print(data)
        fileToWrite = "deadDir.txt"
        with open(f"{fileToWrite}", "w", encoding="utf-8") as f:
            for path, mtime, human_time_iso in data:
                f.write(f"{path} {mtime} {human_time_iso}\n")
        print(f"Saved to file {fileToWrite}")
        messagebox.showinfo("Success", f"Saved to file {fileToWrite}")

    def askAndScan():
        root = simpledialog.askstring("Directory to scan?", "Directory to scan?")
        deadDirScanCls.scan(root)

askAndScanBtn = tk.Button(
                root, text="Scan directories",
                command=deadDirScanCls.askAndScan)
askAndScanBtn.pack()

# root = r"C:\\Users\\Rohan\\Documents\\python"
# root = input("Directory to scan? ")

root.mainloop()