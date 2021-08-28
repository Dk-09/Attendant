from flask import render_template, redirect, url_for, flash, request
from flask_login.utils import logout_user
from main import app, db
from main.form import loginform, registerform
from main.model import login, students
from flask_login import login_user, logout_user, login_required, current_user
from flask.helpers import flash
from functools import wraps

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('/dashboard/home.html')

@app.route('/start')
@login_required
def start():
    return render_template('/dashboard/start.html')

@app.route('/student')
@login_required
def student():
    return render_template('/dashboard/student.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('loginpage'))

@app.route('/login', methods=['GET','POST'])
def loginpage():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = loginform()
        if form.validate_on_submit():
            attempted_user = login.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                return redirect(url_for('home'))
            else:
                flash("Incorrect username or password", category='danger')
        return render_template('/login/index.html', form=form)

@app.route('/admission', methods=['GET','POST'])
@login_required
def register_page():
    form = registerform()
    if form.validate_on_submit():
        user_to_create = students(name = form.name.data,mail = form.mail.data,enroll_no=form.enroll_no.data,roll_no=form.roll_no.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash('User Added', 'info')
        
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg[0]}', category='danger')
    
    return render_template('/dashboard/new_admission.html', form=form)

@app.route('/shutdown')
@login_required
def shutdown():
    logout_user()
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shuting down...you can close this tab..."