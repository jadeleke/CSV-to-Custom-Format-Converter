# CSV-to-Custom-Format-Converter

This Python script converts a CSV file with columns `id`, `designer`, and `organization` into a structured key-value pair format for easy usage. It outputs the formatted data to a text file.  

## Features  
- Processes a CSV file with headers: `id`, `designer`, and `organization`.  
- Outputs data in the following format: 


  ```plaintext
  {
      "ID_000001" => ["designer" => "John Doe", "organization" => "Org1 Inc."],
      "ID_000002" => ["designer" => "Jane Smith", "organization" => "Another Org."],
  }
Ensures data is anonymized and ready for structured use cases.


Requirements
Python 3.x


Installation
Clone the repository or download the script.
Ensure Python 3.x is installed on your machine.


Usage
Prepare your input CSV file with the following structure:

id,designer,organization
ID_000001,John Doe,Org1 Inc.
ID_000002,Jane Smith,Another Org.
Update the input_file variable in the script with the path to your CSV file.


Run the script:

python converter.py
The formatted output will be saved to output.txt in the same directory as the script.

Example Output
The output file (output.txt) will contain:

{
    "ID_000001" => ["designer" => "John Doe", "organization" => "Org1 Inc."],
    "ID_000002" => ["designer" => "Jane Smith", "organization" => "Another Org."],
}

Contribution
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!