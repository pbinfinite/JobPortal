import re
from app import db

class Login(db.Model):
    __tablename__='Login'

    login_username=db.Column(db.String(25), primary_key=True, nullable=False)
    user_password=db.Column(db.String(15), nullable=False)
    login_user_type=db.Column(db.String(1), nullable=False)

    def __init__(self, login_username, user_password, login_user_type):
        self.login_username = login_username
        self.user_password = user_password
        self.login_user_type = login_user_type
    
    def serialize(self):
        return {
            'login_username': self.login_username,
            'user_password': self.user_password,
            'login_user_type':self.login_user_type
        }

class Candidate(db.Model):
    __tablename__ = 'Candidate'

    cand_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cand_email = db.Column(db.String(40))
    cand_address = db.Column(db.String(25), nullable=False)
    cand_name = db.Column(db.String(25), nullable=False)
    cand_phone = db.Column(db.Integer)
    cand_DOB = db.Column(db.DateTime) #check constraint
    cand_gender = db.Column(db.String(1), nullable=False)
    cand_login_username = db.Column(db.String(25), db.ForeignKey('Login.login_username'),cascade='delete, update',nullable=False)
    

    def __init__(self, cand_id, cand_email, cand_address, cand_name, cand_phone, cand_DOB, cand_gender, cand_login_username):
        self.cand_id = cand_id
        self.cand_email = cand_email
        self.cand_address = cand_address
        self.cand_name = cand_name
        self.cand_phone = cand_phone
        self.cand_DOB = cand_DOB
        self.cand_gender = cand_gender
        self.cand_login_username = cand_login_username

    def serialize(self):
        return {
            'cand_id': self.cand_id, 
            'cand_email': self.cand_email,
            'cand_address': self.cand_address, 
            'cand_name': self.cand_name, 
            'cand_phone': self.cand_phone,
            'cand_DOB': self.cand_DOB,
            'cand_gender': self.cand_gender,
            'cand_login_username': self.cand_login_username
        }
    
class Recruiter(db.Model):
    __tablename__='Recruiter'

    emp_name = db.Column(db.String(30), nullable=False)
    emp_id=db.Column(db.Integer, primary_key=True, nullable=False)
    emp_HQ = db.Column(db.String(255), nullable=False)
    emp_phone=db.Column(db.Integer)
    emp_email=db.Column(db.String(40), nullable=False)
    rlogin_username=db.Column(db.String(25),db.ForeignKey('Login.login_username'),cascade='delete, update', nullable=False)

    def __init__(self, emp_name, emp_id,emp_HQ, emp_phone, emp_email, rlogin_username):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_HQ=emp_HQ
        self.emp_phone=emp_phone
        self.emp_email=emp_email
        self.rlogin_username=rlogin_username

    def serialize(self):
        return {
            'emp_name': self.emp_name,
            'emp_id':self.emp_id,
            'emp_HQ':self.emp_HQ,
            'emp_phone':self.emp_phone,
            'emp_email':self.emp_email,
            'rlogin_username':self.rlogin_username
        }

class Job_Profile(db.Model):
    __tablename__='Job_Profile'

    job_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_name = db.Column(db.String(15), nullable=False)
    job_type = db.Column(db.String(15), nullable=False)
    job_description = db.Column(db.String(50))
    recruiter_id = db.Column(db.Integer, db.ForeignKey('Recruiter.emp_id'))
    job_qualification = db.Column(db.String(10), nullable=False)
    job_experience = db.Column(db.Integer, default = 0, nullable=False)
    job_primary_skill = db.Column(db.String(50), nullable=False)

    def __init__(self, job_id, job_name, job_type, job_description, recruiter_id, job_qualification, job_experience, job_primary_skill):
        self.job_id =job_id
        self.job_name=job_name
        self.job_type=job_type
        self.job_description=job_description
        self.recruiter_id=recruiter_id
        self.job_qualification=job_qualification
        self.job_experience = job_experience
        self.job_primary_skill = job_primary_skill

    def serialize(self):
        return {
            'job_id':self.job_id,
            'job_name':self.job_name,
            'job_type':self.job_type,
            'job_description':self.job_description,
            'recruiter_id':self.recruiter_id,
            'job_qualification':self.job_qualification,
            'job_experience':self.job_experience,
            'job_primary_skill':self.job_primary_skill
        }


class Job_Profile_job_Location(db.Model):
    __tablename__='Job_Profile_job_Location'

    job_id = db.Column(db.Integer,db.ForeignKey('Job_Profile.job_id'), primary_key=True, nullable=False)
    job_location = db.Column(db.String(30), primary_key=True, nullable=False)
    job_vacancy = db.Column(db.Integer)

    def __init__(self, job_id, job_location, job_vacancy):
        self.job_id=job_id
        self.job_location =job_location
        self.job_vacancy=job_vacancy
    
    def serialize(self):
        return {
            'job_id':self.job_id,
            'job_location':self.job_location,
            'job_vacancy':self.job_vacancy
        }

class Interview(db.Model):
    __tablename__='Interview'

    int_id = db.Column(db.Integer, primary_key=True, nullable=False)
    int_job = db.Column(db.Integer, db.ForeignKey('Job_Profile.job_id'),nullable=False)
    int_date = db.Column(db.DateTime, nullable=False)
    int_result = db.Column(db.String(10))
    int_remarks=db.Column(db.String(255), nullable=False)
    int_type=db.Column(db.String(15), nullable=False)
    candidateid = db.Column(db.Integer, db.ForeignKey('Candidate.cand_id'),nullable=False)

    def __init__(self, int_id, int_job, int_date, int_result, int_remarks, int_type, candidateid):
        self.int_id=int_id
        self.int_job=int_job
        self.int_date=int_date
        self.int_result=int_result
        self.int_remarks=int_remarks
        self.int_type=int_type
        self.candidateid=candidateid

    def serialize(self):
        return {
            'int_id':self.int_id,
            'int_job':self.int_job,
            'int_date':self.int_date,
            'int_result':self.int_result,
            'int_remarks':self.int_remarks,
            'int_type':self.int_type,
            'candidateid':self.candidateid
        }

class Applications(db.Model):
    __tablename__='Applications'

    application_id =db.Column(db.Integer, primary_key=True, nullable=False)
    application_job_id=db.Column(db.Integer, db.ForeignKey('Job_Profile.job_id'),nullable=False)
    application_date=db.Column(db.DateTime, nullable=False)
    application_cand_id = db.Column(db.Integer, db.ForeignKey('Candidate.cand_id'),nullable=False)

    def __init__(self, application_id, application_job_id, application_date, application_cand_id):
        self.application_id=application_id
        self.application_job_id=application_job_id
        self.application_date=application_date
        self.application_cand_id=application_cand_id

    def serialize(self):
        return {
            'application_id':self.application_id,
            'application_job_id':self.application_job_id,
            'application_date':self.application_date,
            'application_cand_id':self.application_cand_id
        }

class Resume(db.Model):
    __tablename__='Resume'

    resume_id=db.Column(db.Integer, primary_key=True, nullable=False)
    resume_name=db.Column(db.String(15), nullable=False)
    resume_qualification = db.Column(db.String(10), nullable=False)
    candidate_id=db.Column(db.Integer, db.ForeignKey('Candidate.cand_id'), nullable=False)
    resume_experience=db.Column(db.Integer, nullable=False)

    def __init__(self, resume_id, resume_name, resume_qualification, candidate_id, resume_experience):
        self.resume_id=resume_id
        self.resume_name=resume_name
        self.resume_qualification=resume_qualification
        self.candidate_id=candidate_id
        self.resume_experience=resume_experience

    def serialize(self):
        return {
            'resume_id':self.resume_id,
            'resume_name':self.resume_name,
            'resume_qualification':self.resume_qualification,
            'candidate_id':self.candidate_id,
            'resume_experience':self.resume_experience
        }

class Resume_resume_skills(db.Model):
    __tablename__='Resume_resume_skills'

    resume_id=db.Column(db.Integer, db.ForeignKey('Resume.resume_id'), primary_key=True,cascade='update', nullable=False)
    resume_skills=db.Column(db.String(50), primary_key=True, nullable=False)

    def __init__(self, resume_id, resume_skills):
        self.resume_id=resume_id
        self.resume_skills=resume_skills

    def serialize(self):
        return {
            'resume_id':self.resume_id,
            'resume_skills':self.resume_skills
        }