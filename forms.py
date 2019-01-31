from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class ColorForm(FlaskForm):
    R = IntegerField('Red', validators=[DataRequired()])
    G = IntegerField('Green', validators=[DataRequired()])
    B = IntegerField('Blue', validators=[DataRequired()])
    submit = SubmitField('Submit')