alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(i_text, i_shift):
    cipher_text = ''
    for i in i_text:
        pos = alphabet.index(i)
        new_pos = pos + i_shift
        if new_pos > 25:
            new_pos = new_pos - 26
        cipher_text += alphabet[new_pos]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, i_shift):
    decoded_text = ''
    for i in cipher_text:
        pos = alphabet.index(i)
        new_pos = pos - i_shift
        if new_pos < 0:
            new_pos = new_pos + 26
        decoded_text += alphabet[new_pos]
    print(f"The decoded text is {decoded_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
