def caesar_encode(text, shift=3):
    encoded_text = ""
    for char in text:
        if char.isalpha() and char.isascii():  
            start = 65 if char.isupper() else 97
            encoded_char = chr(((ord(char) - start + shift) % 26) + start)
            encoded_text += encoded_char
        elif not char.isalnum():
            encoded_text += " "
        else:
            raise ValueError("Používej jen PÍSMENA z anglické abecedy.")
    return encoded_text

def caesar_decode(text, shift=3):
    decoded_text = ""
    for char in text:
        if char.isalpha() and char.isascii():  
            start = 65 if char.isupper() else 97
            decoded_char = chr(((ord(char) - start - shift) % 26) + start)
            decoded_text += decoded_char
        elif not char.isalnum():
            decoded_text += " "
        else:
            raise ValueError("Používej jen PÍSMENA z anglické abecedy.")
    return decoded_text

if __name__ == "__main__":
    text = "Hello"
    encoded = caesar_encode(text)
    print(encoded)
    text = "Kh oor"
    decoded = caesar_decode(text)
    print(decoded)
    text = "Arabska"
    encoded = caesar_encode(text)
    print(encoded)
    text = "Yixyixyix"
    encoded = caesar_encode(text)
    print(encoded)


