import argparse
import os

from logger.logger import LogFactory
from utils.file_processor import process_input_from_file, process_input_from_user

logger = LogFactory('Main')


def positive_integer(value):
    """Check if the value is a positive integer."""
    val = int(value)
    if val <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer greater than or "
                                         f"equal to 1")
    return val


def get_input():
    """Prompts the user to input two integers separated by space and validates the input."""
    input_list = []
    while True:
        logger.info("Please provide two integers separated by space, or type 'process' to proceed:")
        user_input = input()
        if user_input.lower() == 'process':
            break

        input_values = user_input.split()
        if len(input_values) != 2:
            print("Error: Please provide exactly two integers separated by space.")
            continue
        try:
            x, y = map(int, input_values)
            input_list.append((x, y))
            logger.info("Input added.")
        except ValueError:
            logger.error("Error: Please provide valid integers.")
            continue

    return input_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find IDs with X largest values.")
    parser.add_argument("--file_path", type=str, help="Path to the file containing data. It is "
                                                      "optional.")
    parser.add_argument("--x", type=positive_integer,
                        help="Number of records with largest values. It should be a positive "
                             "integer greater than or equal to 1.")
    args = parser.parse_args()

    # if file_path is provided
    if args.file_path:
        # check if the file exists
        if not os.path.exists(args.file_path):
            msg = f"Error: File not found: {args.file_path}"
            logger.error(msg)
            raise FileNotFoundError(msg)
        process_input_from_file(args.file_path, args.x)
    else:
        user_input_list = get_input()
        logger.info("Would you like to process the input? (yes/no)")
        process_option = input().lower()
        if process_option == 'yes':
            process_input_from_user(user_input_list, args.x)
        else:
            logger.warning("Input discarded.")
