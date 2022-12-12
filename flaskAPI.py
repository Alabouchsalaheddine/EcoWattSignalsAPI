from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello ecoWatt!"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route("/getAllDaysValues")
def getAllDaysValues():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ecowatt"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "select day, dvalue from ecowattdaysignals order by day")
    myresult = mycursor.fetchall()
    myresultList = list(myresult)

    data = []

    for thisLine in myresultList:
        day = {"day" : thisLine[0].strftime("%Y-%m-%d") , "dvalue" : thisLine[1]}
        data.append(day)
    result = {}
    result['data'] = data

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')