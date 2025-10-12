def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def play_game():
    print("Welcome to the Roman Numeral Converter Game!")
    while True:
        try:
            number = int(input("Type a number (1-3999) to convert to Roman numeral (or 0 to quit): "))
            if number == 0:
                print("Goodbye!")
                break
            if 1 <= number <= 3999:
                print(f"Roman numeral: {int_to_roman(number)}")
            else:
                print("Please enter a number between 1 and 3999.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    play_game()