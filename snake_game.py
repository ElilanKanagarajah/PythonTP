import tkinter as tk
from game_by import Game

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()
        self.create_menu()

    def create_menu(self):
        tk.Button(self.menu_frame, text="Start Game", command=self.start_game).pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Quit", command=self.root.quit).pack(side=tk.LEFT)

    def start_game(self):
        self.menu_frame.pack_forget()
        game = Game(self.root)
        game.run()

    def run(self):
        while True:
            game.draw_game()
            if self.check_collision():
                break
            self.root.update()
            self.root.after(100)  # Met à jour le jeu toutes les 100ms

if __name__ == "__main__":
    game = SnakeGame()
    game.run()