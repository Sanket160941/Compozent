# Function to check if a string is a palindrome
def is_palindrome(s: str) -> bool:

    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is the same as its reverse
    return normalized == normalized[::-1]

# Main function for user interaction
def main():
    print("Palindrome Checker")
    
    # Start an infinite loop for user interaction
    while True:
        # Get user input
        user_input = input("\nEnter a string to check if it is a palindrome: ").strip()
        
        # Check if the string is a palindrome
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")
        
        # Ask if the user wants to check another string
        another_check = input("\nDo you want to check another string? (yes/no): ").strip().lower()
        if another_check != 'yes':
            print("Bye !\n")
            break

# Check if the script is executed directly
if __name__ == "__main__":
    main()    # Call the main function to start the program