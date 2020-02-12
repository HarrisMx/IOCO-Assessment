from flask import Flask, jsonify, escape, request
from database import EmployeeHandler
db = EmployeeHandler('mxolisi', 'Mx@lisi7', '160.153.133.158', 'employee')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome'})


@app.route('/Employees', methods=['GET'])
def getAllEmployees():
    try:
        employees = db.getAllEmployees()
        json_data = []
        json_data = jsonify(employees)
        return {'message': 'Success', 'Employees': json_data}, 200
    except Exception as error:
        return {'message': '%s' % (error)}, 404


@app.route('/Employees', methods=['POST'])
def setEmployee():
    employees = {}
    try:
        emp = {"emp_id": request.json['emp_id'], "emp_num": request.json['emp_num'], "emp_date" : request.json['emp_date'], "terminated_date": request.json['terminated_date']}
        employees = db.addEmployee(emp)
        
        return {'message': ' New Employee Added'}, 200
    except Exception as error:
        return {'message': '%s' % (error)}, 404

    
@app.route('/Employees/<int:id>', methods=['GET'])
def getEmployeeByID(id):
    try:
        _employee = db.getEmployeeById(id)
        employee = {}
        employee = {"EmployeeId": _employee[0][0], "EmployeeNum": _employee[0][1], "EmployeeDate" : _employee[0][2], "TerminatedDate": _employee[0][3]}

        return {'message': 'Success', 'employee': employee}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


@app.route('/Employees/<int:id>', methods=['PUT'])
def updateEmployeeData(id):
    try:
        _employee = db.updateEmployee(id)
        employee = {}
        employee = {"EmployeeId": _employee[0][0], "EmployeeNum": _employee[0][1], "EmployeeDate" : _employee[0][2], "TerminatedDate": _employee[0][3]}

        return {'message': 'Success', 'employee': employee}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


@app.route('/Employees/<int:id>', methods=['DELETE'])
def deleteEmployeeData(id):
    try:
        _employee = db.deleteEmployee(id)
        employee = {}
        employee = {"EmployeeId": _employee[0][0], "EmployeeNum": _employee[0][1], "EmployeeDate" : _employee[0][2], "TerminatedDate": _employee[0][3]}

        return {'message': 'Success', 'employee': employee}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


'''
People API Code Starts Here
'''


@app.route('/People', methods=['GET'])
def getAllPeople():
    try:
        persons = db.getAllPeople()
        json_data = []
        json_data = jsonify(persons)
        return {'message': 'Success', 'People': json_data}, 200
    except Exception as error:
        return {'message': '%s' % (error)}, 404


@app.route('/People', methods=['POST'])
def setPerson():
    persons = {}
    try:
        emp = {'lasName': request.json['surname'], "firstName": request.json['name'], "birthDate" : request.json['dob']}
        persons = db.addperson(emp)
        
        return {'message': ' New Person Added'}, 200
    except Exception as error:
        return {'message': '%s' % (error)}, 404

    
@app.route('/People/<int:id>', methods=['GET'])
def getPersonByID(id):
    try:
        _person = db.getPersonById(id)
        person = {}
        person = {"surname": _person[0][0], "name": _person[0][1], "dob" : _person[0][2]}

        return {'message': 'Success', 'person': person}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


@app.route('/People/<int:id>', methods=['PUT'])
def updatePersonData(id):
    try:
        _person = db.updateperson(id)
        person = {}
        person = {"surname": _person[0][0], "name": _person[0][1], "dob" : _person[0][2]}

        return {'message': 'Success', 'person': person}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


@app.route('/People/<int:id>', methods=['DELETE'])
def deletePersonData(id):
    try:
        _person = db.deletePerson(id)
        person = {}
        person = {"surname": _person[0][0], "name": _person[0][1], "dob" : _person[0][2]}

        return {'message': 'Success', 'person': person}, 200
    
    except Exception as error:
        return {'message': '%s' % (error)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8081)
