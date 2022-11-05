from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):
    id=IntegerField("enter puppy id")
    name =StringField("enter your name")
    submit=SubmitField('submit')
