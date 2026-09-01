import tkinter as tk
from tkinter import messagebox, ttk

# --- ข้อมูลเนื้อหาและคำถาม ---
LESSONS = {
    "String": [
        "1. การเข้าถึงตัวอักษร (Indexing):\n   ข้อความ index เริ่มจาก 0 เช่น 'Python'[0] ได้ 'P'",
        "2. การสไลซ์ (Slicing):\n   การตัดข้อความบางส่วน เช่น 'Python'[0:3] ได้ 'Pyt'",
        "3. ความยาวของ String (len):\n   ฟังก์ชัน len() ใช้หาจำนวนตัวอักษร เช่น len('Hello') ได้ 5",
        "4. เมธอดเปลี่ยนตัวพิมพ์ (upper/lower):\n   'py'.upper() ได้ 'PY' และ 'PY'.lower() ได้ 'py'",
        "5. การค้นหาคำ (in / find):\n   ใช้ 'in' เช็คว่ามีคำนั้นไหม เช่น 'a' in 'cat' ได้ True"
    ],
    "List": [
        "1. การสร้างและเข้าถึงสมาชิก:\n   List เก็บหลายข้อมูลได้ เช่น fruits = ['apple', 'banana'] โดย fruits[0] คือ 'apple'",
        "2. การเพิ่มสมาชิก (append):\n   ใช้ .append() เพื่อเพิ่มข้อมูลต่อท้าย เช่น fruits.append('orange')",
        "3. การลบสมาชิก (remove / pop):\n   ใช้ .remove('apple') หรือ .pop(0) เพื่อลบข้อมูลออกจาก List",
        "4. การนับสมาชิกและเรียงลำดับ (len / sort):\n   len(list) ใช้หาจำนวนสมาชิก และ .sort() ใช้เรียงลำดับข้อมูล",
        "5. การเข้าถึงสมาชิกตัวสุดท้าย (Negative Indexing):\n   list[-1] จะดึงข้อมูลตัวสุดท้ายของ List เสมอ"
    ]
}

QUIZ = [
    # --- String Quiz (5 ข้อ) ---
    {
        "category": "String",
        "question": "1. ผลลัพธ์ของ 'Python'[1] คืออะไร?",
        "options": ["P", "y", "t", "h"],
        "answer": "y"
    },
    {
        "category": "String",
        "question": "2. คำสั่ง len('Hello World') คืนค่าเท่าใด?",
        "options": ["10", "11", "12", "5"],
        "answer": "11"
    },
    {
        "category": "String",
        "question": "3. เมธอดใดใช้แปลงข้อความให้เป็นตัวพิมพ์ใหญ่ทั้งหมด?",
        "options": [".capitalize()", ".upper()", ".lower()", ".title()"],
        "answer": ".upper()"
    },
    {
        "category": "String",
        "question": "4. ผลลัพธ์ของ 'Hello'[1:4] คืออะไร?",
        "options": ["Hel", "ell", "ello", "ello "],
        "answer": "ell"
    },
    {
        "category": "String",
        "question": "5. ข้อความ 'cat' in 'caterpillar' ให้ผลลัพธ์เป็นอะไร?",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    # --- List Quiz (5 ข้อ) ---
    {
        "category": "List",
        "question": "6. กำหนด x = [10, 20, 30] ค่าของ x[0] คืออะไร?",
        "options": ["10", "20", "30", "Error"],
        "answer": "10"
    },
    {
        "category": "List",
        "question": "7. หากต้องการเพิ่มข้อมูลต่อท้าย List ต้องใช้เมธอดใด?",
        "options": [".add()", ".insert()", ".append()", ".push()"],
        "answer": ".append()"
    },
    {
        "category": "List",
        "question": "8. คำสั่งใดใช้ดึงสมาชิก 'ตัวสุดท้าย' ของ List ออกมา?",
        "options": ["list[0]", "list[-1]", "list[last]", "list.end()"],
        "answer": "list[-1]"
    },
    {
        "category": "List",
        "question": "9. กำหนด nums = [3, 1, 2] หลังเรียก nums.sort() ค่าของ nums คืออะไร?",
        "options": ["[3, 1, 2]", "[2, 1, 3]", "[1, 2, 3]", "[3, 2, 1]"],
        "answer": "[1, 2, 3]"
    },
    {
        "category": "List",
        "question": "10. หากเรียก len([1, [2, 3], 4]) จะได้ผลลัพธ์เท่าใด?",
        "options": ["3", "4", "2", "Error"],
        "answer": "3"
    }
]

# --- Class สถาปัตยกรรม GUI ---
class EducationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("โปรแกรมเรียนรู้และทดสอบ List & String")
        self.root.geometry("650x550")
        self.root.configure(bg="#f4f6f9")

        self.current_quiz_index = 0
        self.score = 0
        self.user_answers = {}

        # สร้าง Tab Control
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # หน้าต่างเรียนรู้
        self.learn_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.learn_frame, text="📖 เนื้อหาบทเรียน")
        self.setup_learn_tab()

        # หน้าต่างแบบทดสอบ
        self.quiz_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.quiz_frame, text="✏️ แบบทดสอบ")
        self.setup_quiz_tab()

    # --- ส่วนที่ 1: หน้าเรียนรู้ ---
    def setup_learn_tab(self):
        canvas = tk.Canvas(self.learn_frame, bg="#ffffff")
        scrollbar = ttk.Scrollbar(self.learn_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # หัวข้อ String
        tk.Label(scrollable_frame, text="🔤 ความรู้เกี่ยวกับ String (ข้อความ)", font=("Helvetica", 14, "bold"), fg="#1e3d59", bg="#ffffff").pack(anchor="w", padx=15, pady=(15, 5))
        for item in LESSONS["String"]:
            lbl = tk.Label(scrollable_frame, text=item, font=("Helvetica", 10), justify="left", bg="#e8eef5", anchor="w", padx=10, pady=8, wraplength=550)
            lbl.pack(fill="x", padx=15, pady=4)

        # หัวข้อ List
        tk.Label(scrollable_frame, text="📋 ความรู้เกี่ยวกับ List (รายการ)", font=("Helvetica", 14, "bold"), fg="#1e3d59", bg="#ffffff").pack(anchor="w", padx=15, pady=(20, 5))
        for item in LESSONS["List"]:
            lbl = tk.Label(scrollable_frame, text=item, font=("Helvetica", 10), justify="left", bg="#e8eef5", anchor="w", padx=10, pady=8, wraplength=550)
            lbl.pack(fill="x", padx=15, pady=4)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # --- ส่วนที่ 2: หน้าแบบทดสอบ ---
    def setup_quiz_tab(self):
        self.category_label = tk.Label(self.quiz_frame, text="", font=("Helvetica", 10, "bold"), fg="#17b978")
        self.category_label.pack(anchor="w", padx=20, pady=(15, 0))

        self.q_label = tk.Label(self.quiz_frame, text="", font=("Helvetica", 12, "bold"), wraplength=550, justify="left")
        self.q_label.pack(anchor="w", padx=20, pady=10)

        self.selected_option = tk.StringVar()
        self.radio_buttons = []

        for i in range(4):
            rb = tk.Radiobutton(
                self.quiz_frame, text="", variable=self.selected_option, value="",
                font=("Helvetica", 11), anchor="w", justify="left"
            )
            rb.pack(fill="x", padx=40, pady=5)
            self.radio_buttons.append(rb)

        # ปุ่มควบคุม
        btn_frame = ttk.Frame(self.quiz_frame)
        btn_frame.pack(fill="x", padx=20, pady=20)

        self.prev_btn = ttk.Button(btn_frame, text="◄ ข้อก่อนหน้า", command=self.prev_question)
        self.prev_btn.pack(side="left")

        self.next_btn = ttk.Button(btn_frame, text="ข้อถัดไป ►", command=self.next_question)
        self.next_btn.pack(side="right")

        self.submit_btn = ttk.Button(btn_frame, text="ส่งคำตอบ 🏆", command=self.submit_quiz)

        self.load_question()

    def load_question(self):
        q_data = QUIZ[self.current_quiz_index]
        self.category_label.config(text=f"หมวดหมู่: {q_data['category']} ({self.current_quiz_index + 1}/{len(QUIZ)})")
        self.q_label.config(text=q_data["question"])

        # คืนค่าคำตอบเดิมถ้าเคยตอบไปแล้ว
        saved_ans = self.user_answers.get(self.current_quiz_index, "")
        self.selected_option.set(saved_ans)

        for i, option in enumerate(q_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        # แสดง/ซ่อน ปุ่มกด
        self.prev_btn.config(state="normal" if self.current_quiz_index > 0 else "disabled")
        
        if self.current_quiz_index == len(QUIZ) - 1:
            self.next_btn.pack_forget()
            self.submit_btn.pack(side="right")
        else:
            self.submit_btn.pack_forget()
            self.next_btn.pack(side="right")

    def save_current_answer(self):
        if self.selected_option.get():
            self.user_answers[self.current_quiz_index] = self.selected_option.get()

    def next_question(self):
        self.save_current_answer()
        if self.current_quiz_index < len(QUIZ) - 1:
            self.current_quiz_index += 1
            self.load_question()

    def prev_question(self):
        self.save_current_answer()
        if self.current_quiz_index > 0:
            self.current_quiz_index -= 1
            self.load_question()

    def submit_quiz(self):
        self.save_current_answer()
        
        if len(self.user_answers) < len(QUIZ):
            if not messagebox.askyesno("คำเตือน", "คุณยังตอบคำถามไม่ครบทุกข้อ ต้องการส่งคำตอบเลยหรือไม่?"):
                return

        score = 0
        for idx, q_data in enumerate(QUIZ):
            if self.user_answers.get(idx) == q_data["answer"]:
                score += 1

        percent = (score / len(QUIZ)) * 100
        msg = f"คุณได้คะแนน: {score} / {len(QUIZ)} คะแนน ({percent:.0f}%)\n\n"
        
        if percent >= 80:
            msg += "🌟 ยอดเยี่ยมมาก! คุณมีความเข้าใจ List และ String เป็นอย่างดี"
        elif percent >= 50:
            msg += "อ ทำได้ดี! สามารถกลับไปทบทวนเนื้อหาเพื่อเพิ่มความแม่นยำได้"
        else:
            msg += "📘 ลองกลับไปอ่านบทเรียนทบทวนอีกครั้งนะ!"

        messagebox.showinfo("ผลการทดสอบ", msg)

# --- เรียกใช้งานโปรแกรม ---
if __name__ == "__main__":
    root = tk.Tk()
    app = EducationalApp(root)
    root.mainloop()