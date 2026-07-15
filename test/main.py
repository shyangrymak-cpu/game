from src.gamepkg.egobird import EgoBirdGame as rungame
import tkinter as tk

def main():
    print("Hi")
    
    # ส่วนนี้สั่งรันเกม EgoBird
    root = tk.Tk()
    app = rungame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    print(__name__)
