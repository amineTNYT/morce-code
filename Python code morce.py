#             text = input("\nEnter the text to convert to Morse code: ").strip()
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
