from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "student_id": 101, "company_name": "CompanyA", "start_date": "2022-01-01", "end_date": "2022-06-30"}
]

# GET /students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET /students/{id}
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['student_id'] == student_id), None)
    if student is not None:
        return jsonify(student)
    return jsonify({"error": "Студент не знайдений"}), 404


# POST /students
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    print("Updated students:", students)
    return jsonify(new_student), 201


# PUT /students/{id}
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['student_id'] == student_id), None)
    if student is not None:
        updated_data = request.get_json()
        student.update(updated_data)
        return jsonify(student)
    return jsonify({"error": "Студент не знайдений"}), 404

# DELETE /students/{id}
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['student_id'] != student_id]
    return jsonify({"message": "Студент видалений успішно"}), 200

if __name__ == '__main__':
    app.run(debug=True)
