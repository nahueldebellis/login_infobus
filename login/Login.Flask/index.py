from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "users"
app.config['MYSQL_DATABASER_HOST'] = "localhost"
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/nReg")
def nReg():
	return render_template('registro.html')
@app.route("/login", methods=['POST'])
def login():
	user = request.form["user"]
	password = request.form["pass"]
	cursor.callproc('consultaUser',(user, password))
	data = cursor.fetchall()
	if(data):
		return "Exito"
	return "Error"

@app.route("/registro", methods=['POST'])
def registro():
	user = request.form['name']
	password = request.form['pass']
	email = request.form['email']
	cursor.callproc('nUser', (user, password, email))
	return render_template("index.html")
