
CREATE TABLE IF NOT EXISTS Login
(
  login_username VARCHAR(25) NOT NULL,
  user_password VARCHAR(15) NOT NULL,
  login_user_type CHAR NOT NULL,
  PRIMARY KEY (login_username)
);

CREATE TABLE IF NOT EXISTS Candidate
(
  cand_id INT NOT NULL,
  Cand_name VARCHAR(25) NOT NULL,
  Cand_email VARCHAR(40),
  Cand_address Varchar(255),
  Cand_phone BIGINT ,
  Cand_DOB date NOT NULL check(date_part('year',age(Cand_DOB))>=18),
  Cand_gender CHAR NOT NULL,
  cand_login_username VARCHAR(25) NOT NULL ,
  PRIMARY KEY (cand_id),
  FOREIGN KEY (cand_login_username) REFERENCES Login(login_username) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Recruiter
(
  emp_id INT NOT NULL,
  emp_name VARCHAR(30) NOT NULL,
  emp_HQ VARCHAR(255) NOT NULL,
  emp_phone BIGINT,
  emp_email VARCHAR(40) NOT NULL,
  login_username VARCHAR(25) NOT NULL,
  PRIMARY KEY (emp_id),
  FOREIGN KEY (login_username) REFERENCES Login(login_username) ON UPDATE CASCADE ON DELETE CASCADE
  
);

CREATE TABLE IF NOT EXISTS Job_Profile 
(
  job_id INT NOT NULL,
  job_name CHAR(15) NOT NULL,
  job_type VARCHAR(15) NOT NULL,
  job_description varchar(50),
  recruiter_ID INT,
  job_qualifications VARCHAR(10) NOT NULL,
  job_experience INT NOT NULL DEFAULT 0,
  job_primary_skill varchar(50) NOT NULL,
  FOREIGN KEY (recruiter_ID) REFERENCES Recruiter(emp_id),
  PRIMARY KEY (job_id)
);

CREATE TABLE IF NOT EXISTS Job_Profile_job_location
(
  job_id INT NOT NULL,
  job_location VARCHAR(30) NOT NULL,
  job_vacancy INT ,
  PRIMARY KEY (job_location, job_id),
  FOREIGN KEY (job_id) REFERENCES Job_Profile(job_id) ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Interview
(
  int_id INT NOT NULL,
  int_job INT NOT NULL,
  int_date DATE NOT NULL,
  int_result VARCHAR(10) ,
  int_remarks VARCHAR(255) NOT NULL,
  int_type CHAR(15) NOT NULL,
  CandidateID int NOT NULL,
  PRIMARY KEY (int_id),
  FOREIGN KEY(int_job) REFERENCES Job_Profile(job_id),
  FOREIGN KEY(CandidateID) REFERENCES Candidate(cand_id)
);

CREATE TABLE IF NOT EXISTS Applications
(
  application_id INT NOT NULL,
  application_job_id INT NOT NULL,
  application_date DATE NOT NULL,
  application_cand_id INT NOT NULL,
  PRIMARY KEY (application_id),
  FOREIGN KEY(application_job_id) REFERENCES Job_Profile(job_id),
  FOREIGN KEY(application_cand_id) REFERENCES Candidate(cand_id)
);


CREATE TABLE IF NOT EXISTS Resume 
(
  resume_id INT NOT NULL,
  resume_name VARCHAR(15) NOT NULL,
  resume_qualification VARCHAR(10) NOT NULL,
  Candidate_id INT NOT NULL,
  resume_experience INT NOT NULL,
  PRIMARY KEY (resume_id),
  FOREIGN KEY (Candidate_id) REFERENCES Candidate(cand_id)
);

CREATE TABLE IF NOT EXISTS Resume_resume_skills 
(
  resume_id INT NOT NULL,
  resume_skills VARCHAR(50) NOT NULL,
  PRIMARY KEY (resume_skills, resume_id),
  FOREIGN KEY (resume_id) REFERENCES Resume(resume_id) ON UPDATE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS Candidate_seq
  start 1005
  increment 1
  OWNED BY Candidate.cand_id;

CREATE SEQUENCE IF NOT EXISTS Recruiter_seq
  start 2005
  increment 1
  OWNED BY Recruiter.emp_id;
