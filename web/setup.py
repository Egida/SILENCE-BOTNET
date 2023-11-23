import flask, pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

mydv = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="silence"
)

app.run(host="localhost", port=8080)