from flask import Flask, render_template, json, url_for, request, jsonify, make_response
from flask.ext.sqlalchemy import SQLAlchemy

# INIT
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:123456@mysql-server:3306/cross_engage'
db = SQLAlchemy(app)

# MODELS
class Counter(db.Model):
	__tablename__ = "counter"
	id = db.Column('id',db.Integer , primary_key=True)
	name = db.Column('name', db.String(20), unique=True , index=True)
	value = db.Column('value' , db.Integer)

	def __init__(self, name, value):
		self.name = name
		self.value = value

db.create_all()
db.session.commit()

db.session.query(Counter).delete()
db.session.commit()

# API ENDPOINTS
@app.route("/")
@app.route("/main")
def main():
	resp = make_response(render_template('index.html'))
	return resp

@app.route("/getStats")
def getStats():
	resp = {}
	counters = Counter.query.all()
	for counter in counters:
		resp[counter.name] = counter.value
	return jsonify(resp)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
