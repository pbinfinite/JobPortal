from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

from models import Login, Candidate, Recruiter, Job_Profile, Job_Profile_job_Location, Interview, Applications, Resume, Resume_resume_skills

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()