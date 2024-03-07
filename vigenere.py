def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ""
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
                shift = ord(keyword[keyword_index % len(keyword)]) - ord("A")
                ciphertext += chr((ord(char) - base + shift) % 26 + base)
                keyword_index += 1
            else:
                base = ord("a")
                shift = 0
                ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char

    return ciphertext


# len(key)*x=len(plaintext), x=len(plaintext)/len(key) mod len(keyword)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    ciphertext = ""
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            shift = ord(keyword[keyword_index % len(keyword)]) - base
            decrypted_char = chr(((ord(char) - base - shift) % 26) + base)
            ciphertext += decrypted_char
            keyword_index += 1
        else:
            ciphertext += char
    return ciphertext
