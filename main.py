import tkinter as tk
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from src.gamepkg.egobird import EgoBirdGame as start_egobird
from src.gamepkg.snakegame import start_snake
from src.gamepkg.egobird import EgoBirdGame as start_egobird
from src.gamepkg.snakegame import start_snake

def open_game(game_type):
    # ซ่อนหน้าต่างเมนูชั่วคราว แล้วเปิดหน้าต่างเกมใหม่
    launcher.withdraw()
    game_window = tk.Toplevel()
    
    # เมื่อปิดหน้าต่างเกม ให้เปิดหน้าเมนูกลับขึ้นมา
    def on_close():
        game_window.destroy()
        launcher.deiconify()
        
    game_window.protocol("WM_DELETE_WINDOW", on_close)

    if game_type == "egobird":
        start_egobird(game_window)
    elif game_type == "snake":
        start_snake(game_window)

# สร้างหน้าต่างเลือกเกม (Launcher)
launcher = tk.Tk()
launcher.title("Game Launcher")
launcher.geometry("320x260")

label = tk.Label(launcher, text="กรุณาเลือกเกมที่ต้องการเล่น", font=("Arial", 14, "bold"))
label.pack(pady=20)

btn_egobird = tk.Button(
    launcher, text="1. Play EgoBird Game", font=("Arial", 12), width=22, bg="#4CAF50", fg="white",
    command=lambda: open_game("egobird")
)
btn_egobird.pack(pady=10)

btn_snake = tk.Button(
    launcher, text="2. Play Snake Game", font=("Arial", 12), width=22, bg="#2196F3", fg="white",
    command=lambda: open_game("snake")
)
btn_snake.pack(pady=10)

launcher.mainloop()