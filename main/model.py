from enum import unique
from main import db, login_manager
from main import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return login.query.get(int(user_id))

class login(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=30), nullable=False)

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)

class students(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    mail = db.Column(db.String(length=30), nullable=False, unique=True)
    enroll_no = db.Column(db.Integer(), nullable=False, unique=True)
    roll_no = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return f'Item {self.name}'