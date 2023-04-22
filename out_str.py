import pyperclip

# Take inputs from the console
color = input("Enter a color: ")
repetitions = int(input("Enter a number of repetitions: "))

# Generate the text with inputs substituted in
output = ""
for i in range(1, repetitions + 1):
    c_repetition = str(i)
    output += f"{color}_OUT_STR_{c_repetition}\n"
    output += "\t" + "movf\tINDEX, W\n"
    output += "\t" + f"call\t{color}_LOOK{c_repetition}\n"
    output += "\t" + "movwf\ttemp\n"
    output += "\t" + "addlw\t01h\n"
    output += "\t" + "btfsc\tSTATUS, Z\n"
    output += "\t" + "return\n"
    output += "\t" + "movf\ttemp,W\n"
    output += "\t" + "movwf\tTXREG\n"
    output += "\t" + "nop\n"
    output += "\t" + "call\tTransmit\n"
    output += "\t" + "incf\tINDEX, F\n"
    output += "\t" + f"goto\t{color}_OUT_STR_{c_repetition}\n\n"

# Copy the generated text to clipboard
pyperclip.copy(output)
print("Generated text has been copied to clipboard!")
