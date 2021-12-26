from flask import render_template, redirect, url_for, flash, request
from flask_login.utils import logout_user
from main import app, db
from main.form import loginform, registerform
from main.model import login, students
from flask_login import login_user, logout_user, login_required, current_user
from flask.helpers import flash
import os, csv
from main.ap import start_face_recognition
from main.cam import camera

@app.route('/')
@app.route('/start', methods=['GET','POST'])
@login_required
def start():
    if request.method == 'POST':    
        path_to_img = os.getcwd() + "/main/img/"
        if not os.path.exists(path_to_img):
            os.mkdir(path_to_img)
            print("[*] Making img file...")
        dir = os.listdir(path_to_img)
        if len(dir) > 0:
            start_face_recognition()
        else:
            return redirect(url_for('register_page'))
    else:
        return render_template('/dashboard/start.html')
    return render_template('/dashboard/start.html')

@app.route('/record')
@login_required
def record():
    files = os.listdir("main/database/")
    return render_template('/dashboard/record.html',files=files)

@app.route('/show_file/<string:fname>')
@login_required
def show_file(fname):
    file = open("main/database/" + fname)
    csvreader = csv.reader(file)
    return render_template('/dashboard/show_file.html', csvreader=csvreader)

@app.route('/student', methods=['GET','POST'])
@login_required
def student():
    items = students.query.all()
    return render_template('/dashboard/student.html', items=items)

@app.route('/delete_student/<string:ids>/<string:name>', methods=['POST'])
@login_required
def delete_student(ids, name):
    path = os.getcwd()
    fullpath = path + "/main/img/" + name.strip() + ".jpg"
    fullpath2 = path + "/main/database2/" + name.strip() + ".csv"
    os.remove(fullpath)
    os.remove(fullpath2)
    print("[+] Removing: " + fullpath)
    print("[+] Removing: " + fullpath2)
    print("[+] Deleted sucessfully")
    students.query.filter_by(id=ids).delete()
    db.session.commit()
    
    return redirect(url_for('student'))
    

@app.route('/logout')
def logout():
    logout_user()
    print("[-] Logging out...")
    return redirect(url_for('loginpage'))


@app.route('/login', methods=['GET','POST'])
def loginpage(): 
    if current_user.is_authenticated:
        return redirect(url_for('start'))
    else:
        form = loginform()
        if form.validate_on_submit():
            attempted_user = login.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                return redirect(url_for('start'))
            else:
                flash("Incorrect username or password", category='danger')
        return render_template('/login/index.html', form=form)

    

@app.route('/admission', methods=['GET','POST'])
@login_required
def register_page():
    form = registerform()
    if form.validate_on_submit():
        if form.name.data:
            camera(form.name.data)
        user_to_create = students(name = form.name.data,mail = form.mail.data,enroll_no=form.enroll_no.data,roll_no=form.roll_no.data)
        db.session.add(user_to_create)
        db.session.commit()
        path = "main/database2/"
        with open(os.path.join(path,form.name.data)+".csv", 'w') as e:
            pass
        print("[+] creating file: " + form.name.data + ".csv")
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
    func()
    return "Shuting down...you can close this tab..."

