alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Prints the encoded or decoded message 
def ceasar(message,shift_amount,encode_or_decode): 
    cipher_text = '' # Store the resulting text

    if encode_or_decode=='decode': # Reverse the shift for decoding
        shift_amount *= -1 

    for letter in message:
        if letter not in alphabet: # Non-alphabetic characters are added unchanged
            cipher_text += letter
        else:
            # Find the new position after shifting
            new_alphabet_pos = alphabet.index(letter)+shift_amount
            new_alphabet_pos %= 26
            cipher_text += alphabet[new_alphabet_pos]

    print(f'{encode_or_decode}d result: '+cipher_text)

# Main program loop
while True:
    print("Enter encode to encode a message")
    print("Enter decode to decode a message")
    print("Enter exit to exit the program \n")

    user_option = (input()).strip().lower()
    print('')

    if user_option in ['encode', 'decode']:
        message = input(f'Enter the message to {user_option}: ')
        shift = int(input('Enter the shift number: '))
        ceasar(message, shift, user_option)
        print(' \n')    
        continue 
    
    if user_option == 'exit':
        break

    else:
        print('Invalid option. Please try again.\n')
        continue

