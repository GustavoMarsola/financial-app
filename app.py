import os
from flask import Flask, render_template
from database import Database
from dotenv import load_dotenv

load_dotenv('.env')

DB_ULR = os.environ.get("PGURL_LOCAL")

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)