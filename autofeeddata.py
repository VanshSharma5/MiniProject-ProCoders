import sqlite3
import re
from sys import exit

# Function to parse the question data
def parse_question_data(file_path):
    questions = []
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into individual questions based on a number and period
    question_blocks = re.split(r'\n\d+\. ', content)
    for block in question_blocks:  # Skip the first split as it's empty
        try:
            # Extract question text
            question_match = re.search(r'^(.*?)(?=\n[a-d]\))', block, re.DOTALL)
            if not question_match:
                print(f"Skipping block due to missing question text: {block[:50]}...")
                continue

            question_text = question_match.group(1).strip()

            # Extract options
            options = re.findall(r'([a-d]\)) (.*?)(?=\n[a-d]\)|(?=\nAnswer:))', block, re.DOTALL)
            if len(options) != 4:
                print(f"Skipping block due to incomplete options: {block[:50]}...")
                continue

            options_dict = {key: value.strip() for key, value in options}

            # Extract answer and explanation
            answer_match = re.search(r'Answer: ([a-d])\)', block)
            explanation_match = re.search(r'Explanation: (.*)', block, re.DOTALL)

            if not answer_match or not explanation_match:
                print(f"Skipping block due to missing answer/explanation: {block[:50]}...")
                continue

            answer = answer_match.group(1)
            explanation = explanation_match.group(1).strip()

            # Map answer (a-d) to numeric value (1-4)
            answer_num = ord(answer) - ord('a') + 1

            questions.append((question_text,options_dict['a)'],options_dict['b)'],options_dict['c)'],options_dict['d)'],answer_num,explanation))
        except Exception as e:
            print(f"Error parsing block: {block[:50]}...\nError: {e}")
    return questions

# Function to create SQLite3 database and table
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    """cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            answer INTEGER,
            explanation TEXT
        )
    ''')
    conn.commit()"""
    return conn

# Function to insert data into SQLite3 database
def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO ProCoders_quiz (question, option1, option2, option3, option4, answer, explanation, language_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, 6)
    ''', data)
    conn.commit()

# Main function
def main():
    file_path = "c++.txt"  # Input file containing questions
    db_name = "db.sqlite3"     # SQLite3 database file

    # Parse the question data
    questions = parse_question_data(file_path)

    # Create the database and table
    conn = create_database(db_name)

    # Insert the parsed data into the database
    insert_data(conn, questions)

    # Close the database connection
    conn.close()
    print(f"Inserted {len(questions)} questions into the database.")

if __name__ == "__main__":
    main()
