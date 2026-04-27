import re
import random
import string
import json
from difflib import SequenceMatcher
from cryptography.fernet import Fernet
import base64
import hashlib


class PasswordManager:
    def __init__(self, key=None):
        self.common_passwords = self.load_common_passwords()
        self.key = self.generate_key(key) if key else None
        self.cipher = Fernet(self.key) if self.key else None

    # ---------------- ATOMIC METHODS ---------------- #

    def has_uppercase(self, password):
        return bool(re.search(r"[A-Z]", password))

    def has_lowercase(self, password):
        return bool(re.search(r"[a-z]", password))

    def has_digit(self, password):
        return bool(re.search(r"\d", password))

    def has_special(self, password):
        return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    def is_long_enough(self, password):
        return len(password) >= 8

    def has_repetition(self, password):
        return bool(re.search(r"(.)\1\1", password))

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    # ---------------- CORE FEATURES ---------------- #

    def load_common_passwords(self):
        return [
            "password", "123456", "123456789", "qwerty", "abc123",
            "password123", "111111", "123123", "admin", "letmein",
            "welcome", "iloveyou", "monkey", "dragon", "sunshine"
        ]

    def is_common_password(self, password):
        return password.lower() in self.common_passwords

    def is_similar_to_common(self, password, threshold=0.7):
        for common in self.common_passwords:
            if self.similarity(password.lower(), common) > threshold:
                return True
        return False

    def check_strength(self, password):
        score = 0
        feedback = []

        if self.is_long_enough(password):
            score += 1
        else:
            feedback.append("Password too short.")

        if self.has_uppercase(password):
            score += 1
        else:
            feedback.append("Add uppercase letters.")

        if self.has_lowercase(password):
            score += 1
        else:
            feedback.append("Add lowercase letters.")

        if self.has_digit(password):
            score += 1
        else:
            feedback.append("Add numbers.")

        if self.has_special(password):
            score += 1
        else:
            feedback.append("Add special characters.")

        if self.has_repetition(password):
            feedback.append("Avoid repeated characters.")

        if self.is_common_password(password):
            score = 0
            feedback.append("Very common password!")

        if self.is_similar_to_common(password):
            feedback.append("Too similar to common passwords.")

        strength = ["Weak", "Medium", "Strong"][min(score // 2, 2)]
        return strength, feedback

    # ---------------- PASSWORD GENERATION ---------------- #

    def generate_password(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(chars) for _ in range(length))

    def strengthen_password(self, base):
        additions = [
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        return base + "".join(additions)

    # ---------------- ENCRYPTION ---------------- #

    def generate_key(self, password):
        key = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(key)

    def encrypt(self, text):
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt(self, text):
        return self.cipher.decrypt(text.encode()).decode()

    def save_password(self, password, filename="vault.json"):
        encrypted = self.encrypt(password)

        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(encrypted)

        with open(filename, "w") as f:
            json.dump(data, f)

    def load_passwords(self, filename="vault.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            return [self.decrypt(p) for p in data]
        except:
            return []
