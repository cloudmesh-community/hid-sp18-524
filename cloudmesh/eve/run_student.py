from eve import Eve
from student import Student
import platform
import psutil
import json
from flask import Response
import getpass

app = Eve()

@app.route('/student/albert', methods=['GET'])
def processor():
    student = Student("Albert", "Zweistein", "Indiana University", "albert@example.edu")

    response = Response()
    response.headers["Content-Type"] = "application/json;charset=utf-8"

    try:
        student.setUsername(getpass.getuser())
        response.headers["status"] = 200
    except:
        response.headers["status"] = 500

    response.data = json.dumps(student.get())
    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
