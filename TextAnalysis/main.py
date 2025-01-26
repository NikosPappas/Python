import os
import re

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
      print("File not found.")
      return None
    except Exception as e:
      print(f"An error ocurred: {e}")
      return None

def count_lines(text):
  return len(text.splitlines())

def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
   return len(text)

def count_pattern(text, pattern):
    try:
       matches = re.findall(pattern, text)
       return len(matches)
    except re.error:
        print("Invalid regular expression.")
        return None

def get_user_choice():
    while True:
        print("\nAnalysis options:")
        print("1. Count Lines")
        print("2. Count Words")
        print("3. Count Characters")
        print("4. Search for a Pattern")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice, try again.")

def main():
    while True:
        filepath = input("Enter the path of the text file to analyze: ")
        if not os.path.exists(filepath):
            print("Invalid file path. Please try again.")
        else:
            break

    text = read_file(filepath)

    if text is None:
        return
    running = True
    while running:
        choice = get_user_choice()
        match choice:
            case "1":
              lines = count_lines(text)
              print(f"Number of lines: {lines}\n")
            case "2":
              words = count_words(text)
              print(f"Number of words: {words}\n")
            case "3":
              chars = count_characters(text)
              print(f"Number of characters: {chars}\n")
            case "4":
              pattern = input("Enter the regular expression pattern to search for: ")
              count = count_pattern(text, pattern)
              if count is not None:
                  print(f"Number of matches: {count}\n")
            case "5":
              running = False
              print("Exiting Text Analyzer. Goodbye!")

if __name__ == "__main__":
    print("Welcome to the Text File Analyzer!\n")
    main()
