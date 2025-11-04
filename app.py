from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Peter Scott in 330'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flask_postgres_pesc3485_user:lbcH2gmgGSjMYwgEoLQGrSKVv4kUsnLp@dpg-d44m7ti4d50c73ek31mg-a.oregon-postgres.render.com/flask_postgres_pesc3485")
    conn.close()
    return "Database Cponnected Successfully"
