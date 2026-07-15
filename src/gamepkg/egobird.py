import tkinter as tk
import random

WIDTH = 500
HEIGHT = 700
BIRD_SIZE = 30
PIPE_WIDTH = 70
PIPE_GAP = 180
GRAVITY = 2
JUMP_STRENGTH = -15
PIPE_SPEED = 6

class EgoBirdGame:
    def __init__(self, root):
        self.root = root
        self.root.title("EgoBird")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
        self.canvas.pack()

        self.score = 0
        self.game_over = False

        self.bird_x = 100
        self.bird_y = HEIGHT // 2
        self.velocity = 0

        self.bird = self.canvas.create_oval(
            self.bird_x,
            self.bird_y,
            self.bird_x + BIRD_SIZE,
            self.bird_y + BIRD_SIZE,
            fill="yellow",
            outline="orange",
            width=3
        )

        self.pipes = []
        self.score_text = self.canvas.create_text(
            60, 40,
            text="Score: 0",
            font=("Arial", 20, "bold"),
            fill="white"
        )

        self.canvas.create_text(
            WIDTH//2, 60,
            text="Press SPACE to Fly",
            font=("Arial", 18, "bold"),
            fill="navy"
        )

        self.root.bind("<space>", self.jump)

        self.create_pipe()
        self.update_game()

    def jump(self, event=None):
        if not self.game_over:
            self.velocity = JUMP_STRENGTH
        else:
            self.restart()

    def create_pipe(self):
        gap_y = random.randint(150, HEIGHT - 150)

        top_pipe = self.canvas.create_rectangle(
            WIDTH, 0,
            WIDTH + PIPE_WIDTH, gap_y - PIPE_GAP//2,
            fill="green"
        )

        bottom_pipe = self.canvas.create_rectangle(
            WIDTH, gap_y + PIPE_GAP//2,
            WIDTH + PIPE_WIDTH, HEIGHT,
            fill="green"
        )

        self.pipes.append((top_pipe, bottom_pipe, False))

    def move_pipes(self):
        new_pipes = []

        for top, bottom, scored in self.pipes:
            self.canvas.move(top, -PIPE_SPEED, 0)
            self.canvas.move(bottom, -PIPE_SPEED, 0)

            top_coords = self.canvas.coords(top)

            if top_coords[2] < 0:
                self.canvas.delete(top)
                self.canvas.delete(bottom)
                continue

            if not scored and top_coords[2] < self.bird_x:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                scored = True

            new_pipes.append((top, bottom, scored))

        self.pipes = new_pipes

        if len(self.pipes) == 0 or self.canvas.coords(self.pipes[-1][0])[0] < WIDTH - 250:
            self.create_pipe()

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)

        if bird_coords[1] <= 0 or bird_coords[3] >= HEIGHT:
            return True

        for top, bottom, _ in self.pipes:
            if self.overlap(bird_coords, self.canvas.coords(top)):
                return True
            if self.overlap(bird_coords, self.canvas.coords(bottom)):
                return True

        return False

    def overlap(self, a, b):
        return not (
            a[2] < b[0] or
            a[0] > b[2] or
            a[3] < b[1] or
            a[1] > b[3]
        )

    def update_game(self):
        if self.game_over:
            return

        self.velocity += GRAVITY
        self.bird_y += self.velocity

        self.canvas.coords(
            self.bird,
            self.bird_x,
            self.bird_y,
            self.bird_x + BIRD_SIZE,
            self.bird_y + BIRD_SIZE
        )

        self.move_pipes()

        if self.check_collision():
            self.end_game()
            return

        self.root.after(30, self.update_game)

    def end_game(self):
        self.game_over = True

        self.canvas.create_text(
            WIDTH//2,
            HEIGHT//2 - 40,
            text="GAME OVER",
            font=("Arial", 32, "bold"),
            fill="red"
        )

        self.canvas.create_text(
            WIDTH//2,
            HEIGHT//2 + 10,
            text=f"Final Score: {self.score}",
            font=("Arial", 22, "bold"),
            fill="white"
        )

        self.canvas.create_text(
            WIDTH//2,
            HEIGHT//2 + 50,
            text="Press SPACE to Restart",
            font=("Arial", 18),
            fill="yellow"
        )

    def restart(self):
        self.canvas.delete("all")
        self.score = 0
        self.game_over = False

        self.bird_y = HEIGHT // 2
        self.velocity = 0

        self.bird = self.canvas.create_oval(
            self.bird_x,
            self.bird_y,
            self.bird_x + BIRD_SIZE,
            self.bird_y + BIRD_SIZE,
            fill="yellow",
            outline="orange",
            width=3
        )

        self.pipes = []

        self.score_text = self.canvas.create_text(
            60, 40,
            text="Score: 0",
            font=("Arial", 20, "bold"),
            fill="white"
        )

        self.create_pipe()
        self.update_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = EgoBirdGame(root)
    root.mainloop()
