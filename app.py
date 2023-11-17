from flask import Flask,render_template
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [
#     {"id":1,"title": "Data Analyist","location": "Lahore","salary": 80000},
#     {"id":2,"title": "web developer","location": "karachi","salary": 150000},
#     {"id":3, "title": "Devops","location": "remote"},
#     {"id":4, "title": "Front End Developer","location": "USA","salary": 20000},                                               
# ]

@app.route('/')

def home():
    jobs = load_jobs_from_db()
    return render_template("home.html",jobs=jobs,
                           company_name="Jaawan")


print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True )