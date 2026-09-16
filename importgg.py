import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class TextProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("w10 Date-String Format Processor")
        self.root.geometry("850x650")
        
        # --- UI Layout ---
        # 1. โซนปุ่มเปิดไฟล์
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(btn_frame, text="📂 โหลดไฟล์ Text", command=self.load_file, bg="#4CAF50", fg="white").pack(side=tk.LEFT)
        
        # 2. โซนแสดงผลข้อความต้นฉบับ
        tk.Label(root, text="ข้อความต้นฉบับ (Original Text):", anchor="w").pack(fill=tk.X, padx=10)
        self.txt_input = tk.Text(root, height=8)
        self.txt_input.pack(fill=tk.BOTH, padx=10, pady=2, expand=True)
        
        # 3. โซนเลือกฟังก์ชัน และ ใส่ Parameter
        control_frame = tk.LabelFrame(root, text=" ตัวเลือกการประมวลผล Regex ")
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(control_frame, text="เลือกฟังก์ชัน:").grid(row=0, column=0, padx=5, pady=5)
        self.func_cb = ttk.Combobox(control_frame, width=45, state="readonly")
        self.func_cb['values'] = [
            "1. ค้นหาตาม Pattern (re.findall)",
            "2. ค้นหาตำแหน่งแรก (re.search)",
            "3. ค้นหาวันที่รูปแบบ YYYY-MM-DD",
            "4. ค้นหาสกุลเงิน (เช่น $100 หรือ 500บาท)",
            "5. ค้นหา อีเมล (Email)",
            "6. ค้นหา เบอร์โทรศัพท์",
            "7. แทนที่คำด้วยข้อความใหม่ (re.sub)",
            "8. แยกข้อความด้วย ตัวคั่น (re.split)",
            "9. กรองเฉพาะคำที่ยาวเกินกำหนด (re.finditer)",
            "10. ตรวจสอบว่าเริ่มต้นด้วยคำที่ระบุหรือไม่ (re.match)"
        ]
        self.func_cb.current(0)
        self.func_cb.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(control_frame, text="Param 1 (Pattern/Target):").grid(row=1, column=0, padx=5, pady=5)
        self.ent_param1 = tk.Entry(control_frame, width=30)
        self.ent_param1.insert(0, r"\d+")  # Default regex: หาตัวเลข
        self.ent_param1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        tk.Label(control_frame, text="Param 2 (Replace/Limit):").grid(row=2, column=0, padx=5, pady=5)
        self.ent_param2 = tk.Entry(control_frame, width=30)
        self.ent_param2.insert(0, "[REPLACED]")
        self.ent_param2.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        tk.Button(control_frame, text="⚡ ประมวลผล", command=self.process_text, bg="#2196F3", fg="white", width=15).grid(row=1, column=2, rowspan=2, padx=10)

        # 4. โซนแสดงผลลัพธ์
        tk.Label(root, text="ผลลัพธ์ (Output):", anchor="w").pack(fill=tk.X, padx=10)
        self.txt_output = tk.Text(root, height=8, bg="#f0f0f0")
        self.txt_output.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

    # --- ฟังก์ชันเปิดไฟล์ ---
    def load_file(self):
        try:
            filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if filepath:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.txt_input.delete("1.0", tk.END)
                    self.txt_input.insert(tk.END, content)
                messagebox.showinfo("สำเร็จ", "โหลดไฟล์เรียบร้อยแล้ว!")
        except Exception as e:
            messagebox.showerror("Error", f"ไม่สามารถอ่านไฟล์ได้: {str(e)}")

    # --- ฟังก์ชันประมวลผลหลัก (รวม 10 โมดูล Regex & try-except) ---
    def process_text(self):
        text = self.txt_input.get("1.0", tk.END).strip()
        p1 = self.ent_param1.get()
        p2 = self.ent_param2.get()
        selected = self.func_cb.current() + 1
        
        if not text:
            messagebox.showwarning("คำเตือน", "กรุณาใส่ข้อความหรือโหลดไฟล์ก่อน")
            return

        self.txt_output.delete("1.0", tk.END)

        # ใช้ try-except จัดการ Error การประมวลผล Regex
        try:
            result = ""
            
            # 1. re.findall
            if selected == 1:
                matches = re.findall(p1, text)
                result = f"[re.findall] เจอ {len(matches)} รายการ:\n" + str(matches)
                
            # 2. re.search
            elif selected == 2:
                match = re.search(p1, text)
                result = f"[re.search] เจอที่ตำแหน่ง: {match.span()} คำว่า: '{match.group()}'" if match else "ไม่พบข้อมูล"
                
            # 3. Find Dates (YYYY-MM-DD or DD/MM/YYYY)
            elif selected == 3:
                pattern = p1 if p1 != r"\d+" else r"\b\d{4}[-/]\d{2}[-/]\d{2}\b|\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"
                dates = re.findall(pattern, text)
                result = f"[Date Finder] เจอวันที่: {dates}"
                
            # 4. Find Currency
            elif selected == 4:
                pattern = r"(\$\d+(?:\.\d+)?|\d+\s?บาท)"
                currencies = re.findall(pattern, text)
                result = f"[Currency Finder] เจอยอดเงิน: {currencies}"
                
            # 5. Find Emails
            elif selected == 5:
                pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
                emails = re.findall(pattern, text)
                result = f"[Email Finder] เจออีเมล: {emails}"
                
            # 6. Find Phone Numbers
            elif selected == 6:
                pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
                phones = re.findall(pattern, text)
                result = f"[Phone Finder] เจอเบอร์โทร: {phones}"
                
            # 7. re.sub (Replace)
            elif selected == 7:
                new_text = re.sub(p1, p2, text)
                result = f"[re.sub] ข้อความหลังแทนที่:\n{new_text}"
                
            # 8. re.split
            elif selected == 8:
                parts = re.split(p1, text)
                result = f"[re.split] แยกข้อความได้ {len(parts)} ส่วน:\n" + str(parts)
                
            # 9. re.finditer (กรองคำยาวกว่า param2)
            elif selected == 9:
                min_len = int(p2) if p2.isdigit() else 5
                matches = [m.group() for m in re.finditer(r"\b\w+\b", text) if len(m.group()) >= min_len]
                result = f"[re.finditer] คำที่มีความยาว >= {min_len} ตัวอักษร:\n" + str(matches)
                
            # 10. re.match
            elif selected == 10:
                match = re.match(p1, text)
                result = f"[re.match] ข้อความเริ่มต้นตรงตาม Pattern: '{match.group()}'" if match else "[re.match] ข้อความไม่ได้เริ่มต้นด้วย Pattern นี้"

            self.txt_output.insert(tk.END, result)

        except re.error as reg_err:
            messagebox.showerror("Regex Error", f"รูปแบบ Pattern ไม่ถูกต้อง:\n{str(reg_err)}")
        except Exception as e:
            messagebox.showerror("Runtime Error", f"เกิดข้อผิดพลาด: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextProcessorApp(root)
    root.mainloop()