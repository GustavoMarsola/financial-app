import os
from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db.validateUser(email, password)
        if result[0] is True and result[1] != 0:
            print(f'O usuário {email} foi logado')
            name = result[1][0][1]
            return render_template('index.html',user=name)
        elif result[0] is False and result[1] != 0:
            return render_template('login.html',error='Senha incorreta')
        else:
            return render_template('login.html',error='Usuário não encontrado')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)