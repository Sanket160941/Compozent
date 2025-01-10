# Define the input and output file names
input_file = r"Python\File_Handling\reading.txt"
output_file = r"Python\File_Handling\result.txt"

# Function to count words in a file
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    
    # Handle the case where the file does not exist
    except FileNotFoundError:    
        print(f"Error: The file '{file_path}' does not exist.")
        return None

# Count the words in the input file
word_count = count_words(input_file)

# Write the word count to the output file if successful
if word_count is not None:    
    
    # Proceed only if word count is valid
    try:
        with open(output_file, 'w') as file:
            file.write(f"The number of words in '{input_file}' is: {word_count}")
        print(f"Word count written to '{output_file}'.")
    
    # Handle any errors during file writing
    except Exception as e:    
        print(f"Error writing to '{output_file}': {e}")