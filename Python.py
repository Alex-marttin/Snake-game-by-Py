import tkinter as tk
import random

class SnakeGame:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.speed = 70

        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.snake = []
        self.snake.append([self.width / 2, self.height / 2])
        self.direction = "down"

        self.food = None
        self.create_food()

        self.window.bind("<Key>", self.on_key_press)

        self.game_over = False
        self.score = 0

        self.create_restart_button()

        self.update()

    def create_food(self):
        x = random.randint(0, (self.width // 10) - 1) * 10
        y = random.randint(0, (self.height // 10) - 1) * 10
        self.food = (x, y)

    def on_key_press(self, event):
        if event.keysym == "Up" and self.direction != "down":
            self.direction = "up"
        elif event.keysym == "Down" and self.direction != "up":
            self.direction = "down"
        elif event.keysym == "Left" and self.direction != "right":
            self.direction = "left"
        elif event.keysym == "Right" and self.direction != "left":
            self.direction = "right"

    def move_snake(self):
        head = self.snake[0]
        x, y = head

        if self.direction == "up":
            y -= 10
        elif self.direction == "down":
            y += 10
        elif self.direction == "left":
            x -= 10
        elif self.direction == "right":
            x += 10

        self.snake.insert(0, (x, y))

        if self.snake[0] == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()

        if (x < 0 or x > self.width or
            y < 0 or y > self.height or
            self.snake[0] in self.snake[1:]):
            self.game_over = True

    def update(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="light green")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red")

        if self.game_over:
            self.canvas.create_text(self.width / 2, self.height / 2, text=f"Game Over\nScore: {self.score}", font=("Arial", 32), fill="red")
            self.restart_button.config(state="normal")
        else:
            self.move_snake()
            self.window.after(self.speed, self.update)

    def create_restart_button(self):
        self.restart_button = tk.Button(self.window, text="Restart", font=("Arial", 24), command=self.restart_game, state="disabled")
        self.restart_button.pack()

    def restart_game(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        self.snake = []
        self.snake.append([self.width / 2, self.height / 2])
        self.direction = "down"
        self.food = None
        self.create_food()
        self.window.bind("<Key>", self.on_key_press)
        self.game_over = False
        self.score = 0
        self.create_restart_button()
        self.update()

if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()
