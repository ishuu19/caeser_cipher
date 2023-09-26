### cipher


want = input('Do you want to encode or decode?').lower()
ques = input('Enter the text you want to encode or decode (Please write withot spaces): ').lower()
shifts = int(input("Enter the number of shifts you want: "))


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def encrypt(text, shift):
    cipher_text = ''
    for letter in ques:
        position = letters.index(letter)
        new_position = position + shift
        new_letter = letters[new_position]
        cipher_text += new_letter
    print(f'the encoded text is: {cipher_text}')



def decrypt(text, shift):
    cipher_text = ''
    for letter in ques:
        position = letters.index(letter)
        new_position = position - shift
        new_letter = letters[new_position]
        cipher_text += new_letter
    print(f'the decoded text is: {cipher_text}')


if want == 'encode':
    encrypt(text = ques, shift= shifts)
elif want == 'decode':
    decrypt(text = ques, shift= shifts)
else:
    print("Please enter a valid command!")