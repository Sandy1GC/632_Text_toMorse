import pandas as pd
import re
data = pd.read_csv('morse_base.csv', on_bad_lines='skip')
def check():
    global text_x
    text_x = input("\nGive here the Morse code or plain text: ").upper()
    if re.match("[0-9A-Z]+", text_x):
        print("True1 Plain Text\n")
        encode()
    elif re.match("[ .,+∙•●◎☉⦾⦿◍◌○◉⊛⊚⊙◦。❍⬤⚉⚇◑◐◓◒◔◕◙◘〇◯⊖⊕⚯⧂⚫_-]", text_x):
        print("That's Morse")
        decode()
    else:
        print("There are not enough symbols. Try again.")
        check()

def decode():
    split_the_input= text_x.split(' ')
    full_decode_text = ""
    for d in split_the_input:
        matches = data[data['code'] == d]
        if not matches.empty:
            equal_letter = matches.iloc[0]['symbol']
            print(f"Equal for combination '{d}': {equal_letter}")
            full_decode_text += str(equal_letter)
        else:
            print(f"No match found for combination '{d}'")
            full_decode_text += str(" ")
    print(f"\n{full_decode_text}")
    check()

def encode():
    encode_the_input = list(text_x)
    full_code_text = ""
    for e in encode_the_input:
        matches = data[data['symbol'] == e]
        if not matches.empty:
            code_letter = matches.iloc[0]['code']
            print(f"Encode symbol'{e}': [{code_letter}]")
            full_code_text += str(f' {code_letter}')
        else:
            print(f"No match found for symbol '{e}'")
            full_code_text += str(" ")
    print(f"\n{full_code_text}")
    check()
check()