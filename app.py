import psycopg2
from datetime import timedelta
from flask import Flask, redirect, render_template, request, url_for
from flask import session

conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
conn.autocommit=True
conn.set_isolation_level(0)
cur=conn.cursor()
print("cursor ",cur)
dbcr='''
dropdb database if not exists jobportal;
create database jobportal;
'''
createfile = open('./createtables.sql','r')
insertfile=open('./insertrecs.sql','r')

cur.execute("select * from Login")
login_data = cur.fetchall()
print(login_data)            

if login_data == []:
    cur.execute(createfile.read())
    cur.execute(insertfile.read())
    
cur.close()
print("cursor after close",cur)

conn.commit()
conn.close()
print("cursor after end",cur)


app=Flask(__name__,template_folder='templates')
app.secret_key = "DBMS"
#session.pop("user", None)

role_link='H'
logged_user=''
@app.route('/', endpoint = 'loginpage', methods = ['GET', 'POST'])
def loginpage():
    #signup login for candidate and recruiter
    find = 0
    global role_link
    global logged_user
    if request.method == 'POST':
        # retrieving the entries made in the login form
        loginDetails = request.form
        username = loginDetails['username']
        password = loginDetails['password']
        role = loginDetails['role']
        role_link=role
        logged_user=username
        print(username, password, role)
        conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
        cur=conn.cursor()
        find = cur.execute('Select * from Login where (login_username, user_password, login_user_type) = (%s, %s,%s) ', (username, password,role))
        # selecting email and password attributes from jobseeker entity to check if the email and its password exists in the entity
        details = cur.fetchall()
        cur.close()
    # login to home page if we find such an entry in the table or redirect to the same page
    if find != 0:
        user = details[0][0]
        session["user"] = user
        print(user)
        return redirect('/home')
    else: 
        if "user" in session:
            print('here')
            return redirect('/logout')
        return render_template('login.html', find = find)

@app.route('/signup_cand', endpoint='singup_cand', methods = ['GET', 'POST'])
def signup_cand():
    if request.method == 'POST':
        # retrieving the entries made in the signup form
        userDetails = request.form
        name = userDetails['name']
        username = userDetails['username']
        role = userDetails['role']
        email = userDetails['email']
        address = userDetails['address']
        phone_num = userDetails['phone_num']
        gender = userDetails['gender']
        DOB = userDetails['DOB']
        password = userDetails['password']
        cpassword = userDetails['cpassword']
        # checking if the password entered in both the fields are same
        if password == cpassword and role == 'C':
            conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
            cur=conn.cursor()
            # creating a record by inserting the jobseeker details in jobseeker entity
            cur.execute("INSERT INTO Login(login_username, user_password, login_user_type) VALUES (%s, %s, %s)",(username, password, role))
            cur.execute("select nextval('Candidate_seq')")
            Cand_id = cur.fetchone()
            cur.execute("INSERT INTO Candidate(cand_id, Cand_name, Cand_email,Cand_address, Cand_phone , Cand_DOB, Cand_gender, cand_login_username) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)",(Cand_id, name, email, address,phone_num, DOB,gender,username))
            conn.commit()
            cur.close()
            print('here')
            # go to login page on submit
            return redirect('/')
        else:
            return redirect('signup_cand')
    return render_template('signup_cand.html')

@app.route('/signup_rec', endpoint='singup_rec', methods = ['GET', 'POST'])
def signup_rec():
    if request.method == 'POST':
        # retrieving the entries made in the signup form
        userDetails = request.form
        name = userDetails['name']
        username = userDetails['username']
        role = userDetails['role']
        email = userDetails['email']
        HQ = userDetails['HQ']
        phone_num = userDetails['phone_num']
        password = userDetails['password']
        cpassword = userDetails['cpassword']
        # checking if the password entered in both the fields are same
        if password == cpassword and role == 'R':
            conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
            cur=conn.cursor()
            # creating a record by inserting the jobseeker details in jobseeker entity
            cur.execute("INSERT INTO Login(login_username, user_password, login_user_type) VALUES (%s, %s, %s)",(username, password, role))
            cur.execute("select nextval('Candidate_seq')")
            emp_id = cur.fetchone()
            cur.execute("INSERT INTO Recruiter(emp_id,emp_name, emp_HQ, emp_phone,emp_email,login_username) VALUES (%s, %s, %s, %s, %s,%s)",(emp_id, name, HQ, phone_num,email, username))
            conn.commit()
            cur.close()
            print('here')
            # go to login page on submit
            return redirect('/')
        else:
            return redirect('signup_rec')
    return render_template('signup_rec.html')

@app.route('/home', endpoint='homepage')
def homepage():
    print(role_link)
    if(role_link=='C'):
        return redirect('/home_cand')
    elif(role_link=='R'):
        return redirect('/home_rec')
    else:
        return "at home page"

@app.route('/home_cand', endpoint='candidate_home', methods=['POST','GET'])
def candidate_home():

    conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
    cur=conn.cursor()
    cur.execute('select job_name, job_type, job_description, emp_name, job_qualifications, job_experience, job_primary_skill from Job_Profile as j, Recruiter as r where j.recruiter_id=r.emp_id;')
    recarr = cur.fetchall()

    if "user" in session:
        user = session["user"]
        int_sch='''select emp_name, job_name, int_date, int_type, int_result, int_remarks
        from interview as i, job_profile as j, recruiter as r, candidate as c, login as l
        where i.int_job=j.job_id and i.candidateid=c.cand_id and j.recruiter_id=r.emp_id and c.cand_login_username=l.login_username and l.login_username='{}';'''
        cur.execute(int_sch.format(user))
        interviewarr=cur.fetchall()
        conn.commit()
        cur.close()
        return render_template('candidate_page.html', recarr=recarr, intv = interviewarr)

@app.route('/home_rec', endpoint='rec_home', methods=['POST','GET'])
def rec_home():
    if "user" in session:
        user = session["user"]
        print(user)
        conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
        cur=conn.cursor()
        # selecting jobseeker details to display the name of the jobseeker on the home page who is currently logged in
        cur.execute("SELECT * FROM Recruiter WHERE login_username = '{}'".format(user))
        userdet = cur.fetchall()
        name = userdet[0][1]
        return render_template('recruiter_home.html', name = name)
    else:
        return redirect(url_for('login'))
    

@app.route('/apply',endpoint='applyjob', methods=['GET','POST'])
def applyjob():
    return "applied"

@app.route('/resume_edit', endpoint='edit_resume', methods=["GET","POST"])
def edit_resume():
    return "edit resume"

@app.route('/profile_cand', endpoint='profile_cand', methods=["GET","POST"])
def profile_cand():
    id=0
    if "user" in session:
        user = session["user"]
        conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
        cur=conn.cursor()
        cur.execute("select cand_name, cand_email, cand_address, cand_phone, cand_id from Candidate as c, Login as l where c.cand_login_username=l.login_username and l.login_username='{}';".format(user))
        old_details=cur.fetchone()
        id=old_details[4]

    if request.method == 'POST':
        profile=request.form
        name=profile["name"]
        email=profile["email"]
        address=profile["address"]
        phoneno=profile["phoneno"]
        
        cur.execute("update Candidate set cand_email=%s, cand_name=%s, cand_address=%s, cand_phone=%s where cand_id=%s;",(email, name, address,phoneno,id))
        conn.commit()
        cur.close()
        return redirect('/home_cand')
    return render_template('profile_edit_cand.html', profile=old_details)
#commented to add endpoint to all functions


@app.route('/profile_rec',endpoint='profile_rec', methods=["GET","POST"])
def profile_rec():
    id=0
    if "user" in session:
        user = session["user"]
        conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
        cur=conn.cursor()
        cur.execute("select emp_id, emp_name, emp_HQ, emp_phone, emp_email from Recruiter as r, Login as l where r.login_username=l.login_username and l.login_username='{}';".format(user))
        old_details=cur.fetchone()
        id=old_details[0]

    if request.method == 'POST':
        profile=request.form
        name=profile["name"]
        email=profile["email"]
        address=profile["address"]
        phoneno=profile["phoneno"]
        
        cur.execute("update Recruiter set emp_email=%s, emp_name=%s, emp_HQ=%s, emp_phone=%s where emp_id=%s;",(email, name, address,phoneno,id))
        conn.commit()
        cur.close()
        return redirect('/home_rec')
    return render_template('profile_edit_rec.html', profile_data=old_details)

'''
@app.route('/home_cand')
def candidate_home():
    return "cand home"

@app.route('/rec_home')
def rec_home():
    return "rec home"

@app.route('/addjob')
def add_job():
    return "adding new job appl"

@app.route('/resume_view')
def view_resume():
    return "view resume"

@app.route('/resume_edit')
def edit_resume():
    return "edit resume"
'''

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/')

@app.route('/rec', endpoint='recdis')
def recdis():
    conn=psycopg2.connect(database='jobportal', user='postgres', password='P@rimala9', port=5432, host='127.0.0.1')
    cur=conn.cursor()
    cur.execute('select emp_id, emp_name from Recruiter;')
    recarr = cur.fetchall()
    return render_template('recr_display.html', recarr=recarr)

if __name__=='__main__':
    app.run(debug=True)
