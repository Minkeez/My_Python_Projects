import random
import string
import os
from cryptography.fernet import Fernet

# 🔐 Generate or load encryption key
KEY_FILE = "secret.key"

def load_or_generate_key():
  """
  Load the encryption key from a file or generate a new one if not found.
  """
  if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as key_file:
      return key_file.read()
  else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
      key_file.write(key)
    return key
  
key = load_or_generate_key()
cipher = Fernet(key)

def generate_password(length=12, use_digits=True, use_special_chars=True):
  """
  Generate a random password with customizable options.

  Parameters:
    length(int): Length of the password.
    use_digit(bool): Include numbers.
    use_special_chars(bool): Include special characters.

  Returns:
    str: Randomly generated password.
  """
  characters = string.ascii_letters # Uppercase + Lowercase
  if use_digits:
    characters += string.digits
  if use_special_chars:
    characters += string.punctuation

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def generate_multiple_passwords(count=5, length=12, use_digits=True, use_special_chars=True):
  """
  Generate multiple random passwords.
  """
  return [generate_password(length, use_digits, use_special_chars) for _ in range(count)]

def generate_passphrase(words=4, separator="-"):
  """
  Generate a passphrase using random words.
  """
  word_list = ["apple", "banana", "carrot", "dragon", "elephant", "flame", "gold", "horizon", "iceberg", "jungle"]
  passphrase = separator.join(random.choice(word_list).capitalize() for _ in range(words))
  return passphrase

def check_password_strength(password):
  """
  Analyze the strength of a password.
  Returns: Weak, Medium, Strong
  """
  length_score = len(password) >= 12
  upper = any(c.isupper() for c in password)
  lower = any(c.islower() for c in password)
  digit = any(c.isdigit() for c in password)
  special = any(c in string.punctuation for c in password)

  score = sum([length_score, upper, lower, digit, special])

  if score == 5:
    return "🟢 Strong"
  elif score >= 3:
    return "🟡 Medium"
  else:
    return "🔴 Weak"

def save_encrypted_password(purpose, password, filename="passwords.txt"):
  """
  Save the encrypted password with its purpose to a file.
  """
  encrypted_password = cipher.encrypt(password.encode()).decode()
  with open(filename, "a") as file:
    file.write(f"{purpose}: {encrypted_password}\n")
  print(f"🔒 Encrypted Password for '{purpose}' saved to {filename}")

def decrypt_passwords(filename="passwords.txt"):
  """
  Decrypt and display saved passwords.
  """
  if not os.path.exists(filename):
    print("❌ No saved passwords found.")
    return
  
  with open(filename, "r") as file:
    lines = file.readlines()

  print("\n🔓 Decrypted Passwords:")
  for line in lines:
    try:
      purpose, encrypted_password = line.strip().split(": ")
      decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
      print(f"{purpose}: {decrypted_password}")
    except Exception as e:
      print(f"⚠️ Error decrypting {line.strip()} - {e}")

# Main Program
if __name__ == "__main__":
  print("🔒 Random Password Generator 🔒")

  try:
    mode = input("Do you want a (s)ingle or (m)ultiple passwords? ").strip().lower()

    if mode == 's':
      use_passphrase = input("🔢 Use random characters or 📝 passphrase? (r/p): ").strip().lower()

      if use_passphrase == "p":
        password = generate_passphrase()
      else:
        length = int(input("Enter password length: "))
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        while True:
          password = generate_password(length, use_digits, use_special_chars)
          print(f"\n✅ Your Generated Password: {password}")
          strength = check_password_strength(password)
          print(f"💪 Password Strength: {strength}")

          regenerate = input("🔄 Generate a new one? (y/n): ").strip().lower()
          if regenerate != 'y':
            break

      save_option = input("Do you want to save this password? (y/n): ").strip().lower()
      if save_option == 'y':
        purpose = input("What is this password for? (e.g., Facebook, Gmail): ").strip()
        save_encrypted_password(purpose, password)
    
    elif mode == 'm':
      count = int(input("How many passwords do you need? "))
      length = int(input("Enter password length: "))
      use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
      use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

      passwords = generate_multiple_passwords(count, length, use_digits, use_special_chars)

      print("\n✅ Your Generated Passwords:")
      for idx, pwd in enumerate(passwords, 1):
        strength = check_password_strength(pwd)
        print(f"{idx}. {pwd}")

      save_option = input("Do you want to save this password? (y/n): ").strip().lower()
      if save_option == 'y':
        for idx, pwd in enumerate(passwords, 1):
          purpose = input(f"What is this password {idx} for? ").strip()
          save_encrypted_password(purpose, pwd)
    
    else:
      print("❌ Invalid choice! Please enter 's' for single or 'm' for multiple.")

    # Decryption Option
    decrypt_option = input("\n🔓 Do you want to view saved passwords? (y/n): ").strip().lower()
    if decrypt_option == 'y':
      decrypt_passwords()
  except ValueError:
    print("❌ Invalid input! Please enter a valid number for length.")