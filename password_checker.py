import re
import hashlib

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add at least one digit")

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        remarks.append("Add at least one special character")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, remarks


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def cracking_simulation(password):
    common_passwords = ["123456", "password", "admin", "welcome", "qwerty"]

    if password in common_passwords:
        return "Password cracked using dictionary attack!"
    else:
        return "Password not found in dictionary (safe from basic attack)"


if __name__ == "__main__":
    print("🔐 Password Strength Checker & Cracking Simulator")

    user_password = input("Enter password: ")

    strength, suggestions = check_password_strength(user_password)
    hashed = hash_password(user_password)
    crack_result = cracking_simulation(user_password)

    print("\nPassword Strength:", strength)
    print("Hashed Password (SHA-256):", hashed)
    print("Cracking Simulation Result:", crack_result)

    if suggestions:
        print("\nSuggestions to improve password:")
        for s in suggestions:
            print("-", s)
