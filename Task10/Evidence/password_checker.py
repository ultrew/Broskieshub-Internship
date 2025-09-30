import re

def check_password_strength(password):
    """
    Analyzes the strength of a password based on a set of rules.

    Args:
        password (str): The password to analyze.

    Returns: 
        A tuple containing the strength level (str) and a list of feedback
        suggestions (list).
    """
    score = 0
    feedback = []

    # Rule 1 & 2: Password Length (Score 0-2)
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    # Rule 3: Uppercase Letters (Score +1)
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (e.g., A-Z).")

    # Rule 4: Lowercase Letters (Score +1)
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (e.g., a-z).")

    # Rule 5: Numbers (Score +1)
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (e.g., 0-9).")

    # Rule 6: Special Characters (Score +1)
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # Determine strength level based on the final score
    if score <= 2:
        strength_level = "Very Weak"
    elif score == 3:
        strength_level = "Weak"
    elif score == 4:
        strength_level = "Moderate"
    elif score == 5:
        strength_level = "Strong"
    else: # score == 6
        strength_level = "Very Strong"

    return strength_level, feedback

def main():
    """
    Main function to run the password strength checker tool.
    """
    print("--- Password Strength Checker ---")
    print("Enter a password to check its strength, or type 'exit' to quit.")

    while True:
        password = input("\nPlease enter a password: ")

        if password.lower() == 'exit':
            print("Exiting the tool. Stay safe!")
            break

        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        strength, suggestions = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")

        if suggestions:
            print("\nSuggestions for improvement:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

if __name__ == "__main__":
    main()
