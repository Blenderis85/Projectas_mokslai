def encrypt_char(char, key):
    return chr((ord(char) - ord('A') + key) % 26 + ord('A'))

def encrypt_message(message, key):
    message = message.upper()
    cipher = ''
    for c in message:
        if c in ' .,':
            cipher = cipher + c
        else:
            cipher = cipher + encrypt_char(c, key)
    return cipher

encrypted_message = encrypt_message("you are awesome", 3)
print(encrypted_message)
