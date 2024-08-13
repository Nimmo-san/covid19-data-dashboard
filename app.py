from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
	conn = psycopg2.connect(dbname='covid19_data', user='nemo', password='nemo', host='localhost')
	return conn





@app.route('/')
def home():
	return jsonify(message="Welcome to the covid19 data dashboard")

if __name__ == '__main__':
	app.run(debug=True)
