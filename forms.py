from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class ColorForm(FlaskForm):
    R = IntegerField('Red')
    G = IntegerField('Green')
    B = IntegerField('Blue')
    submit = SubmitField('Submit')