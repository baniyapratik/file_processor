# File Processor
This python program is designed to identify the X records with the largest numeric values in a given input data.

## Prerequisites
Required to build and run the project:
- Python 3.x

## Set up the project

1. Clone the repository: git clone https://github.com/your_username/project_name.git
2. Navigate to the project directory: cd project_name
3. Install dependencies: pip install -r requirements.txt

## Setting up PYTHONPATH
Before running the program, ensure that the project directory is included in your `PYTHONPATH` environment variable. This allows Python to locate the modules and packages within the project.

You can set the `PYTHONPATH` variable using the following command in your terminal:

```bash
export PYTHONPATH=/path/to/your/project/directory:$PYTHONPATH
````

For additional help and options, you can use the -h or --help flag:
```commandline
python main.py -h
```
## Usage

### To run the script with input from a file:
```commandline
python main.py --file_path /path/to/your/file.txt --x 5
```

### To run the script with interactive input:

# Technical Specification

## Functional Requirement
### Input Handling
The program should accept a file path containing data i.e. one file path. Example: --file_path=<file_path>. It is an optional field.
It should accept an integer that specifies the number of recorders records with the largest numeric values to be identified. 
If it is not an integer it should raise an exception. Example: --x=2
### File Reading
The program should be able to read data from the specific file path or standard input if no file path is provided.
### Unique Record IDs
The program should ensure that each record identifier is unique within the data. It should report errors and raise and exception when duplicate record identifier is seen.
### Data Validation
The program should validate the format of each line in the input data. Each line should consist of two parts separated by a single space: a unique record identifier and a numeric value. It should report errors for lines with incorrect format.
### Identify largest values
The program should identify the X records with the largest numeric values in the data.
Processing data
The program should process the data line by line, extracting the record identifier and the numeric value from each line.
### Output
The program should print unique record identifiers associated with the X largest numeric values. The order of the output does not matter.

## Non-functional Requirement
### Performance
The program should be able to process large files efficiently, minimizing processing time and memory usage.
### Error Handling
The program should gracefully handle errors and provide informative error messages to the user. Some  errors are:
- Invalid file paths
- Invalid data formats
- Duplicate record identifiers
### Testability
The program should be well-structured and modular to facilitate unit testing and ensure its functionality.
Logging(Optional)
The program should log information about the processing, such as number of lines processed, errors encountered, and execution time. This can be useful for debugging and monitoring purposes.

