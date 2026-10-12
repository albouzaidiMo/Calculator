import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

color_white = "white"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_light_gray = "#D4D4D2"
color_orange = "#FF9500"

#setup window
window = tkinter.Tk()   #create window
window.title("Calculator")
window.resizable(False, False)   # (width,hight)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial",45), background=color_black,
                       foreground=color_white)


window.mainloop() #don't disappear after uses
