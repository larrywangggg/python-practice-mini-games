import tkinter as tk

def set_tile(row, col):
    
    pass

def new_game():
    pass

#game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#3b83bd"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

#window setup
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text="current player: " + current_player, font=("Consolas", 20), 
                      bg=color_gray, fg="white")


label.grid(row=0, column=0,columnspan=3,sticky="we")

for row in range(3):
    for col in range(3):
        board[row][col] = tk.Button(frame, text="",font=("Consolas", 50, "bold"), 
                                    bg=color_gray,fg=color_blue,
                                    width=4, height=1,
                                    command=lambda r=row, c=col: set_tile(r, c))
        board[row][col].grid(row=row+1, column=col)

button = tk.Button(frame, text="Reset Game", font=("Consolas", 20),
                   bg=color_gray, fg="white",
                   command=new_game)
button.grid(row=4, column=0,columnspan=3,sticky="we")
frame.pack()

#center the window on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()