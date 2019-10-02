from flask import Flask
from flask import render_template
from flask import request
# libreria para ataques de terceros
from flask_wtf import CsrfProtect

from form import Loginform

app = Flask(__name__)
# palabra secreta
app.secret_key = 'palabra_muy_muy_secreta'
csrf = CsrfProtect(app)


# rutas
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Loginform()
    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run('127.0.0.1', 5080, debug=True)
