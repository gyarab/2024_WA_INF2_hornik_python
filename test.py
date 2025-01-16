def morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
        ':': '---...', ';': '-.-.-.', "'": '.----.', '"': '.-..-.',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '@': '.--.-.', ' ': '/',  
    }

    def remove_diacritics(text):
        diacritics_map = {
            'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i',
            'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u',
            'ů': 'u', 'ý': 'y', 'ž': 'z',
        }
        normalized_text = ''
        for char in text:
            if char in diacritics_map:
                normalized_text += diacritics_map[char]
            else:
                normalized_text += char
        return normalized_text
    
    normalized_text = remove_diacritics(text)

    morse_code = []
    for char in normalized_text.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            continue

    return ' '.join(morse_code)

if __name__ == "__main__":
    print(morse("Hello World"))
    print(morse("Ahoj světe!"))
    

