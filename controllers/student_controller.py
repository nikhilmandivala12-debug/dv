students = []


# Add a student
def create_student(student):
    students.append(student)
    return student


# Get all students
def get_all_students():
    return students


# Find a student by ID
def get_student_by_id(student_id):
    for student in students:
        if student.id == student_id:
            return student

    return None


# Update a student
def update_student(student_id, student_data):
    for student in students:
        if student.id == student_id:
            student.name = student_data.name
            student.email = student_data.email
            student.course = student_data.course
            student.semester = student_data.semester

            return student

    return None


# Delete a student
def delete_student(student_id):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return True

    return False