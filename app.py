from flask import Flask
import psycopg

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Peter Scott in 330'

@app.route('/db_test')
def testing():
    conn = psycopg.connect("postgresql://flask_postgres_pesc3485_user:lbcH2gmgGSjMYwgEoLQGrSKVv4kUsnLp@dpg-d44m7ti4d50c73ek31mg-a.oregon-postgres.render.com/flask_postgres_pesc3485")
    conn.close()
    return "Database Connected Successfully"

@app.route('/db_create')
def create():
    conn = psycopg.connect("postgresql://flask_postgres_pesc3485_user:lbcH2gmgGSjMYwgEoLQGrSKVv4kUsnLp@dpg-d44m7ti4d50c73ek31mg-a.oregon-postgres.render.com/flask_postgres_pesc3485")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                First VARCHAR(255),
                Last VARCHAR(255),
                City VARCHAR(255),
                Name VARCHAR(255),
                Number INT                
                );               
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created."

@app.route('/db_insert')
def insert():
    conn = psycopg.connect("postgresql://flask_postgres_pesc3485_user:lbcH2gmgGSjMYwgEoLQGrSKVv4kUsnLp@dpg-d44m7ti4d50c73ek31mg-a.oregon-postgres.render.com/flask_postgres_pesc3485")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);                        
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

