from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User class
class User(UserMixin):
    def __init__(self, username):
        self.username = username

# Dummy user for authentication
users = {'admin': {'password': 'Password'}}

@login_manager.user_loader
def load_user(username):
    return User(username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('gallery'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/gallery')
@login_required
def gallery():
    cars = ['Car 1', 'Car 2', 'Car 3', 'Car 4', 'Car 5']
    return render_template('gallery.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
