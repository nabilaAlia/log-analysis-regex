#!/usr/bin/env python3

import re
import csv
import operator

# 1. Initialize dictionaries
# error: counts how many times each specific error message occurs
# per_user: tracks {username: {"INFO": count, "ERROR": count}}
error = {}
per_user = {}

# 2. Process the log file
with open('syslog.log', 'r') as f:
    for line in f:
        # Regex to capture the log type, the message, and the username in brackets
        # Example line: Jan 31 16:16:53 ubuntu.local ticky: ERROR Ticket doesn't exist (blossom)
        match = re.search(r"ticky: (INFO|ERROR) ([\w ']+) \(([\w.]+)\)", line)
        if not match:
            continue

        log_type = match.group(1)
        message = match.group(2)
        username = match.group(3)

        # Initialize user in dictionary if not already present
        if username not in per_user:
            per_user[username] = {"INFO": 0, "ERROR": 0}

        # Count INFO or ERROR for the user
        if log_type == "INFO":
            per_user[username]["INFO"] += 1
        elif log_type == "ERROR":
            per_user[username]["ERROR"] += 1
            # Also count the specific error message type
            error[message] = error.get(message, 0) + 1

# 3. Sort the data
# Sort errors by frequency (most to least)
sorted_errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

# Sort users alphabetically by username
sorted_users = sorted(per_user.items(), key=operator.itemgetter(0))

# 4. Prepare data for CSV (insert headers at index 0)
sorted_errors.insert(0, ("Error", "Count"))

# For users, we flatten the nested dictionary into a tuple for the CSV
user_report = [("Username", "INFO", "ERROR")]
for user, counts in sorted_users:
    user_report.append((user, counts["INFO"], counts["ERROR"]))

# 5. Write to CSV files
with open('error_message.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sorted_errors)

with open('user_statistics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(user_report)
