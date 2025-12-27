

import os
import time
import sys
from datetime import datetime

# Try to use pygame for better audio, fall back to simple beep
try:
    import pygame
    pygame.init()
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

# Morse code dictionary (International Morse Code + common punctuation)
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....', 'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',   'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',  'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' / '  # Word space
}

REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items() if k != ' '}

# Timing constants (in seconds)
DOT_DURATION = 0.2
DASH_DURATION = DOT_DURATION * 3
SYMBOL_GAP = DOT_DURATION
LETTER_GAP = DOT_DURATION * 3
WORD_GAP = DOT_DURATION * 7

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def beep(frequency=800, duration=0.1):
    if SOUND_AVAILABLE:
        sound = pygame.mixer.Sound(buffer=pygame.sndarray.make_sound(
            pygame.sndarray.samples(pygame.mixer.Sound(pygame.mixer.Sound(buffer=b'\x00\x7F' * int(44100 * duration / 100))), (44100,)))
        sound.set_volume(0.3)
        sound.play()
        time.sleep(duration)
    else:
        # Fallback to system beep (Windows) or print bell (others)
        if os.name == 'nt':
            import winsound
            winsound.Beep(frequency, int(duration * 1000))
        else:
            print('\a', end='')
            time.sleep(duration)

def flash_symbol(symbol):
    if symbol == '.':
        print("🔴", end='', flush=True)
        time.sleep(DOT_DURATION)
        print("\b \b", end='', flush=True)
    elif symbol == '-':
        print("🟥" * 3, end='', flush=True)
        time.sleep(DASH_DURATION)
        print("\b \b" * 3, end='', flush=True)

def play_morse_audio(morse):
    print("\nPlaying Morse code audio...\n")
    for symbol in morse.replace(' ', ''):
        if symbol == '.':
            beep(800, DOT_DURATION)
        elif symbol == '-':
            beep(800, DASH_DURATION)
        time.sleep(SYMBOL_GAP)
    print("Done playing.\n")

def flash_morse_visual(morse):
    print("\nFlashing Morse code visually...\n")
    for symbol in morse:
        if symbol == '.':
            flash_symbol('.')
            time.sleep(SYMBOL_GAP)
        elif symbol == '-':
            flash_symbol('-')
            time.sleep(SYMBOL_GAP)
        elif symbol == ' ':
            time.sleep(LETTER_GAP - SYMBOL_GAP)
        elif symbol == '/':
            time.sleep(WORD_GAP - LETTER_GAP)
    print("\nDone flashing.\n")

def text_to_morse(text):
    text = text.upper()
    morse_parts = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_parts.append(MORSE_CODE_DICT[char])
        else:
            morse_parts.append('<?>')  # Unknown
    return ' '.join(morse_parts)

def morse_to_text(morse):
    morse = morse.strip()
    # Normalize separators
    morse = morse.replace('/', ' / ').replace('  ', ' ')
    words = morse.split(' / ')
    result = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(REVERSE_DICT.get(code, '?') for code in letters)
        result.append(decoded_word)
    return ' '.join(result)

def save_translation(text, morse):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("morse_history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\nText: {text}\nMorse: {morse}\n{'-'*50}\n")
    print("Translation saved to 'morse_history.txt'")

def load_history():
    if os.path.exists("morse_history.txt"):
        with open("morse_history.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("No history file found.")

def main_menu():
    while True:
        clear_screen()
        print("\033[96m" + "="*60)
        print("    🚨 MORSE CODE TRANSLATOR PRO 🚨".center(60))
        print("="*60 + "\033[0m")
        print("\n\033[1mMain Menu:\033[0m")
        print("1. Text → Morse Code")
        print("2. Morse Code → Text")
        print("3. Play Morse Code (Audio)")
        print("4. Flash Morse Code (Visual)")
        print("5. Save Last Translation")
        print("6. View History")
        print("7. Exit")
        
        choice = input("\n\033[93mEnter your choice (1-7): \033[0m").strip()
        
        if choice == '1':
            text = input("\n\033[92mEnter text to convert: \033[0m").strip()
            if text:
                morse = text_to_morse(text)
                print(f"\n\033[95mMorse Code:\033[0m\n{morse}")
                last_translation = (text, morse)
            else:
                print("\033[91mError: Empty input!\033[0m")
        
        elif choice == '2':
            morse = input("\n\033[92mEnter Morse code (. - / separators): \033[0m").strip()
            if morse:
                text = morse_to_text(morse)
                print(f"\n\033[95mDecoded Text:\033[0m\n{text}")
                last_translation = (text, morse)
            else:
                print("\033[91mError: Empty input!\033[0m")
        
        elif choice == '3':
            if 'last_translation' in locals() and last_translation[1]:
                play_morse_audio(last_translation[1].replace('/', ' '))
            else:
                print("\033[91mNo Morse code to play! Convert text first.\033[0m")
        
        elif choice == '4':
            if 'last_translation' in locals() and last_translation[1]:
                flash_morse_visual(last_translation[1])
            else:
                print("\033[91mNo No Morse code to flash! Convert text first.\033[0m")
        
        elif choice == '5':
            if 'last_translation' in locals():
                save_translation(*last_translation)
            else:
                print("\033[91mNothing to save yet!\033[0m")
        
        elif choice == '6':
            load_history()
        
        elif choice == '7':
            print("\n\033[96mThank you for using Morse Code Translator Pro!\033[0m")
            print("73 (Best regards) 👋\n")
            break
        
        else:
            print("\033[91mInvalid choice! Please try again.\033[0m")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        last_translation = None
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[96mGoodbye! 73 👋\033[0m")
    finally:
        if SOUND_AVAILABLE:
            pygame.quit()
