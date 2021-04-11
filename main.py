from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""
    if direction == "d":
        shift *= -1
    for char in text:

        if char in alphabet:
            position = (alphabet.index(char) + shift) % 26
            char = alphabet[position]
        end_text += char

    print(f"Here's the {direction}d result: {end_text}")


print(logo)

user = "yes"
while user == "yes":
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user = input("Do you want to go again? If yes, type 'yes', else type 'no'\n")
print("bye! See you soon.")
