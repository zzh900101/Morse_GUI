import tkinter
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}


##led##
led = LED(4)

###window###
win = Tk()
win.title('Morse Code')
myFont = tkinter.font.Font(family = 'Helvetica',size = 12, weight = "bold")

##


## text box ## 
txtBox = Entry(win)
txtBox.pack()

UppercaseBox = Entry(win)
UppercaseBox.pack()

morsecodeBox = Entry(win)
morsecodeBox.pack()

        
## function of the symbol ##
def dot():
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
    
def dash():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.2)
    
##function##
def insert_point():
    var=txtBox.get()
    print(var)
    
def upper_case():
    var = txtBox.get()
    for letter in var:
        print(letter.upper())
        UppercaseBox.insert('end',letter.upper())

def morse_code():
    var = txtBox.get()
    for letter in var:
        for symbol in CODE[letter.upper()]:
            morsecodeBox.insert('insert',symbol)

def blink():
    var = txtBox.get()
    if (len(var) < 12):
        print('less than 12')
        for letter in var:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.5)
            time.sleep(0.5)
    else:
        print('text length is too long.')

def exit_fun():
    GPIO.cleanup()
    win.destroy()
        
    
## button ##
print_things = Button(win, text="print",command = insert_point)
print_things.pack()

covert_to_uppercase = Button(win,text = "uppercase", command = upper_case)
covert_to_uppercase.pack()

transfer_to_morse_code = Button(win,text = "morse code transfer", command = morse_code)
transfer_to_morse_code.pack()

blink_button = Button(win,text = "start to blink", command = blink)
blink_button.pack()

exit_button = Button(win, text = "exit" , command = exit_fun)
exit_button.pack()