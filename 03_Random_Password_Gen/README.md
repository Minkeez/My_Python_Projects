# Random Password Generator

A **Secure and customizable** random password generator written in **Python**, This program allows users to generate **strong passwords** or **passphrases**, save them securely with **encryption**, and decrypt them when needed.

---

### Features
-  **Random Password Generator** – Generates secure passwords with customizable length and complexity.  
-  **Passphrase Generator** – Creates easy-to-remember passphrases using random words.  
-  **Password Strength Checker** – Labels passwords as **Weak, Medium, or Strong**.  
-  **Encrypted Password Storage** – Uses **Fernet encryption** to save passwords securely.  
-  **Decryption Function** – Allows users to retrieve and view saved passwords.  
-  **Regenerate Password Option** – Users can generate a new password if unsatisfied.  

---

### Installation
1. **Clone this repository**:
  ```
  bash
  git clone https://github.com/Minkeez/My_Python_Projects.git
  cd My_Python_Projects/RandomPasswordGenerator
  ```
2. **Install required dependencies**
  ```
  pip install cryptography
  ```

---

### Usage
Run the script:
```
python main.py
```
The program will ask:
1. **Do you want a single or multiple passwords?**
2. **Random character password or passphrase?**
3. **Include numbers and special characters?**
4. **Save the password? (Yes/No)**
5. **If saved, specify the purpose (e.g., "Facebook")**
6. **Optionally, decrypt and view saved passwords.**

---

### Example Output
```
🔒 Random Password Generator 🔒

Do you want a (s)ingle or (m)ultiple passwords? s
🔢 Use random characters or 📝 passphrase? (r/p): r
Enter password length: 16
Include numbers? (y/n): y
Include special characters? (y/n): y

✅ Generated Password: L#e@q6Xt9J&!sPzF
💪 Password Strength: 🟢 Strong

🔄 Generate a new one? (y/n): n
Do you want to save this password? (y/n): y
What is this password for? (e.g., Facebook, Gmail): Facebook
🔒 Encrypted Password for 'Facebook' saved to passwords.txt

🔓 Do you want to view saved passwords? (y/n): y

🔓 Decrypted Passwords:
Facebook: L#e@q6Xt9J&!sPzF
```

---

### How Passwords Are Stored Securely
- **Encryption**: Used `cryptography.Fernet` to encrypt stored passwords.
- **Decryption**: Users can decrypt stored passwords when needed.
- **Key Management**: **A secret key file** (`secret.key`) is generated for encryption and must be kept safe.

---

### Future Enhancements
- **Add GUI** - A Tkinter-based interface for easy interaction.
- **Generate QR Codes** - Store passwords as QR codes for easy retrieval
- **Categorized Paswords** - Store passwords under different categories (e.g., Work, Social, Banking).
- **Bulk Export & Import** - Save and load passwords in JSON or CSV format.