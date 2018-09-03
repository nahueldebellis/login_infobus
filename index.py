from flask import Flask, render_template, request, abort, redirect
#from flaskext.mysql import MySQL
import os
import mysql.connector as mysql

app = Flask(__name__)

"""mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = "nhdb"
app.config['MYSQL_DATABASE_PASSWORD'] = "123456789"
app.config['MYSQL_DATABASE_DB'] = "users"
app.config['MYSQL_DATABASER_HOST'] = "localhost"
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

app.config['MYSQL_DATABASE_DB'] = "tokens"
con2 = mysql.connect()
cur = con2.cursor()
"""
conneccion = mysql.connect(
	host="localhost",
	user="nhdb",
	passwd="123456789"
)
cursor = conneccion.cursor()

@app.route("/reset")
def reset():
	return render_template("resetContra.html")

@app.route("/getoken")
def token():
	tok = os.urandom(10).hex()
	param = (tok, )
	cursor.execute('USE tokens')
	cursor.execute('INSERT INTO tok VALUES(%s)', param)
	conneccion.commit()
	return tok

@app.route("/validate/<tok>")
def sesion(tok):
	param = (tok, )
	cursor.execute('USE tokens')
	cursor.execute('SELECT * FROM tok where token = %s', param)
	inf = cursor.fetchall()
	if inf:
		return "True"
	return "False"

@app.route("/login")
def main():
	return render_template("login.html")

@app.route("/registro")
def nReg():
	return render_template('registro.html')

@app.route("/acceso", methods=['POST'])
def login():
	try:
		user = request.form["user"]
		password = request.form["pass"]
		param = (user, password)
		cursor.execute('USE users')
		cursor.execute('SELECT * from usuarios where usernames = %s and passwords = %s', param)
		data = cursor.fetchall()
		if(data):
			tok = token()
			return redirect("http://localhost:3000/"+tok, code=302)
		else:
			return "<h1>Usuario no registrado</h1>"
	except:
		abort(500)

@app.route("/nuevo", methods=['POST'])
def registro():
	user = request.form['name']
	password = request.form['password']
	email = request.form['Email']
	param = (user, password, email)
	cursor.execute('USE users')
	cursor.execute('insert into usuarios (`usernames`, `passwords`, `email`) values(%s, %s, %s)', param)
	conneccion.commit()
	return render_template("login.html")
