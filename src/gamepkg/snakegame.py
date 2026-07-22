import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        
        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.direction = "Right"
        self.food = self.spawn_food()
        self.score = 0
        
        self.root.bind("<Key>", self.change_direction)
        self.update_game()

    def spawn_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def change_direction(self, event):
        new_dir = event.keysym
        all_dirs = ["Up", "Down", "Left", "Right"]
        if new_dir in all_dirs:
            opposite = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
            if new_dir != opposite.get(self.direction):
                self.direction = new_dir

    def update_game(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up": head_y -= 20
        elif self.direction == "Down": head_y += 20
        elif self.direction == "Left": head_x -= 20
        elif self.direction == "Right": head_x += 20
        
        new_head = (head_x, head_y)

        if (head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or 
            new_head in self.snake):
            self.canvas.create_text(200, 200, text=f"Game Over!\nScore: {self.score}", fill="white", font=("Arial", 20))
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green")
        
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx+20, fy+20, fill="red")
        
        self.root.after(100, self.update_game)

def start_snake(root):
    return SnakeGame(root)

# สั่งรันเดี่ยวๆ ด้านล่างสุด (เฉพาะเวลาทดสอบรันไฟล์นี้ตรงๆ)
if __name__ == "__main__":
    root = tk.Tk()
    app = start_snake(root)
    root.mainloop()