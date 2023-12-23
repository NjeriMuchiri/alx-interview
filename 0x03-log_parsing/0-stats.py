#!/usr/bin/python3
"""file stat method"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            # Split the line into components
            parts = line.split()
            if len(parts) >= 8:
                ip, _, _, _, _, status_code, file_size = parts[:7]

                # Check if status_code is a valid integer
                try:
                    status_code = int(status_code)
                except ValueError:
                    continue

                # Update metrics
                total_size += int(file_size)
                status_counts[status_code] += 1

                lines_processed += 1

                # Print statistics every 10 lines
                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
