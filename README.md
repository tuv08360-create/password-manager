# password-manager
# Smart Password Manager

A modular Python-based password manager that checks password strength, generates secure passwords, enhances weak passwords, and securely stores them using encryption.

---

# Features

*  Password strength analysis (with feedback)
*  Fuzzy matching against common passwords
*  Strong password generator
*  Password strengthening from user input
*  Encrypted password storage (Fernet encryption)
*  Modular and scalable class-based design


# Tech Stack

* Python 3
* `re` (regex)
* `difflib` (fuzzy matching)
* `cryptography` (encryption)
* `json` (storage)



###  Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

2. Install required dependencies:

```bash
pip install cryptography
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

---

###  How to Run

```bash
python main.py
```



#How to Use

1. When you start the program, you will be asked for a **master key**

   * This is used to encrypt/decrypt stored passwords 

2. Choose from the menu:

* 1 → Check Password Strength

  * Enter any password
  * Get feedback
  * Option to save it securely

* 2 → Generate Password

  * Automatically creates a strong password
  * Option to save it

* 3 → Strengthen Your Password

  * Enter a simple password
  * Program enhances it
  * Option to save it

* 4 → View Stored Passwords

  * Decrypts and shows saved passwords using your master key



#Important Notes

* If you forget your **master key**, stored passwords cannot be recovered
* Passwords are encrypted using secure symmetric encryption
* Stored inside `vault.json`




open-source and free to use.

