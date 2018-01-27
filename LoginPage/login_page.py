import MySQLdb
from flask import Flask, request, jsonify

app = Flask(__name__)
db = MySQLdb.connect("localhost","root","dwarkamai","user")
cursor = db.cursor()
@app.route("/login")
def check_login():
    request_data = request.args
    uname = request_data["username"]
    passwd = request_data["password"]

   # cursor = db.cursor()
    cursor.execute("select * from users where username = %s AND password = %s", [uname, passwd])
    result = cursor.fetchall()
    if result:
        return "success"
    else:
        return "fail"
    db.commit()
    
@app.route("/user")
def get_users():
	cursor.execute("select * from users")
	entries = cursor.fetchall()
	return jsonify({"users":entries})
	'''response_data = []
	for entry in entries:
		res_dict = {}
		res_dict["username"] = entry[0]
		res_dict["password"] = entry[1]
		response_data.append(res_dict)
	response_dict = {'data':response_data}
	return json.dumps(response_dict)
'''
if __name__=="__main__":
    app.run(host='127.0.0.1', port=2019, debug=True)
db.close()
