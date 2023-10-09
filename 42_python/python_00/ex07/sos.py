NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
}

def encode_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            raise AssertionError(" the arguments are bad")
    return morse_code

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise AssertionError(" the arguments are bad")
    
    try:
        morse_result = encode_to_morse(sys.argv[1])
        print(morse_result)
    except AssertionError as e:
        print(e)
