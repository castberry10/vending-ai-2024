import random

def split_file(input_file, output_file1, output_file2, split_ratio=0.6):
    # Read the contents of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Shuffle the lines to randomize
    random.shuffle(lines)

    # Calculate the split index
    split_index = int(len(lines) * split_ratio)

    # Split the lines into two parts
    part1 = lines[:split_index]
    part2 = lines[split_index:]

    # Write the first part to the first output file
    with open(output_file1, 'w', encoding='utf-8') as file:
        file.writelines(part1)

    # Write the second part to the second output file
    with open(output_file2, 'w', encoding='utf-8') as file:
        file.writelines(part2)

# Example usage
input_file = '/home/aicompetition28/oc_rgb_rand/target.txt'
output_file1 = '/home/aicompetition28/output6.txt'
output_file2 = '/home/aicompetition28/output4.txt'
split_file(input_file, output_file1, output_file2)

