import psycopg2
from flask import Flask, redirect, render_template, request

conn=psycopg2.connect(database='jobportal', user='postgres', password='pb1sql', port=5432, host='127.0.0.1')
conn.autocommit=True
conn.set_isolation_level(0)
cur=conn.cursor()

dbcr='''
dropdb database if not exists jobportal;
create database jobportal;
'''
createfile = open('./createtables.sql','r')

insertfile=open('./insertrecs.sql','r')



cur.execute(createfile.read())
cur.execute(insertfile.read())
cur.close()
conn.commit()
conn.close()


app=Flask(__name__)

@app.route('/')
def loginpage():
    #signup login for candidate and recruiter
    return "hello world"

@app.route('/signupc', endpoint='singup_cand')
def signup_cand():
    return "signup cand"
#commented to add endpoint to all functions
'''@app.route('/registerc')
def register_cand():
    return "register cand"

@app.route('/signuprec')
def signup_cand():
    return "signup rec"

@app.route('/registerrec')
def register_cand():
    return "register rec"

#login after register
@app.route('/login')
def login():
    return "login"

@app.route('/login_info')
def login_info():
    return "login info"

@app.route('/profile_cand')
def profile_cand():
    return "cand profile"

@app.route('/profile_rec')
def profile_rec():
    return "rec profile"

@app.route('/home_cand')
def candidate_home():
    return "cand home"

@app.route('/rec_home')
def rec_home():
    return "rec home"

@app.route('/resume_view')
def view_resume():
    return "view resume"

@app.route('/resume_edit')
def edit_resume():
    return "edit resume"

@app.route('/apl_for_job')
def appl_for_job():
    return "appl for this job"'''

@app.route('/rec', endpoint='recdis')
def recdis():
    conn=psycopg2.connect(database='jobportal', user='postgres', password='pb1sql', port=5432, host='127.0.0.1')
    cur=conn.cursor()
    cur.execute('select emp_name, emp_id from Recruiter where emp_id=2001;')
    stat = cur.fetchone()
    return stat

if __name__=='__main__':
    app.run(debug=True)
