from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    return render_template('profile.html', username=username, posts=['첫 글', '두 번째 글'])

@app.route('/newuser/<username>')
def new_user(username):
    return render_template('profile.html', username=username, posts=[])

if __name__ == "__main__":
    app.run(debug=True)