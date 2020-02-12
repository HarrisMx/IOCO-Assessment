import pymysql
import json


class Person():

    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self._query_execute = ""
        
        try:
            self.conn = pymysql.connect(user=self.user, password=self.password , host=self.host, db=self.database)
            self._query_execute = self.conn.cursor()
        except Exception as e:
            print("Error: ", e)

    def getAllPeople(self):
        try:
            query = "SELECT * FROM person"
            self._query_execute.execute(query)
            employees = ''
            employees = self._query_execute.fetchall()

        except Exception as e:
            print("Error: ", e)
        
        def updatePerson(self, id, data):
            try:
                query = "UPDATE people SET lastName={}, firstName={}, birthDtae = {}  WHERE personId={} ".format(data[0], data[1], data[2], id)
                test = self._query_execute.execute(query)
                if test:
                    return True
                else:
                    return False
            except Exception as e:
                print("Error: ", e)

    def setPerson(self, emp):
        try:
            query = "INSERT INTO people ('lastName','firstName','birthDate') VALUES({}, {}, {})".format(emp['surname'], emp['name'], emp['dob'])
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False

        except Exception as e:
            print("Error: ", e)

    def deletePerson(self, id):
        try:
            query = "DELETE FROM people WHERE personId = {}".format(id)
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False
        except Exception as e:
            print("Error: ", e)

    def getPersonById(self, id):
        try:
            query = "SELECT *  FROM people WHERE personId={}".format(id)
            self._query_execute.execute(query)
            user = ''
            user = self._query_execute.fetchall()
        except Exception as e:
            print("Error: ", e)

        return user


class EmployeeHandler(Person):

    def getAllEmployees(self):
        try:
            query = "SELECT * FROM employee"
            self._query_execute.execute(query)
            employees = ''
            employees = self._query_execute.fetchall()

        except Exception as e:
            print("Error: ", e)

        return employees

    def setEmployee(self, emp):
        try:
            query = "INSERT INTO employee ('EmployeeId','PersonId','EmployeeNum','EmploymentDate','TerminatedDate') VALUES({}, {}, {}, {})".format(emp['emp_id'], emp['emp_num'], emp['emp_date'], emp['terminated_date'])
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False

        except Exception as e:
            print("Error: ", e)

    def addEmployee(self, emp):
        try:
            query = "INSERT INTO employee ('EmployeeId','PersonId','EmployeeNum','EmploymentDate','TerminatedDate') VALUES({}, {}, {}, {})".format(emp['emp_id'], emp['emp_num'], emp['emp_date'], emp['terminated_date'])
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False

        except Exception as e:
            print("Error: ", e)

    def updateEmployee(self, id, data):
        try:
            query = "UPDATE employee SET EmployeeNum={}, EmploymentDate={}, TerminatedDate = {}  WHERE EmployeeId={} ".format(data[0], data[1], data[2], id)
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False
        except Exception as e:
            print("Error: ", e)

    def deleteEmployee(self, id):
        try:
            query = "DELETE FROM employee WHERE EmployeeId = {}".format(id)
            test = self._query_execute.execute(query)
            if test:
                return True
            else:
                return False
        except Exception as e:
            print("Error: ", e)

    def getEmployeeById(self, id):
        try:
            query = "SELECT EmployeeId,EmployeeNum,EmploymentDate,TerminatedDate  FROM employee WHERE EmployeeId={}".format(id)
            self._query_execute.execute(query)
            user = ''
            user = self._query_execute.fetchall()
        except Exception as e:
            print("Error: ", e)

    
