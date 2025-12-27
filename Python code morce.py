# High-quality Interactive Morse Code Translator in Python
# Supports text to Morse code and Morse code to text translation
# Handles letters (A-Z), numbers (0-9), and spaces
# Input is case-insensitive for text to Morse
# For Morse to text: use '.' for dot, '-' for dash, space between letters, '/' or multiple spaces for word separation

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Word separator in Morse
}

# Reverse dictionary for decoding
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Convert text to Morse code."""
    text = text.upper()
    morse = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')  # Unknown character
    return ' '.join(morse)

def morse_to_text(morse):
    """Convert Morse code to text."""
    # Normalize input: replace multiple spaces with single, and allow '/' as word space
    morse = morse.replace('/', ' / ')  # Ensure word separators are handled
    codes = morse.split(' ')
    text = []
    for code in codes:
        if code == '' or code == '/':
            text.append(' ')  # Word space
        elif code in REVERSE_DICT:
            text.append(REVERSE_DICT[code])
        else:
            text.append('?')  # Unknown code
    result = ''.join(text)
    # Clean up multiple spaces
    while '  ' in result:
        result = result.replace('  ', ' ')
    return result.strip()

def main_menu():
    """Interactive menu loop."""
    print("\n" + "="*50)
    print("    Welcome to Morse Code Translator")
    print("="*50)
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            text = input("\nEnter the text to convert to Morse code: ").strip()
            if text:
                result = text_to_morse(text)
                print(f"\nMorse Code:\n{result}")
            else:
                print("Error: Empty input!")
        
        elif choice == '2':
            morse = input("\nEnter Morse code (use . and -, space between letters, / or extra space between words): ").strip()
            if morse:
                result = morse_to_text(morse)
                print(f"\nDecoded Text:\n{result}")
            else:
                print("Error: Empty input!")
        
        elif choice == '3':
            print("\nGoodbye! Thanks for using Morse Code Translator.")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
