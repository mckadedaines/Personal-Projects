morse_code_dict = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(user_english):
    morse_code = ""
    for char in user_english.upper():
        if char == " ":
            morse_code += "   "
        elif char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code[:-1]

def decrypt(user_code):
    message = ""
    words = user_code.split("   ")
    for word in words:
        chars = word.split(" ")
        for code in chars:
            for char, morse in morse_code_dict.items():
                if morse == code:
                    message += char
        message += " "
    return message

def main():
    while True:
        print("\n1. English to Morse Code, \n2. Morse Code to English, \n3. Quit\n")
        user_input = input("Please select your option: \n")

        if user_input == "1":
            user_english = input("Please type what you would like translated: ")
            result = encrypt(user_english)
            print(f"\nTranslated Morse Code:\n{result}")

        elif user_input == "2":
            user_code = input("Please type what you would like translated: ")
            result = decrypt(user_code)
            print(f"\nTranslated Text:\n{result}")

        elif user_input == "3":
            print("Thanks for using the translator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()