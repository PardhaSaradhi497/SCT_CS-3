import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):  # Uppercase
        strength += 1
    if re.search(r"[a-z]", password):  # Lowercase
        strength += 1
    if re.search(r"[0-9]", password):  # Digit
        strength += 1
    if re.search(r"[!@#$%^&*()?]", password):  # Special char
        strength += 1

    # Strength levels
    if strength == 5:
        remarks = "Very Strong 💪"
    elif strength == 4:
        remarks = "Strong ✅"
    elif strength == 3:
        remarks = "Moderate ⚠"
    elif strength == 2:
        remarks = "Weak ❌"
    else:
        remarks = "Very Weak ❌❌"

    return strength, remarks


# 🔹 MAIN PROGRAM STARTS HERE
password = input("Enter your password: ")
strength, remarks = check_password_strength(password)
print(f"\nPassword: {password}")
print(f"Strength Score: {strength}")
print(f"Remarks: {remarks}")
