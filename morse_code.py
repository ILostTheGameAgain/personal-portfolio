#Alec George Simple Morse Code Translator

#will give the user the option to either translate a line of morse code to english or english to morse code

#function to translate english into morse code
def eng_to_morse(phrase, english, morse_code):
    end_value = ""
    for i in range(len(phrase)):
        if phrase[i] not in english: #stupid proof
            return "\nplease only type letters and spaces, this wasn't coded to translate numbers or special characters."
        end_value += f" {morse_code[english.index(phrase[i])]}"

    return end_value


#function to translate morse code into english
def morse_to_eng(phrase, english, morse_code):
    end_value = ""
    for i in range(len(phrase)):
        if phrase[i].strip() not in morse_code: #stupid proof
            return "\nplease only type letters and spaces, this wasn't coded to translate numbers or special characters."
        end_value += f" {english[morse_code.index(phrase[i])]}"

    return end_value


#main function
def main():
    #list of english letters and morse code letters with corresponding letters having the same index
    english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]
    while True: #repeat the function
        #user input to decide if they're going from english to morse code or morse code to english, supid proofed
        while True: #stupid proof while loop
            choice = input("\nwhat would you like to do? type:\n 1 to translate English to morse code\n 2 to translate morse code to english\n 3 to exit program\n your answer here (type 1, 2, or 3): ")
            if choice in "123" and len(choice) == 1:
                break
            else:
                print("\ninvalid input")

        #use choice to decide what to do
        if choice == "1":
            print(eng_to_morse(input("\nwhat would you like to translate? (only letters and spaces, no numbers or special characters): ").strip().lower(), english, morse_code))
        
        elif choice == "2":
            print(morse_to_eng(input('\nwhat would you like to translate? Type:\n "." for dots\n "-" for dashes\n "/" for spaces\n separate letters with spaces\n this will only translate to letters and spaces, don\'t input morse code for numbers or special characters.\n Your answer here: ').strip().split(), english, morse_code))

        elif choice == "3":
            break
