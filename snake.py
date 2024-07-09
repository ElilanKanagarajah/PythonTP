import tkinter as tk
import random

# Window setup
window = tk.Tk()
window.title("The Snake")
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
height = str(int(screen_height/1.1))
width = str(int(screen_width/2))
window.geometry(width + "x" + height + "+0+0")

# Game setup
plateau_width = screen_width / 2
plateau_height = screen_height / 1.2
plateau = tk.Canvas(window, width=plateau_width, height=plateau_height, bg="pink")
plateau.pack(side="bottom")

score_bar = tk.Text(window, width=int(screen_width / 2), height=int(plateau_height / 10), bg="light blue")
score_bar.pack(side="top")
score_bar.insert(tk.END, "score: 0\n")

# Game constants
num_cases = 75
case_width = plateau_width / num_cases
case_height = plateau_height / num_cases

# Functions
def fill_case(x, y):
    x1 = x * case_width
    y1 = y * case_height
    x2 = x1 + case_width
    y2 = y1 + case_height
    plateau.create_rectangle(x1, y1, x2, y2, fill="green")

def random_case():
    x = random.randint(0, num_cases - 1)
    y = random.randint(0, num_cases - 1)
    return (x, y)

def draw_snake(snake):
    for case in snake:
        x, y = case
        fill_case(x, y)

def is_in_snake(case):
    if case in snake:
        return 1
    else:
        return 0

def random_fruit():
    fruit = random_case()
    while is_in_snake(fruit):
        fruit = random_case()
    return fruit

def draw_fruit():
    global fruit
    x, y = fruit
    x1 = x * case_width
    y1 = y * case_height
    x2 = x1 + case_width
    y2 = y1 + case_height
    plateau.create_oval(x1, y1, x2, y2, fill="red")

def left_key(event):
    global movement
    movement = (-1, 0)

def right_key(event):
    global movement
    movement = (1, 0)

def up_key(event):
    global movement
    movement = (0, -1)

def down_key(event):
    global movement
    movement = (0, 1)

window.bind("<Left>", left_key)
window.bind("<Right>", right_key)
window.bind("<Up>", up_key)
window.bind("<Down>", down_key)

def snake_dead(new_head):
    global lost
    new_head_x, new_head_y = new_head
    if (is_in_snake(new_head) and movement != (0, 0)) or new_head_x < 0 or new_head_y < 0 or new_head_x >= num_cases or new_head_y >= num_cases:
        lost = 1

def update_score():
    global score
    score += 1
    score_bar.delete(0.0, 3.0)
    score_bar.insert(tk.END, "score: " + str(score) + "\n")

def update_snake():
    global snake, fruit
    old_head_x, old_head_y = snake[0]
    movement_x, movement_y = movement
    new_head_x = old_head_x + movement_x
    new_head_y = old_head_y + movement_y
    snake.insert(0, (new_head_x, new_head_y))
    if snake[0] == fruit:
        update_score()
        fruit = random_fruit()
    else:
        snake.pop()

def task():
    window.update()
    window.update_idletasks()
    update_snake()
    plateau.delete("all")
    draw_fruit()
    draw_snake(snake)
    if lost:
        score_bar.delete(0.0, 3.0)
        score_bar.insert(tk.END, "Lost with a score of " + str(score))
        reset_game()
    else:
        window.after(70, task)

def reset_game():
    global snake, fruit, movement, score, lost
    snake = [random_case()]
    fruit = random_fruit()
    movement = (0, 0)
    score = 0
    lost = 0
    task()

snake = [random_case()]
fruit = random_fruit()
movement = (0, 0)
score = 0
lost = 0

window.after(0, task)
window.mainloop()