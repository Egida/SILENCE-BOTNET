import flask, pymysql, os, requests
from dotenv import load_dotenv

load_dotenv("config.env")

app = flask.Flask(__name__)
app.config["DEBUG"] = False

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

mydv = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

@app.route('/silence', methods=['GET'])
def silence():
    return flask.render_template('index.html')

@app.route('/ip-tracker', methods=['GET'])
def ip_tracker():
    if flask.request.method == 'GET':
        username = flask.request.args.get('username')
        
        r = requests.get('https://api.ipify.org').text
        
        cursor = mydv.cursor()
        sql = "SELECT * FROM ip_tracker WHERE username=%s"
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        

        if row is None:
            sql = "INSERT INTO ip_tracker (username, ip_address) VALUES (%s, %s)"
            val = (username, r)
            cursor.execute(sql, val)
            mydv.commit()
        else:
            sql = "UPDATE ip_tracker SET ip_address=%s WHERE username=%s"
            val = (r, username)
            mydv.commit()
            

        return "<center><h1>418 I'm a teapot</h1></center>", 418



app.run(os.getenv("HOST"), os.getenv("PORT"))