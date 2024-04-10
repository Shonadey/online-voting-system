from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def index():
    return render_template('ind.html')
def register():
    name = request.form['name']
    email = request.form['email']

    conn = mysql.connect('registered_users.db')
    c= conn.cursor()
    c.execute('INSERT INTO users(name,email) VALUES (?,?)',(name,email))
    conn.commit()
    conn.close()

    return 'Registration successful!'
if __name__ == '__main__':
    app.run(debug=True)