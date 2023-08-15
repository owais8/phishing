from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api/phishing_details', methods=['GET'])
def get_phishing_details():
    try:
        # MySQL connection parameters
        db_params = {
            'host': 'localhost',     # Usually 'localhost' if the database is on the same machine
            'user': 'root',
            'password': '1234',
            'database': 'phishing',
            'port': '3306',     # Typically 3306 for MySQL
        }

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_params)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SELECT query to get all details from the phishing_details table
        select_query = "SELECT * FROM phishing_details"
        cursor.execute(select_query)

        # Fetch all rows
        result = cursor.fetchall()

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # Convert the result to a list of dictionaries
        phishing_details = []
        for row in result:
            detail = {
                'label': row[0],
                'url': row[1],
            }
            phishing_details.append(detail)

        return jsonify(phishing_details)

    except Exception as e:
        return jsonify({'error': 'Failed to fetch data from the database', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
