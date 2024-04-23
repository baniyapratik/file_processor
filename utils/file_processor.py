import heapq

from exceptions.exceptions import DuplicateRecordIdentifier
from logger.logger import LogFactory
from utils.utils import measure_time
logger = LogFactory('File Processor')

CHUNK_SIZE = 1024


def generate_large_file(file_path, num_lines):
    """Generate a large test file"""
    try:
        with open(file_path, 'w') as f:
            for i in range(num_lines):
                f.write(f"Record_{i} {i}\n")
    except (IOError, OSError) as e:
        logger.error(f"Error: Failed to generate file: {file_path}. Reason: {e}")


def is_valid_line(line):
    """Checks if a line is in the expected format."""
    parts = line.strip().split(" ", 1)
    if len(parts) != 2:
        return False
    try:
        int(parts[1])
    except ValueError:
        return False
    return True


@measure_time
def process_input_from_user(input_list, x):
    """
    Prompts the user for input and outputs IDs with X the largest values.

    Args:
      input_list: List of
      x: Number of records with the largest values to output.

    Time Complexity: O(n log(k)), where n is the length of the lines and k is value of x. Space
    Complexity: O(k), k is value of x, o(distinct_ids) for last_seen_ids which is bounded by the
    number of lines n.
    """
    last_seen_ids = set()
    result = process_input(input_list, x, last_seen_ids)
    result = [res[0] for res in result]
    logger.info(f"IDs with largest values: {result}")
    return result


@measure_time
def process_input_from_file(file_path, x):
    """
    Reads the file and outputs IDs with X the largest values.

    Args:
      file_path: Absolute path to the file.
      x: Number of records with the largest values to output.

    Time Complexity: O(n log(k)), where n is the length of the lines and k is value of x.
    Space Complexity: O(k), k is value of x, o(distinct_ids) for last_seen_ids which is bounded by the
    number of lines n.
    """
    last_seen_ids = set()
    min_heap = []

    with open(file_path, 'r') as f:
        while True:
            # Read a chunk of lines from the file
            lines = f.readlines(CHUNK_SIZE)

            # If no more lines are read, break the loop
            if not lines:
                break

            # Process the lines in the chunk
            result = process_input(lines, x, last_seen_ids)

            for record_id, value in result:
                if len(min_heap) < x:
                    heapq.heappush(min_heap, (value, record_id))
                elif value > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (value, record_id))

    result = [heapq.heappop(min_heap)[1] for _ in range(min(len(min_heap), x))]
    logger.success(f"IDs with largest values: {result}")
    return result


def process_input(lines_or_input_list, x, last_seen_ids):
    """
    Processes the input and outputs IDs with X the largest values.

    Args:
      lines_or_input_list: Iterable containing lines from the file or user input list.
      x: Number of records with the largest values to output.
      last_seen_ids: Set containing record IDs encountered so far.

    Time Complexity: O(n log(k)), where n is the length of the lines and k is value of x.
    Space Complexity: O(k), k is value of x, o(distinct_ids) for last_seen_ids which is bounded by the
    number of lines n.
    """
    min_heap = []
    for line_or_tuple in lines_or_input_list:
        # if reading from the file
        if isinstance(line_or_tuple, str):
            if not is_valid_line(line_or_tuple):
                logger.error(f"Error: Invalid line format: {line_or_tuple.strip()}")
                continue

            record_id, value = line_or_tuple.strip().split(" ", 1)
            value = int(value)
        # if tuple from user input
        else:
            record_id, value = line_or_tuple

        if record_id in last_seen_ids:
            msg = f"Error: Duplicate record ID: {record_id}"
            logger.error(msg)
            raise DuplicateRecordIdentifier(msg)

        if len(min_heap) < x:
            heapq.heappush(min_heap, (value, record_id))
        elif value > min_heap[0][0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (value, record_id))

        last_seen_ids.add(record_id)

    result = [(record_id, value) for value, record_id in min_heap]
    return result
