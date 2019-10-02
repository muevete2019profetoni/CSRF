from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class Loginform(Form):
    username = StringField('usuario', [
        validators.Required(message='El usuario es obligatorio'),
        validators.length(min=4, max=30, message='Usuario incorrecto')
    ])
    password = PasswordField('password', [
        validators.Required(message='El password es obligatorio')
    ])
