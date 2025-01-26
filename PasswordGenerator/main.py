import random
import string

def generate_password(length, use_lower, use_upper, use_numbers, use_special):
  all_chars = ""
  if use_lower:
    all_chars += string.ascii_lowercase
  if use_upper:
    all_chars += string.ascii_uppercase
  if use_numbers:
      all_chars += string.digits
  if use_special:
      all_chars += string.punctuation

  if not all_chars:
     return "At least one type of characters should be requested"

  if length < len(all_chars):
     return "The password length should be greater or equal than the number of the types of characters requested"


  password = []
  if use_lower:
    password.append(random.choice(string.ascii_lowercase))
  if use_upper:
    password.append(random.choice(string.ascii_uppercase))
  if use_numbers:
    password.append(random.choice(string.digits))
  if use_special:
     password.append(random.choice(string.punctuation))

  for _ in range(length - len(password)):
     password.append(random.choice(all_chars))

  random.shuffle(password)
  return "".join(password)

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
            else:
              break
        except ValueError:
          print("Invalid input. Please enter a valid number.")
    while True:
        lower = input("Use lowercase letters? (yes/no): ").lower()
        if lower in ("yes", "no"):
           break
        else:
          print("Please answer 'yes' or 'no'")
    while True:
        upper = input("Use uppercase letters? (yes/no): ").lower()
        if upper in ("yes", "no"):
            break
        else:
          print("Please answer 'yes' or 'no'")
    while True:
        numbers = input("Use numbers? (yes/no): ").lower()
        if numbers in ("yes", "no"):
           break
        else:
           print("Please answer 'yes' or 'no'")

    while True:
      special = input("Use special characters? (yes/no): ").lower()
      if special in ("yes", "no"):
        break
      else:
        print("Please answer 'yes' or 'no'")

    return length, lower =="yes", upper =="yes", numbers =="yes", special == "yes"

def main():
    print("Welcome to the Password Generator!\n")
    length, use_lower, use_upper, use_numbers, use_special = get_user_input()
    password = generate_password(length, use_lower, use_upper, use_numbers, use_special)
    print("\nGenerated password: " + password)


if __name__ == "__main__":
    main()
