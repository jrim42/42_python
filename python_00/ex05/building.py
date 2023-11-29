import string

def calculate_character_sums(text):
    if text is None or len(text) == 0:
        return 0, 0, 0, 0, 0

    upper_sum = sum(1 for char in text if char.isupper())
    lower_sum = sum(1 for char in text if char.islower())
    punctuation_sum = sum(1 for char in text if char in string.punctuation)
    space_sum = sum(1 for char in text if char.isspace())
    digit_sum = sum(1 for char in text if char.isdigit())

    return upper_sum, lower_sum, punctuation_sum, space_sum, digit_sum

def main():
    input_text = input("What is the text to count?\n")

    upper_sum, lower_sum, punctuation_sum, space_sum, digit_sum = calculate_character_sums(input_text)

    total_characters = len(input_text)
    output = (
        f"The text contains {total_characters} characters:\n"
        f"{upper_sum} upper letters\n"
        f"{lower_sum} lower letters\n"
        f"{punctuation_sum} punctuation marks\n"
        f"{space_sum} spaces\n"
        f"{digit_sum} digits"
    )

    print(output)

if __name__ == "__main__":
    main()
