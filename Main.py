def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        content = file.read()

    # Split content based on the delimiter #
    sections = content.split('#')

    # Strip whitespace and split each section into lines
    sections = [section.strip().split('\n') for section in sections]

    # Find the maximum number of lines in the sections
    max_lines = max(len(section) for section in sections)

    # Pad shorter sections with empty strings to match the length of the longest section
    padded_sections = [section + [''] * (max_lines - len(section)) for section in sections]

    # Combine lines from each section into columns
    combined_lines = [
        '|'.join(column)
        for column in zip(*padded_sections)
    ]

    # Write the combined lines to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write('\n'.join(combined_lines))

# Usage
input_filename = 'file.txt'
output_filename = 'output.txt'
process_file(input_filename, output_filename)
