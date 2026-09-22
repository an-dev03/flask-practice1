from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/profile")
def profile_page():
    return render_template("profile.html", hobbies=["운동", "게임", "독서"])

if __name__ == "__main__":
    app.run(debug=True)