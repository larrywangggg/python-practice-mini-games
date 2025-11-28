import os
import tkinter
import random
os.environ["TK_SILENCE_DEPRECATION"] = "1"


ROWS = 25
COLS = 25
TILE_SIZE = 25
game_over = False
score = 0

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window 
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(
    window,
    bg="black", 
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    borderwidth=0, 
    highlightthickness=0)
canvas.pack()
window.update_idletasks()


#获取窗口和电脑显示器屏幕尺寸
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#计算左上角点的坐标
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
#center the window, format: widthxheight+x+y
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#initialize game
snake = Tile(5* TILE_SIZE,5 * TILE_SIZE) #single tile, snakes head)
food = Tile(10* TILE_SIZE,10 * TILE_SIZE) #single tile, food position
snake_body = [] #list to store snake body parts
velocityX = 0
velocityY = 0

def change_direction(e): #e for event
    #print(e.keysym)# print the key symbol
    global velocityX, velocityY, game_over
    
    if game_over:
        return
    
    if e.keysym == "Up" and velocityY != 1: #prevent snake from going back on itself
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0


def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return
    
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or
        snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return
        
    #collision with food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y)) #add new body part at snake's current position
        #relocate food after being eaten
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1
    
    #update snake body from tail to head
    for i in range(len(snake_body) - 1, -1, -1):
      tile = snake_body[i]
      if i == 0:
          tile.x = snake.x
          tile.y = snake.y
      else:
          previous_tile = snake_body[i - 1]
          tile.x = previous_tile.x
          tile.y = previous_tile.y
          
          
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
    
    
    
def draw():
    global snake, food, snake_body, game_over, score
    move()
    canvas.delete("all") #clear canvas
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red") 
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green")
    
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="lime green")
   
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, fill="white", font=("Arial", 20), text= f"Game Over: {score} points")
    else:
        canvas.create_text(30,20, fill="white", font=("Arial", 10), text= f"Score: {score}")
    
    window.after(100, draw) #redraw every 100 ms, 10 frames per second
    
draw()
 
window.bind("<KeyRelease>",change_direction)    
window.mainloop()
