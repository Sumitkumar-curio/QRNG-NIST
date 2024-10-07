# Check the number of binary digits in the file
def count_binary_digits(binary_file):
    with open(binary_file, 'r') as file:
        content = file.read().strip()
        binary_length = len(content)
        print(f"Total number of binary digits: {binary_length}")

# Call the function with your binary file
count_binary_digits('binary_output2.txt')
