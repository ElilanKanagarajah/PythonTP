import tkinter as tk
import random
class Game:

    def __init__(self, root):
        self.root = root
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()
        self.canvas = tk.Canvas(self.game_frame, width=600, height=400, bg="white")
        self.canvas.pack()
        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.food = (300, 300)
        self.direction = (10, 0)
        self.score = 0
        self.bind_keys()

    def bind_keys(self):
        self.root.bind("<Up>", lambda event: self.change_direction(0, -10))
        self.root.bind("<Down>", lambda event: self.change_direction(0, 10))
        self.root.bind("<Left>", lambda event: self.change_direction(-10, 0))
        self.root.bind("<Right>", lambda event: self.change_direction(10, 0))

    def change_direction(self, x, y):
        if (x, y) != (-self.direction[0], -self.direction[1]):
            self.direction = (x, y)

    def draw_game(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill="green")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill="red")
        self.canvas.create_text(10, 10, text=f"Score: {self.score}", font=("Arial", 12))
        self.update_snake()
        self.root.after(100, self.draw_game)

    def update_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.snake.insert(0, new_head)
        if self.snake[0] == self.food:
            self.score += 1
            self.food = (random.randint(0, 59)*10, random.randint(0, 39)*10)
        else:
            self.snake.pop()
        if (self.snake[0][0] < 0 or self.snake[0][0] > 590 or
            self.snake[0][1] < 0 or self.snake[0][1] > 390 or
            self.snake[0] in self.snake[1:]):
            self.game_over()

    def check_collision(self):
        # ... (le code de la méthode check_collision reste inchangé)

        if self.snake_head in self.snake_body[1:]:
            self.game_over()  # Appel la méthode game_over si le serpent se mord la queue
            return True
        return False

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")
        self.root.after(2000, self.root.quit)  # Quitte le jeu après 2 secondes

    def run(self):
        while True:
            self.draw_game()
            if self.check_collision():
                break
            self.root.update()
            self.root.after(100)  # Met à jour le jeu toutes les 100ms