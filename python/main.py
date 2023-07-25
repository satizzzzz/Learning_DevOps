from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    # Process the user details (you can save them to a database, etc.)

    return f"Thank you for submitting your details, {first_name}!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)