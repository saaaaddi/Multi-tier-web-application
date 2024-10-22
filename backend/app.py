from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask Backend!")

@app.route('/db')
def db_example():
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="db", port="5432", database="postgres")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        return jsonify(message=f"Connected to DB: {record}")
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
