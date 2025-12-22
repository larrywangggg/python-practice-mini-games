import tkinter

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
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

window.mainloop()