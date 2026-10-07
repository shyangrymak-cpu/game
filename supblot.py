import matplotlib.pyplot as plt
import numpy as np

# 1. สร้าง Figure และ Subplots ขนาด 3x3
fig, axs = plt.subplots(3, 3, figsize=(18, 14))

# ปรับขนาดฟอนต์ลงเหลือ 18 และขยับตำแหน่งแนวตั้งขึ้นไปที่ y=0.98
fig.suptitle("My First Class", fontsize=18, fontweight='bold', color='navy', y=0.98)

# ข้อมูลตัวอย่าง
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 8, 1, 10, 5])
y2 = np.array([6, 2, 7, 11, 2])

# -------------------------------------------------------------
# 1. Matplotlib Markers
# -------------------------------------------------------------
axs[0, 0].plot(x, y, marker='o', ms=8, mec='red', mfc='yellow', label='Marker Points')
axs[0, 0].set_title("1. Matplotlib Markers", fontsize=11, fontweight='bold', pad=8)
axs[0, 0].set_xlabel("X Axis (Index)", fontsize=9)
axs[0, 0].set_ylabel("Y Axis (Values)", fontsize=9)
axs[0, 0].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# 2. Matplotlib Line
# -------------------------------------------------------------
axs[0, 1].plot(x, y, color='r', linestyle='-', linewidth=2, label='Solid Line')
axs[0, 1].plot(x, y2, color='g', linestyle=':', linewidth=2, label='Dotted Line')
axs[0, 1].set_title("2. Matplotlib Line", fontsize=11, fontweight='bold', pad=8)
axs[0, 1].set_xlabel("X Axis (Time)", fontsize=9)
axs[0, 1].set_ylabel("Y Axis (Score)", fontsize=9)
axs[0, 1].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# 3. Matplotlib Labels
# -------------------------------------------------------------
font_title = {'family': 'sans-serif', 'color': 'blue', 'size': 11, 'weight': 'bold'}
font_axis = {'family': 'sans-serif', 'color': 'darkred', 'size': 9}
axs[0, 2].plot(x, y, 'b-o', label='Sample Series')
axs[0, 2].set_title("3. Matplotlib Labels", fontdict=font_title, pad=8)
axs[0, 2].set_xlabel("X Axis (Categories)", fontdict=font_axis)
axs[0, 2].set_ylabel("Y Axis (Measurements)", fontdict=font_axis)
axs[0, 2].legend(fontsize=8, loc='upper right')

# -------------------------------------------------------------
# 4. Matplotlib Grid
# -------------------------------------------------------------
axs[1, 0].plot(x, y, color='orange', marker='s', label='Grid Data')
axs[1, 0].set_title("4. Matplotlib Grid", fontsize=11, fontweight='bold', pad=8)
axs[1, 0].set_xlabel("X Axis", fontsize=9)
axs[1, 0].set_ylabel("Y Axis", fontsize=9)
axs[1, 0].grid(color='gray', linestyle='--', linewidth=0.7)
axs[1, 0].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# 5. Matplotlib Subplot
# -------------------------------------------------------------
axs[1, 1].plot(x, y, 'g-^', label='Group A')
axs[1, 1].plot(x, y2, 'b-s', label='Group B')
axs[1, 1].set_title("5. Matplotlib Subplot", fontsize=11, fontweight='bold', pad=8)
axs[1, 1].set_xlabel("X Axis (Group Index)", fontsize=9)
axs[1, 1].set_ylabel("Y Axis (Performance)", fontsize=9)
axs[1, 1].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# 6. Matplotlib Scatter
# -------------------------------------------------------------
x_sc = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y_sc = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
axs[1, 2].scatter(x_sc, y_sc, color='hotpink', label='Car Speed')
axs[1, 2].set_title("6. Matplotlib Scatter", fontsize=11, fontweight='bold', pad=8)
axs[1, 2].set_xlabel("X Axis (Age of Car)", fontsize=9)
axs[1, 2].set_ylabel("Y Axis (Speed)", fontsize=9)
axs[1, 2].legend(fontsize=8, loc='upper right')

# -------------------------------------------------------------
# 7. Matplotlib Bars
# -------------------------------------------------------------
categories = np.array(["A", "B", "C", "D"])
values = np.array([3, 8, 1, 10])
axs[2, 0].bar(categories, values, color="#4CAF50", label='Sales Vol')
axs[2, 0].set_title("7. Matplotlib Bars", fontsize=11, fontweight='bold', pad=8)
axs[2, 0].set_xlabel("X Axis (Categories)", fontsize=9)
axs[2, 0].set_ylabel("Y Axis (Sales)", fontsize=9)
axs[2, 0].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# 8. Matplotlib Histograms
# -------------------------------------------------------------
np.random.seed(42)
x_hist = np.random.normal(170, 10, 250)
axs[2, 1].hist(x_hist, bins=15, color='teal', edgecolor='black', label='Height Dist')
axs[2, 1].set_title("8. Matplotlib Histograms", fontsize=11, fontweight='bold', pad=8)
axs[2, 1].set_xlabel("X Axis (Height Range cm)", fontsize=9)
axs[2, 1].set_ylabel("Y Axis (Frequency)", fontsize=9)
axs[2, 1].legend(fontsize=8, loc='upper right')

# -------------------------------------------------------------
# 9. Matplotlib Pie Charts
# -------------------------------------------------------------
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
y_pie = np.array([35, 25, 25, 15])
myexplode = [0.08, 0, 0, 0]
wedges, texts, autotexts = axs[2, 2].pie(
    y_pie, 
    explode=myexplode, 
    autopct='%1.1f%%', 
    shadow=True, 
    startangle=90,
    textprops=dict(fontsize=8)
)
axs[2, 2].set_title("9. Matplotlib Pie Charts", fontsize=11, fontweight='bold', pad=8)
axs[2, 2].set_xlabel("X Axis (Category Share)", fontsize=9)
axs[2, 2].set_ylabel("Y Axis (Percentage)", fontsize=9)
axs[2, 2].legend(wedges, mylabels, title="Fruits", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=8)

# -------------------------------------------------------------
# 2. ปรับแต่งเว้นระยะขอบบนลงมา (top=0.88) ไม่ให้ชน Title หลัก
# -------------------------------------------------------------
plt.subplots_adjust(
    left=0.06,
    right=0.92,
    top=0.88,      # ดึงขอบบนลงมาจากเดิม เพื่อเว้นที่ให้ "My First Class"
    bottom=0.06,
    wspace=0.35,
    hspace=0.50
)

# แสดงผล GUI
plt.show()