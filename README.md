# Log Analysis with Regular Expressions (Python)

This mini project parses a `syslog.log` file and generates two CSV reports:
- `error_message.csv` — most common ERROR messages (sorted by count, descending)
- `user_statistics.csv` — per-user INFO/ERROR counts (sorted by username)

## What I practiced
- Regular expressions (`re`) to match INFO/ERROR log formats
- Dictionaries to count occurrences
- Sorting results for reporting
- Writing CSV output using Python’s `csv` module

## Input format (example)
Jan 31 00:21:30 ubuntu.local ticky: INFO Closed ticket [#01754] (noel)
Jan 31 00:21:30 ubuntu.local ticky: ERROR Connection to DB failed (noel)
