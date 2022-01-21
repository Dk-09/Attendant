from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, NumberRange
from main.model import students

class loginform(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

class registerform(FlaskForm):

    def validate_mail(self, mail_to_check):
        mail = students.query.filter_by(mail=mail_to_check.data).first()
        if mail:
            raise ValidationError('Mail already exists! Please try a different mail')

    def validate_name(self, name_to_check):
        name = students.query.filter_by(name=name_to_check.data).first()
        if name:
            raise ValidationError('Name already exists! Please try a full name with middle name')

    def validate_enroll_no(self, enroll_no_to_check):
        enroll_no = students.query.filter_by(enroll_no=enroll_no_to_check.data).first()
        if enroll_no:
            raise ValidationError('Enrollment number already exists! Please try a different Enrollment number')
        

    name = StringField(validators=[DataRequired()])
    mail = StringField(validators=[Email(), DataRequired()])
    enroll_no = IntegerField(validators = [DataRequired()])
    roll_no = IntegerField(validators = [DataRequired()])
    submit=SubmitField()

class delete_user(FlaskForm):
    id = HiddenField()
    delete = SubmitField()

