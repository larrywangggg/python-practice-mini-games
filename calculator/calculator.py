import tkinter

button_values = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = {'÷', 'x', '-', '+', '='}   
top_columns = {'AC', '+/-', '%'}

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_orange = "#FF9500"
color_white = "white"
color_dark_gray = "#505050"

#window steup
window = tkinter.Tk() #create the main window
window.title("Calculator")
window.resizable(False, False) #disable resizing the window

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font = ("Arial", 45),
                      bg = color_black, fg = color_white,
                      anchor = "e") #anchor = "e" short for "east"means align to the right
label.grid(row=0,column=0, columnspan=column_count, sticky="we") #span all columns, sticky = "we" means stretch to west and east

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,command =lambda value= value: button_click(value))
        button.grid(row=row+1, column=column)
                
        
        
frame.pack()

def button_click(value):
    pass

window.mainloop() #start the event loop
