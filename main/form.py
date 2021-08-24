from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from main.model import students

class loginform(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

class registerform(FlaskForm):

    def mail_check(self, mail_to_check):
        user = students.query.filter_by(mail=mail_to_check.data).first()
        if user:
            raise ValidationError('Mail already exists! Please try a different mail')

    def enroll_no_check(self, enroll_no_to_check):
        user = students.query.filter_by(enroll_no=enroll_no_to_check.data).first()
        if user:
            raise ValidationError('Enrollment number already exists! Please try a different Enrollment number')


    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    enroll_no = StringField(validators = [DataRequired()])
    roll_no = StringField(validators = [DataRequired()])
