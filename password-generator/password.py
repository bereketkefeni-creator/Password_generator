import random
import string

def generate_password(length, use_numbers, use_symbol, use_uppercase, use_lowercase):
    # 1. BUILD characters first
    characters = ""
    required = []

    if use_uppercase == "y":
        characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))

    if use_lowercase == "y":
        characters += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))

    if use_numbers == "y":
        characters += string.digits
        required.append(random.choice(string.digits))

    if use_symbol == "y":
        characters += string.punctuation
        required.append(random.choice(string.punctuation))

    # 2. THEN validate
    if characters == "":
        print("Error: select at least one character type")
        return None

    if length < len(required):
        print(f"Error: length must be at least {len(required)}")
        return None

    # 3. THEN generate
    remaining = random.choices(characters, k=length - len(required))
    password = required + remaining
    random.shuffle(password)
    return "".join(password)
def main():
    try:
        length = int(input("what is the lengthof password: "))
    except ValueError:
        print("Error: enter a number")
        return None
    use_numbers = input("include numbers (y/n)? ")
    use_symbols = input("include symbols(y/n)? ")
    use_uppercase = input("include uppercase? (y/n): ")
    use_lowercase = input("include lowercase? (y/n): ")
    
    password = generate_password(length, use_numbers, use_symbols,use_uppercase, use_lowercase)
    if password:
        print(password)

if __name__ == "__main__":
    main()