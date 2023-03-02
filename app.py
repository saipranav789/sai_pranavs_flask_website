from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  "Backend Developer", "Frontend Developer", "Full Stack Developer",
  "Data Analyst", "Software Development Engineer"
]


@app.route("/")
def hello_web():
  return render_template("home.html", jobs=JOBS)


# @app.route("/contact_me")
# def hello_contact():
#   return render_template("contact_me.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
