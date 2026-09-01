import subprocess
import sys
import tkinter as tk
from tkinter import font


def run_python_file(filename, status_label):
    """ฟังก์ชันสำหรับสั่งรันไฟล์ Python"""
    status_label.config(text=f"Running: {filename}")
    try:
        # ใช้ sys.executable เพื่อรันไฟล์ใน Python Environment เดียวกัน
        subprocess.Popen([sys.executable, filename])
    except Exception as e:
        status_label.config(text=f"Error running {filename}: {e}")


def main():
    root = tk.Tk()
    root.title("Python Program Launcher")
    root.geometry("420x530")
    root.configure(bg="#EBF4F6")

    # Font Setup
    title_font = font.Font(family="Helvetica", size=18, weight="bold")
    sub_font = font.Font(family="Helvetica", size=10)
    btn_font = font.Font(family="Helvetica", size=11, weight="bold")

    # Header / Title
    title_label = tk.Label(
        root,
        text="Python Program Launcher",
        font=title_font,
        bg="#EBF4F6",
        fg="#333333",
    )
    title_label.pack(pady=(25, 5))

    subtitle_label = tk.Label(
        root,
        text="Select a Python program to run",
        font=sub_font,
        bg="#EBF4F6",
        fg="#555555",
    )
    subtitle_label.pack(pady=(0, 20))

    # รายการปุ่มกด พร้อมไฟล์ที่แมปไว้
    programs = [
        {
            "text": "1. Global & Local Vars",
            "filename": "prog1_global_local.py",
            "color": "#319DA0",
        },
        {
            "text": "2. Global Keyword",
            "filename": "prog2_global_keyword.py",
            "color": "#7FB77E",
        },
        {
            "text": "3. Multiple Values",
            "filename": "prog3_multiple_values.py",
            "color": "#C28C7E",
        },
        {
            "text": "4. One Value to Multi-Vars",
            "filename": "prog4_one_value_multiple_vars.py",
            "color": "#7868E6",
        },
        {
            "text": "5. Unpack Collection",
            "filename": "prog5_unpack_collection.py",
            "color": "#C85C5C",
        },
    ]

    status_label = tk.Label(
        root, text="", font=sub_font, bg="#EBF4F6", fg="#555555"
    )

    # สร้างปุ่มกด 5 ปุ่ม
    for prog in programs:
        btn = tk.Button(
            root,
            text=prog["text"],
            font=btn_font,
            bg=prog["color"],
            fg="white",
            activebackground=prog["color"],
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda f=prog["filename"]: run_python_file(
                f, status_label
            ),
        )
        btn.pack(fill="x", padx=40, pady=6, ipady=10)

    # Status Label แสดงชื่อไฟล์ที่กำลังรัน
    status_label.pack(side="top", pady=(15, 5))

    # ปุ่ม Exit
    exit_btn = tk.Button(
        root,
        text="Exit",
        font=sub_font,
        bg="#6C757D",
        fg="white",
        activebackground="#5A6268",
        activeforeground="white",
        bd=0,
        relief="flat",
        cursor="hand2",
        command=root.quit,
    )
    exit_btn.pack(side="bottom", pady=(0, 20), ipadx=30, ipady=3)

    root.mainloop()


if __name__ == "__main__":
    main()