from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        if username == 'myusername' and password == 'mypassword':
            return 'Login successful!'
            # Add your post-login logic here
        else:
            return 'Invalid username or password. Please try again.'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
