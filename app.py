from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE CONNECTION FUNCTION
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect('campussphere.db')
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# CREATE TABLE (RUNS ON START)
# -----------------------------
conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()
conn.close()

# -----------------------------
# ROUTES
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')
    
    @app.route("/departments")
def departments():
    return render_template("departments.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (name, email, course)
    )
    conn.commit()
    conn.close()

    return "<h2 style='text-align:center;'>Registration Successful 🎉</h2>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

