import csv

# Input and output file paths
input_file = "input.csv"  # Replace with your file path
output_file = "output.txt"

# Process the input file and write to the output file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    reader = csv.DictReader(infile)
    outfile.write("{\n")
    for row in reader:
        record_id = row["id"]
        designer = row["designer"]
        organization = row["organization"]
        formatted_line = f'    "{record_id}" => ["designer" => "{designer}", "organization" => "{organization}"],\n'
        outfile.write(formatted_line)
    outfile.write("}\n")

print(f"Formatted output written to {output_file}")
