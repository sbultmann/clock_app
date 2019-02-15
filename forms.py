from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired

class ColorForm(FlaskForm):
    R = IntegerField('Red')
    G = IntegerField('Green')
    B = IntegerField('Blue')
    msg = StringField('Message')
    submit = SubmitField('Submit')