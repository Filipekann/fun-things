import sqlite3

def analyze_match_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('match_data.db')
    cursor = conn.cursor()

    # Retrieve match data from the database
    cursor.execute("SELECT * FROM matches")
    match_data = cursor.fetchall()

    # Perform analysis on the match data
    for match in match_data:
        match_id, participant_names = match
        print(f"Match ID: {match_id}")
        print(f"Participants: {participant_names}")

        # Add your analysis code here
        # Example: Calculate performance metrics, identify patterns, suggest strategies, etc.

        print("")

    # Close the database connection
    conn.close()

# Example usage
analyze_match_data()
