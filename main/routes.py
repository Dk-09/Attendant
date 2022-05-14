from flask import render_template, redirect, url_for, flash, request
from flask_login.utils import logout_user
from main import app, db
from main.form import loginform, registerform
from main.model import login, students
from flask_login import login_user, logout_user, login_required, current_user
from flask.helpers import flash
import os, csv
from main.send_data import send

@app.route('/')
@app.route('/start', methods=['GET','POST'])
@login_required
def start():
    if request.method == 'POST':    
        path_to_img = os.getcwd() + "/main/img/"
        if not os.path.exists(path_to_img):
            os.mkdir(path_to_img)
            print("\033[92m [*] Making img file...")
        dir = os.listdir(path_to_img)
        if len(dir) > 0:
            os.system(f"python3 main/ap.py")
        else:
            return redirect(url_for('register_page'))
    else:
        return render_template('/dashboard/start.html')
    return render_template('/dashboard/start.html')

@app.route('/record')
@login_required
def record():
    files = os.listdir("main/db1/")
    return render_template('/dashboard/record.html',files=files)

@app.route('/show_file/<string:fname>')
@login_required
def show_file(fname):
    file = open("main/db1/" + fname)
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
    fullpath2 = path + "/main/db2/" + name.strip() + ".csv"
    os.remove(fullpath)
    os.remove(fullpath2)
    print("\033[92m [+] Removing: " + fullpath)
    print("\033[92m [+] Removing: " + fullpath2)
    print("\033[92m [+] Deleted sucessfully")
    students.query.filter_by(id=ids).delete()
    db.session.commit()
    
    return redirect(url_for('student'))
    

@app.route('/logout')
def logout():
    logout_user()
    print("\033[33m [-] Logging out...")
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
                print("\033[92m [+] user looged in")
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
            os.system(f"python3 main/cam.py {form.name.data}")
        user_to_create = students(name = form.name.data,mail = form.mail.data,enroll_no=form.enroll_no.data,roll_no=form.roll_no.data)
        db.session.add(user_to_create)
        db.session.commit()
        path = "main/db2/"
        with open(os.path.join(path,form.name.data)+".csv", 'w') as e:
            pass
        print("\033[92m [+] creating file: " + form.name.data + ".csv")
        return redirect(url_for('student'))
        
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg[0]}', category='danger')
    return render_template('/dashboard/new_admission.html', form=form)

@app.route('/shutdown')
@login_required
def shutdown():
    try:
        send()
    except:
        pass
    logout_user()
    return "Shuting down...you can close this tab..."

