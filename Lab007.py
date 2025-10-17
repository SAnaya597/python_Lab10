import string



def vigenere_sq():

    alphabet = string.ascii_uppercase

    header = "|   |" + "|".join([f" {letter} " for letter in alphabet]) + "|"
    print(header)

    separator = "|---|" + "---|" * len(alphabet)
    print(separator)

    for i in range(len(alphabet)):
        row_letter = alphabet[i]
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        row_content = "|".join([f" {letter} " for letter in shifted_alphabet])
        print(f"| {row_letter} |{row_content}|")


def letter_to_index(letter, alphabet):

    return alphabet.index(letter.upper())


def index_to_letter(index, alphabet):

    return alphabet[index]
def vigenere_index(key_letter, plaintext_letter, alphabet):

    p_index = letter_to_index(plaintext_letter, alphabet)
    k_index = letter_to_index(key_letter, alphabet)
    c_index = (p_index + k_index) % len(alphabet)
    return index_to_letter(c_index, alphabet)
def encrypt_vigenere(key, plaintext, alphabet):

    ciphertext = []
    key_length = len(key)
    key_index = 0
    for char in plaintext:
        if char.upper() in alphabet:
            key_letter = key[key_index % key_length]
            encrypted_letter = vigenere_index(key_letter, char, alphabet)
            ciphertext.append(encrypted_letter)
            key_index += 1
        else:
            ciphertext.append(char)
    return "".join(ciphertext)
def undo_vigenere(key_letter, ciphertext_letter, alphabet):
    c_index = letter_to_index(ciphertext_letter, alphabet)
    k_index = letter_to_index(key_letter, alphabet)
    p_index = (c_index - k_index) % len(alphabet)
    return index_to_letter(p_index, alphabet)
def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = []
    key_length = len(key)
    key_index = 0
    for char in cipher_text:
        if char.upper() in alphabet:
            key_letter = key[key_index % key_length]
            decrypted_letter = undo_vigenere(key_letter, char, alphabet)
            plaintext.append(decrypted_letter)
            key_index += 1
        else:
            plaintext.append(char)
    return "".join(plaintext)


def main_loop():
    alphabet = string.ascii_uppercase
    keys = []
    current_key_index = 0
    y = 'yes'
    n = 'no'
    b= 'back'

    while True:
        print("--- Vigenere Cipher---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Dump Encrypted Text")
        print("4. Keys")
        choice = input("Enter your choice: ")


        if choice == "1":
            if not keys:
                print("No keys stored.")
                continue

            key = keys[current_key_index]
            current_key_index = (current_key_index + 1) % len(keys)


            print(f"Using key - {key}")
            plaintext_input = input("Plaintext: ").upper()
            encrypted_message = encrypt_vigenere(key, plaintext_input.replace('',''), alphabet)
            print(f"Encrypted Message - {encrypted_message}")



        elif choice == "2":
            key = input("Enter your key ")
            if key not in keys:
                print("Key not found. EXITING")
                return main_loop()

            ciphertext_input = input("Ciphertext -  ").upper()

            decrypted_message = decrypt_vigenere(key, ciphertext_input.replace('', ''), alphabet)
            print(f"Decrypted Message - {decrypted_message}")


        elif choice == "3":
            print("Returning to main menu")
            continue




        elif choice == "4":
           while True:
                print("------KEY MENU-----")
                print("1. Add key")
                print("2. Remove keys")
                print("3  View keys")
                print("4. Main menu")

                choice = input("Enter your choice -  ")

                if choice == "1":
                    key_input = input("Enter new key")
                    new_keys = [k.strip() for k in key_input.split(',') if k.strip()]
                    keys.extend(new_keys)
                    print(f"New keys: {'.'.join(new_keys)}")



                elif choice == "2":
                    keys.clear()
                    current_key_index = 0
                    print("keys removed")

                elif choice == "3":
                    if keys:
                        print(f"current keys: {", ".join(keys)}")
                        print(f"next key to be used: {keys[current_key_index]}")
                    else:
                        print("No keys")

                elif choice == "4":
                    print("Return to main menu")
                    break




if __name__ == "__main__":
    main_loop()
