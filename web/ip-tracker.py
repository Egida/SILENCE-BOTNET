from setup import mydv
import requests
import geocoder
import flask

app = flask.Flask(__name__)

@app.route('/ip-tracker', methods=['GET'])

def ip_tracker():
    if flask.request.method == 'GET':
        username = flask.request.args.get('username')
        
        ip_address = flask.request.remote_addr
        g = geocoder.ip(ip_address)
        country = g.country
        city = g.city
        state = g.state
        zip = g.postal
        isp = g.org

        cursor = mydv.cursor()
        sql = "INSERT INTO ip_tracker (username, ip_address, country, city, state, zip, isp)"
        val = (username, ip_address, country, city, state, zip, isp)
        cursor.execute(sql, val)
        
        


app.run(host="localhost", port=40000)