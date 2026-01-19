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

# -------------------------
# ROUTES
# -------------------------

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/departments")
def departments():
    return render_template("departments.html")

@app.route("/faculty")
def faculty():
    return render_template("faculty.html")


@app.route("/examination")
def examination():
    return render_template("examination.html")


@app.route("/admissions")
def admissions():
    return render_template("admissions.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (name, email, course)
    )
    conn.commit()
    conn.close()

    return redirect('/')
    
if __name__ == "__main__":
    app.run()

