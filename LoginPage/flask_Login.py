from flask import Flask, request

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
	req_data =request.args
	if req_data["username"]=="admin" and req_data["pwd"]=="pass":
		return "success"
	else:
		return "failed"

if __name__ == "__main__":
	app.run(host="127.0.0.1",port=9000,debug = True)
	
	
