import csv

# File paths
input_file = 'C2.csv'  # Your input CSV file with QRNG output
binary_output_file = 'binary_output2.txt'  # Binary file for NIST test

# Open the input CSV file
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    
    # Read the header
    header = next(reader)
    channel_1_index = header.index("Channel 1 - Counts per bin")

    # Open the output binary file
    with open(binary_output_file, 'w') as outfile:
        for row in reader:
            channel_1_value = int(row[channel_1_index])
            # Convert to binary: if non-zero, it's 1; otherwise, 0
            binary_value = '1' if channel_1_value != 0 else '0'
            outfile.write(binary_value)  # Write the binary value directly

print(f"Binary data successfully written to {binary_output_file}")
