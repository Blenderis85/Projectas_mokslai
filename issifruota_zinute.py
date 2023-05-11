def decrypt_char(char, key):
    return chr(((ord(char) - ord('A')) + 26 - key) % 26 + ord('A'))

def decrypt_message(cipher, key):
    message = ''
    for c in cipher:
        if c in ' ,.':
            message = message + c
        else:
            message = message + decrypt_char(c, key)
    return message

decrypted_message = decrypt_message('NHVWLV NLHWDV', 3)
print(decrypted_message)