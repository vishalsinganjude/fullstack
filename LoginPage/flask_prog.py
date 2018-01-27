from flask import Flask, url_for, redirect
app = Flask(__name__)
@app.route("/hello")
def sayHello():
	return "Hello Pune"

@app.route("/name")
def studName():
	return "Vishal"

@app.route("/mob")
def mobileNo():
	return "8551960828"

#redirect and url_for

@app.route("/hello_admin")
def hello_admin():
	return "Hello Admin!!!!"

@app.route("/hello_guest/<guest>")
def hello_guest(guest):
	return "Hello %s as Guest" %guest

@app.route("/user/<name>"	)
def user(name):
	if name == "admin":
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest = name))
#variables
@app.route("/hello/<name>")
def nameS(name):
	return "Hello %s" %name

@app.route("/hello/<int:roll>")
def rollS(roll):
	return "Roll No: %d" %roll

@app.route("/hello/<float:per>")
def perS(per):
	if per >=40:
		return "Congo!!!!! You got %f percent" %per
	else:
		return "Sorry!!!!! You got %f percent" %per


#main method
if __name__ == "__main__":
	app.run(host= "127.0.0.1",port=9000, debug = "true")

