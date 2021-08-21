from flask import Flask, render_template, request, session,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import json
from datetime import datetime
import os


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'hpcl_key'
local_server = params['local_server']
app.config['UPLOAD_FOLDER'] = params['upload_location']
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Announcements_img(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Announcements_file(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Opentalks_img(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Opentalks_file(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Healthcheck_img(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Healthcheck_file(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Knowledge_img(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Knowledge_file(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    caption = db.Column(db.String(120), nullable=True)
    filename = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/", methods=['GET'])
def Announcement():
    Announcements_images = Announcements_img.query.filter_by().all()[0:params['no_of_images']]
    Announcements_files = Announcements_file.query.filter_by().all()[0:params['no_of_files']]
    return render_template('Announcements.html', params=params, Announcements_files=Announcements_files, Announcements_images=Announcements_images)

@app.route("/Opentalks")
def Opentalks():
    Opentalks_images = Opentalks_img.query.filter_by().all()[0:params['no_of_images']]
    Opentalks_files = Opentalks_file.query.filter_by().all()[0:params['no_of_files']]
    return render_template('Opentalks.html', params=params, Opentalks_files=Opentalks_files, Opentalks_images=Opentalks_images)

@app.route("/Healthcheck")
def Healthcheck():
    Healthcheck_images = Healthcheck_img.query.filter_by().all()[0:params['no_of_images']]
    Healthcheck_files = Healthcheck_file.query.filter_by().all()[0:params['no_of_files']]
    return render_template('Healthcheck.html', params=params, Healthcheck_files=Healthcheck_files, Healthcheck_images=Healthcheck_images)

@app.route("/Knowledge")
def Knowledge():
    Knowledge_images = Knowledge_img.query.filter_by().all()[0:params['no_of_images']]
    Knowledge_files = Knowledge_file.query.filter_by().all()[0:params['no_of_files']]
    return render_template('Knowledge.html', params=params, Knowledge_files=Knowledge_files, Knowledge_images=Knowledge_images)

@app.route("/login", methods=['GET','POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        Announcements_images = Announcements_img.query.filter_by().all()[0:params['no_of_images']]
        Announcements_files = Announcements_file.query.filter_by().all()[0:params['no_of_files']]
        Opentalks_images = Opentalks_img.query.filter_by().all()[0:params['no_of_images']]
        Opentalks_files = Opentalks_file.query.filter_by().all()[0:params['no_of_files']]
        Healthcheck_images = Healthcheck_img.query.filter_by().all()[0:params['no_of_images']]
        Healthcheck_files = Healthcheck_file.query.filter_by().all()[0:params['no_of_files']]
        Knowledge_images = Knowledge_img.query.filter_by().all()[0:params['no_of_images']]
        Knowledge_files = Knowledge_file.query.filter_by().all()[0:params['no_of_files']]
        return render_template('dashboard.html', params=params, Announcements_images=Announcements_images, Announcements_files=Announcements_files, Knowledge_files=Knowledge_files, Knowledge_images=Knowledge_images, Opentalks_files=Opentalks_files, Opentalks_images=Opentalks_images, Healthcheck_files=Healthcheck_files, Healthcheck_images=Healthcheck_images)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if(username == params['admin_user'] and userpass == params['admin_pass'] ):
            session['user'] = username
            Announcements_images = Announcements_img.query.filter_by().all()[0:params['no_of_images']]
            Announcements_files = Announcements_file.query.filter_by().all()[0:params['no_of_files']]
            Opentalks_images = Opentalks_img.query.filter_by().all()[0:params['no_of_images']]
            Opentalks_files = Opentalks_file.query.filter_by().all()[0:params['no_of_files']]
            Healthcheck_images = Healthcheck_img.query.filter_by().all()[0:params['no_of_images']]
            Healthcheck_files = Healthcheck_file.query.filter_by().all()[0:params['no_of_files']]
            Knowledge_images = Knowledge_img.query.filter_by().all()[0:params['no_of_images']]
            Knowledge_files = Knowledge_file.query.filter_by().all()[0:params['no_of_files']]
            return render_template('dashboard.html', params=params, Announcements_images=Announcements_images, Announcements_files=Announcements_files, Knowledge_files=Knowledge_files, Knowledge_images=Knowledge_images, Opentalks_files=Opentalks_files, Opentalks_images=Opentalks_images, Healthcheck_files=Healthcheck_files, Healthcheck_images=Healthcheck_images)

    return render_template('login.html', params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/login')

@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return redirect('/login')

@app.route("/edit_announcements_img/<string:sno>", methods=['GET','POST'])
def edit_announcements_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                img= Announcements_img(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(img)
                db.session.commit()
            else:
                img= Announcements_img.query.filter_by(sno=sno).first()
                img.title= box_title
                img.filename= filename
                img.caption= caption
                img.date= date
                db.session.commit()

                return redirect('/edit_announcements_img/'+sno)
        img = Announcements_img.query.filter_by(sno=sno).first()
        return render_template('edit_announcements_img.html', params=params, sno=sno, img=img)

@app.route("/delete_announcements_img/<string:sno>", methods=['GET','POST'])
def delete_announcements_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        img= Announcements_img.query.filter_by(sno=sno).first()
        db.session.delete(img)
        db.session.commit()
    return redirect('/login')

@app.route("/edit_announcements_file/<string:sno>", methods=['GET','POST'])
def edit_announcements_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                file = Announcements_file(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(file)
                db.session.commit()
            else:
                file= Announcements_file.query.filter_by(sno=sno).first()
                file.title= box_title
                file.filename= filename
                file.caption= caption
                file.date= date
                db.session.commit()

                return redirect('/edit_announcements_file/'+sno)
        file = Announcements_file.query.filter_by(sno=sno).first()
        return render_template('edit_announcements_file.html', params=params, sno=sno, file=file)

@app.route("/delete_announcements_file/<string:sno>", methods=['GET','POST'])
def delete_announcements_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        file= Announcements_file.query.filter_by(sno=sno).first()
        db.session.delete(file)
        db.session.commit()
    return redirect('/login')

@app.route("/edit_opentalks_img/<string:sno>", methods=['GET','POST'])
def edit_opentalks_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                img= Opentalks_img(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(img)
                db.session.commit()
            else:
                img = Opentalks_img.query.filter_by(sno=sno).first()
                img.title= box_title
                img.filename= filename
                img.caption= caption
                img.date= date
                db.session.commit()

                return redirect('/edit_opentalks_img/'+sno)
        img = Opentalks_img.query.filter_by(sno=sno).first()
        return render_template('edit_opentalks_img.html', params=params, sno=sno, img=img)

@app.route("/delete_opentalks_img/<string:sno>", methods=['GET','POST'])
def delete_opentalks_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        img= Opentalks_img.query.filter_by(sno=sno).first()
        db.session.delete(img)
        db.session.commit()
    return redirect('/login')

@app.route("/edit_opentalks_file/<string:sno>", methods=['GET','POST'])
def edit_opentalks_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                file = Opentalks_file(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(file)
                db.session.commit()
            else:
                file= Opentalks_file.query.filter_by(sno=sno).first()
                file.title= box_title
                file.filename= filename
                file.caption= caption
                file.date= date
                db.session.commit()

                return redirect('/edit_opentalks_file/'+sno)
        file = Opentalks_file.query.filter_by(sno=sno).first()
        return render_template('edit_opentalks_file.html', params=params, sno=sno, file=file)

@app.route("/delete_opentalks_file/<string:sno>", methods=['GET','POST'])
def delete_opentalks_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        file= Opentalks_file.query.filter_by(sno=sno).first()
        db.session.delete(file)
        db.session.commit()
    return redirect('/login')

@app.route("/edit_healthcheck_img/<string:sno>", methods=['GET','POST'])
def edit_healthcheck_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                img= Healthcheck_img(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(img)
                db.session.commit()
            else:
                img = Healthcheck_img.query.filter_by(sno=sno).first()
                img.title= box_title
                img.filename= filename
                img.caption= caption
                img.date= date
                db.session.commit()

                return redirect('/edit_healthcheck_img/'+sno)
        img = Healthcheck_img.query.filter_by(sno=sno).first()
        return render_template('edit_healthcheck_img.html', params=params, sno=sno, img=img)

@app.route("/delete_healthcheck_img/<string:sno>", methods=['GET','POST'])
def delete_healthcheck_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        img= Healthcheck_img.query.filter_by(sno=sno).first()
        db.session.delete(img)
        db.session.commit()
        return redirect('/login')

@app.route("/edit_healthcheck_file/<string:sno>", methods=['GET','POST'])
def edit_healthcheck_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                file = Healthcheck_file(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(file)
                db.session.commit()
            else:
                file= Healthcheck_file.query.filter_by(sno=sno).first()
                file.title= box_title
                file.filename= filename
                file.caption= caption
                file.date= date
                db.session.commit()

                return redirect('/edit_healthcheck_file/'+sno)
        file = Healthcheck_file.query.filter_by(sno=sno).first()
        return render_template('edit_healthcheck_file.html', params=params, sno=sno, file=file)

@app.route("/delete_healthcheck_file/<string:sno>", methods=['GET','POST'])
def delete_healthcheck_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        file= Healthcheck_file.query.filter_by(sno=sno).first()
        db.session.delete(file)
        db.session.commit()
    return redirect('/login')

@app.route("/edit_knowledge_img/<string:sno>", methods=['GET','POST'])
def edit_knowledge_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                img= Knowledge_img(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(img)
                db.session.commit()
            else:
                img = Knowledge_img.query.filter_by(sno=sno).first()
                img.title= box_title
                img.filename= filename
                img.caption= caption
                img.date= date
                db.session.commit()

                return redirect('/edit_knowledge_img/'+sno)
        img = Knowledge_img.query.filter_by(sno=sno).first()
        return render_template('edit_knowledge_img.html', params=params, sno=sno, img=img)

@app.route("/delete_knowledge_img/<string:sno>", methods=['GET','POST'])
def delete_knowledge_img(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        img= Knowledge_img.query.filter_by(sno=sno).first()
        db.session.delete(img)
        db.session.commit()
        return redirect('/login')

@app.route("/edit_knowledge_file/<string:sno>", methods=['GET','POST'])
def edit_knowledge_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            filename = request.form.get('filename')
            caption = request.form.get('caption')
            date = datetime.now()

            if sno == '0':
                file = Knowledge_file(title=box_title, filename=filename, caption=caption, date=date)
                db.session.add(file)
                db.session.commit()
            else:
                file= Knowledge_file.query.filter_by(sno=sno).first()
                file.title= box_title
                file.filename= filename
                file.caption= caption
                file.date= date
                db.session.commit()

                return redirect('/edit_knowledge_file/'+sno)
        file = Knowledge_file.query.filter_by(sno=sno).first()
        return render_template('edit_knowledge_file.html', params=params, sno=sno, file=file)

@app.route("/delete_knowledge_file/<string:sno>", methods=['GET','POST'])
def delete_knowledge_file(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        file= Knowledge_file.query.filter_by(sno=sno).first()
        db.session.delete(file)
        db.session.commit()
    return redirect('/login')



app.run(debug=True)


