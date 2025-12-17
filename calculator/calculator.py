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