from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL Configuration
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='student_data'
)
cursor = conn.cursor()

# 1. Add a Student (POST)
@app.route('/students', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    gender = data['gender']  # Added missing gender variable
    age = data['age']
    department = data['department']
    backlogs = data['backlogs']
    credits_passed = data['credits_passed']

    cursor.execute("INSERT INTO students (name, email, gender, age, department, backlogs, credits_passed) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (name, email, gender, age, department, backlogs, credits_passed))
    conn.commit()
    return jsonify({"message": "User added successfully"}), 201

# 2. Get All Students (GET) with Optional Gender Filtering
@app.route('/students', methods=['GET'])
def get_users():
    gender = request.args.get('gender')  # Get gender from query parameters
    if gender:
        cursor.execute("SELECT * FROM students WHERE LOWER(gender) = LOWER(%s)", (gender,))
    else:
        cursor.execute("SELECT * FROM students")
    
    students = cursor.fetchall()
    return jsonify(students)

# 3. Get Student by ID (GET)
@app.route('/students/<int:id>', methods=['GET'])
def get_user(id):
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    if student:
        return jsonify(student)
    return jsonify({"message": "User not found"}), 404

# 4. Update Student (PUT)
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    name = data['name']
    email = data['email']
    gender = data['gender']
    age = data['age']
    department = data['department']
    backlogs = data['backlogs']
    credits_passed = data['credits_passed']

    cursor.execute("UPDATE students SET name=%s, email=%s, gender=%s, age=%s, department=%s, backlogs=%s, credits_passed=%s WHERE id=%s", 
                   (name, email, gender, age, department, backlogs, credits_passed, id))
    conn.commit()
    return jsonify({"message": "User updated successfully"})

# 5. Delete Student (DELETE)
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
