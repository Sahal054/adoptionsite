from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):
    name = StringField('name of puppy')
    submit= SubmitField('submit')


class DelForm(FlaskForm):
    id = IntegerField('enter id')
    name=StringField("enter name")
    submit= SubmitField('submit')
