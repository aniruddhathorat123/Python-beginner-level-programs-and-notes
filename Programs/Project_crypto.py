# small project where take input string from user.
# encrypt the input from user and show encrypted message to user.
# same for decrypt, take encrypted text and show decrypted message.


def main():
    keys = "abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1] + keys[0:-1]
    # create dictionaries for encrypton and decryption.
    dict_enc = dict(zip(keys, values))
    dict_dec = {value:key for key, value in dict_enc.items()}
    # take input from the user
    msg = input("Enter the message: ")
    mode = input("Enter 'e' to encrypt and any key to decrypt: ")
    new_msg = ""
    if mode.lower() == 'e':
        new_msg = "".join([dict_enc[key] for key in msg.lower()])
    else:
        new_msg = "".join([dict_dec[key] for key in msg.lower()])
    return new_msg.capitalize()

print(main())

#OP: 
# Enter the message: Hello guys
# Enter 'e' to encrypt and any key to decrypt: e
# Gdkknzftxr

# Enter the message: Gdkknzftxr
# Enter 'e' to encrypt and any key to decrypt: d
# Hello guys
