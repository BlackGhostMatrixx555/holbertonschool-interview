#!/usr/bin/python3
"""Script that reads stdin line by line and computes log metrics."""
import sys
import re


def print_stats(total_size, status_counts):
    """Print current file size and status code counts.

    Args:
        total_size (int): the total file size accumulated.
        status_counts (dict): counts per status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0
    pattern = re.compile(
        r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            match = pattern.match(line)
            if match:
                status = int(match.group(1))
                size = int(match.group(2))
                total_size += size
                if status in valid_codes:
                    status_counts[status] = status_counts.get(status, 0) + 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
        print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
