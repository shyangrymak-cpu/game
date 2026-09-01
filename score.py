import random
import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, ROUND_HALF_UP
import customtkinter as ctk
import pandas as pd

# ตั้งค่า Theme ของ GUI
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class GradeCalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Basic Computer Programming - Grade Assessment System")
        self.geometry("950x700")
        self.resizable(False, False)

        # Header Title
        self.title_label = ctk.CTkLabel(
            self,
            text="ระบบรวมคะแนนและตัดเกรดนักศึกษา (20 คน)",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.title_label.pack(pady=(15, 10))

        # Control Frame (Buttons)
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(fill="x", padx=20, pady=5)

        self.btn_random = ctk.CTkButton(
            self.control_frame,
            text="🎲 สุ่มคะแนนตัวอย่าง",
            command=self.generate_random_scores,
            fg_color="#2b5c8f",
        )
        self.btn_random.pack(side="left", padx=10, pady=10)

        self.btn_calculate = ctk.CTkButton(
            self.control_frame,
            text="⚡ คำนวณและตัดเกรด",
            command=self.calculate_grades,
            fg_color="#27ae60",
            hover_color="#219150",
        )
        self.btn_calculate.pack(side="left", padx=10, pady=10)

        self.btn_export = ctk.CTkButton(
            self.control_frame,
            text="💾 ส่งออกไฟล์ Excel",
            command=self.export_to_excel,
            fg_color="#8e44ad",
        )
        self.btn_export.pack(side="right", padx=10, pady=10)

        # Scrollable Frame for Student Inputs
        self.scroll_frame = ctk.CTkScrollableFrame(
            self, width=900, height=520
        )
        self.scroll_frame.pack(pady=10, padx=20)

        # Table Header
        headers = [
            "ลำดับ",
            "รหัสนักศึกษา",
            "Midterm (50)",
            "Final (50)",
            "รวม (100)",
            "เกรด",
        ]
        for col_idx, header in enumerate(headers):
            lbl = ctk.CTkLabel(
                self.scroll_frame,
                text=header,
                font=ctk.CTkFont(size=14, weight="bold"),
            )
            lbl.grid(row=0, column=col_idx, padx=15, pady=10, sticky="ew")

        # Input Row Storage
        self.rows_data = []
        self.create_student_rows()

    def create_student_rows(self):
        for i in range(20):
            row_num = i + 1
            std_id = f"STD660{row_num:02d}"

            # Labels & Entries
            lbl_num = ctk.CTkLabel(
                self.scroll_frame, text=str(row_num), width=40
            )
            lbl_num.grid(row=row_num, column=0, padx=5, pady=5)

            lbl_id = ctk.CTkLabel(self.scroll_frame, text=std_id, width=100)
            lbl_id.grid(row=row_num, column=1, padx=5, pady=5)

            entry_mid = ctk.CTkEntry(
                self.scroll_frame, width=100, placeholder_text="0-50"
            )
            entry_mid.grid(row=row_num, column=2, padx=10, pady=5)

            entry_final = ctk.CTkEntry(
                self.scroll_frame, width=100, placeholder_text="0-50"
            )
            entry_final.grid(row=row_num, column=3, padx=10, pady=5)

            lbl_total = ctk.CTkLabel(
                self.scroll_frame,
                text="-",
                width=100,
                font=ctk.CTkFont(size=14, weight="bold"),
            )
            lbl_total.grid(row=row_num, column=4, padx=10, pady=5)

            lbl_grade = ctk.CTkLabel(
                self.scroll_frame,
                text="-",
                width=80,
                font=ctk.CTkFont(size=14, weight="bold"),
            )
            lbl_grade.grid(row=row_num, column=5, padx=10, pady=5)

            self.rows_data.append({
                "id": std_id,
                "mid": entry_mid,
                "final": entry_final,
                "total_lbl": lbl_total,
                "grade_lbl": lbl_grade,
            })

    def assign_grade(self, score):
        # เกณฑ์การตัดเกรดตามเงื่อนไข
        if score < 40:
            return "F", "#FF4D4D"  # ตัวอักษรสีแดงสด
        elif 40 <= score < 45:
            return "D", "#FFFFFF"
        elif 45 <= score < 50:
            return "D+", "#FFFFFF"
        elif 50 <= score < 55:
            return "C", "#FFFFFF"
        elif 55 <= score < 60:
            return "C+", "#FFFFFF"
        elif 60 <= score < 65:
            return "B", "#FFFFFF"
        elif 65 <= score < 70:
            return "B+", "#FFFFFF"
        elif 70 <= score < 80:
            return "A-", "#FFFFFF"
        else:
            return "A", "#2ECC71"  # เกรด A สีเขียว

    def calculate_grades(self):
        for row in self.rows_data:
            try:
                mid_str = row["mid"].get().strip()
                final_str = row["final"].get().strip()

                mid_val = Decimal(mid_str) if mid_str else Decimal("0")
                final_val = Decimal(final_str) if final_str else Decimal("0")

                # Validate max scores
                mid_val = min(max(Decimal("0"), mid_val), Decimal("50"))
                final_val = min(max(Decimal("0"), final_val), Decimal("50"))

                total = (mid_val + final_val).quantize(
                    Decimal("0.01"), rounding=ROUND_HALF_UP
                )
                grade, color = self.assign_grade(total)

                row["total_lbl"].configure(text=f"{total:.2f}")
                row["grade_lbl"].configure(text=grade, text_color=color)

            except Exception:
                row["total_lbl"].configure(text="Error")
                row["grade_lbl"].configure(text="N/A", text_color="#FF0000")

    def generate_random_scores(self):
        for row in self.rows_data:
            row["mid"].delete(0, tk.END)
            row["final"].delete(0, tk.END)
            row["mid"].insert(0, str(round(random.uniform(15, 50), 1)))
            row["final"].insert(0, str(round(random.uniform(15, 50), 1)))
        self.calculate_grades()

    def export_to_excel(self):
        data = []
        for row in self.rows_data:
            data.append({
                "Student ID": row["id"],
                "Midterm": row["mid"].get(),
                "Final": row["final"].get(),
                "Total": row["total_lbl"].cget("text"),
                "Grade": row["grade_lbl"].cget("text"),
            })
        df = pd.DataFrame(data)
        df.to_excel("grades_result.xlsx", index=False)
        messagebox.showinfo(
            "Success", "ส่งออกไฟล์ข้อมูลเรียบร้อย: grades_result.xlsx"
        )


if __name__ == "__main__":
    app = GradeCalculatorApp()
    app.mainloop()