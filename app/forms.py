from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ContactForm(FlaskForm):
    name = StringField ('Name', validators = [DataRequired('(Required)')])
    email = StringField ('Email', validators = [DataRequired('(Required)'), Email()])
    subject = StringField ('Subject', validators = [DataRequired('(Required)')])
    message = TextAreaField ('Message', validators = [DataRequired('(Required)')])
    