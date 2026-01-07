# Log Analysis with Regular Expressions (Python)

This project demonstrates how to use Python and Regular Expressions to parse system logs, process the data into structured formats (CSV), and visualize the results as HTML reports.

Project Structure
lab_exercise_1.py: Basic regex extraction techniques.

lab_exercise_2.py: Practice with dictionary sorting and the operator module.

ticky_check.py: The final automated script that generates error and user reports.

csv_to_html.py: A utility script to convert CSV data into viewable HTML tables.

## Exercise 2: Data Processing
In this section, I practiced sorting dictionary data using the operator module to prepare it for reporting.

Sorting by Key: Alphabetical ordering of data.

Sorting by Value: Ordering by frequency of occurrence.

Reversing: Using reverse=True to show the most frequent logs at the top.

## Exercise 3: System Log Analysis (ticky_check.py)
The main challenge was creating ticky_check.py, which performs the following:

Parsing: Iterates through syslog.log using regex to find INFO and ERROR patterns.

Counting: Tracks the number of specific error messages and per-user statistics.

Reporting: Exports the sorted data into error_message.csv and user_statistics.csv.

### Visualizations
After converting the generated CSV files to HTML using csv_to_html.py, the reports look like this:

### Error Message Ranking
Displays all error messages from most common to least common.

User Usage Statistics
Displays a list of all users and their total INFO and ERROR log counts.
