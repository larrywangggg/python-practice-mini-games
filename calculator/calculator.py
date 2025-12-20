import tkinter

button_values = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = {'÷', 'x', '-', '+', '='}   
top_symbols = {'AC', '+/-', '%'}

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
                      anchor = "e",
                      width=column_count) #anchor = "e" short for "east"means align to the right
label.grid(row=0,column=0, columnspan=column_count, sticky="we") #span all columns, sticky = "we" means stretch to west and east

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,command =lambda value= value: button_click(value),
                                relief="flat",        
                                bd=0,                
                                highlightthickness=0)
        
        if value in top_symbols:
            button.config(bg=color_light_gray, fg=color_black)
        elif value in right_symbols:
            button.config(bg=color_orange, fg=color_white)
        else:
            button.config(bg=color_dark_gray, fg=color_white)
            
        button.grid(row=row+1, column=column) #row+1 because row 0 is used by the label
                        
frame.pack()

#A+B, A-B, A*B, A/B, √A, +/ - A, A%, AC
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator, label
    A = "0"
    B = None
    operator = None
    
def remove_zero_decimal(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

#center the window on the screen
window.update() #update the window to get the correct dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()   
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def button_click(value):
    global right_symbols, top_symbols, label, A, B, operator
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A) 
                numB = float(B)
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decimal(numA / numB)
                
                clear_all()
                        
        elif value in "÷x-+":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
                
            operator = value
        
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else: #digit or .
        if value == ".":
            if value not in label["text"]:  #avoid multiple decimals
                label["text"] += value 
            pass
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace the 0 with the digit
            else:
                label["text"] += value #append the digit to the current number



window.mainloop() #start the event loop
