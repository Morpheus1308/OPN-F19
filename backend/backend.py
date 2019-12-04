
import mysql.connector
import json
from flask import Flask, request           # import flask
app = Flask(__name__)             # create an app instance



def insert(firstname, lastname):
    cnx = mysql.connector.connect(user='root', password='password', database='crowd',
                              host='db', port='3306')
    cursor = cnx.cursor()
    cursor.execute("use crowd")

    insertperson = "insert into people(firstname, lastname) values('" + firstname + "', '" + lastname + "')"
    cursor.execute(insertperson)
    cnx.commit()
    cursor.close()
    cnx.close()
    return query_test()

def query_test():
    cnx = mysql.connector.connect(user='root', password='password',database='crowd',
                              host='db', port='3306')
    cursor = cnx.cursor()
    cursor.execute("SELECT personid AS 'PersonID', firstname AS 'Firstname', lastname AS 'Lastname' FROM people")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    cursor.close()
    cnx.close()
    return json.dumps(json_data)

@app.route("/person", methods=['POST'])                  
def hello():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    return "hello {}".format(insert(firstname, lastname))                  
    # return "text here, {}".format(query_test())        

@app.route("/persons", methods=['GET'])
def people():
    return query_test()

if __name__ == "__main__":        # on running python app.py
    app.run('0.0.0.0')
    #app.run(debug=True)