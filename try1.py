import tkinter as tk
from tkinter import *

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}
def convert():
    a = text_entry.get("1.0", "end-1c")
    b = int(choice_var.get())
    
    if b == 1:
        a = a.upper()
        morse_code = ""
        for char in a:
            if char in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[char] + " "
            else:
                morse_code += char + " "
        output_text.delete("1.0", "end")
        output_text.insert("1.0",   morse_code)
    elif b == 2:
        morse_code = a.split()
        text = ""
        for code in morse_code:
            for key, value in MORSE_CODE_DICT.items():
                if value == code:
                    text += key
                    break
            else:
                text += code
        output_text.delete("1.0", "end")
        output_text.insert("1.0", text)

def clear_text_boxes():
    text_entry.delete("1.0", "end")
    output_text.delete("1.0", "end")
    # Creating the main GUI window
root = tk.Tk()
root.title("Morse Code Converter")
root.configure(bg="#36454f")
root.geometry('600x475')


# Creating input label and text box
input_label = tk.Label(root, text="Enter the text:", font=("Helvetica", 15, "italic"),fg="white", bg="#36454f")
input_label.pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.configure(bg="black", foreground="white", font=("Helvetica", 12, " italic"))
text_entry.pack()
# Creating choice label and radio buttons
choice_label = tk.Label(root)
choice_label.configure(bg="#36454f", foreground="#36454f", font=("Helvetica", 12, "bold italic"))
choice_label.pack()
choice_var = tk.StringVar()
choice_var.set("1")
radio1 = tk.Radiobutton(root, height=1, width=10, text="Alphabets", font=("Helvetica", 12, "italic"), fg="white", bg="#9897A9", indicatoron=False, selectcolor="#564C4D", variable=choice_var, value="1", highlightthickness=0)
radio2 = tk.Radiobutton(root, height=1, width=10, text="Morse Code",font=("Helvetica", 12, "italic"),fg="white", bg="#9897A9", indicatoron=False, selectcolor="#564C4D",variable=choice_var, value="2" , highlightthickness=0)
radio1.pack(padx=10, pady=(0, 10)) 
radio2.pack(padx=10, pady=(0, 10))

# Creating Convert button & output label
convert_button = tk.Button(root, height=1, width=10, text="Convert",font=("Helvetica", 12, "italic"), fg="white", bg="#36454f",command=convert)
convert_button.pack(pady=(10, 0))
choice_labe2 = tk.Label(root)
choice_labe2.configure(bg="#36454f", foreground="#36454f", font=("Helvetica", 12, "bold italic"))
choice_labe2.pack()
clear_button = tk.Button(root, height=1, width=10, text="Clear",font=("Helvetica", 12, "italic"), fg="white", bg="#36454f", command=clear_text_boxes)
clear_button.pack(pady=(0, 10))
output_label = tk.Label(root, text="Output text:", font=("Helvetica", 15, "italic"),fg="white", bg="#36454f")
output_label.pack()

# Create output text box
output_text = tk.Text(root, height=5, width=60)
output_text.configure(bg="black", foreground="#03C04A", font=("Helvetica", 12, "italic"))
output_text.pack()

# Start the GUI event loop
root.mainloop()
