TRUNCATE TABLE Login cascade;

INSERT into Login values ('alpha_login','alpha_pwd','R');
INSERT into Login values ('beta_login','beta_pwd','R');
INSERT into Login values ('arjun_login','arjun_pwd','C');
INSERT into Login values ('barsha_login','barsha_pwd','C');
INSERT into Login values ('chandran_login','chandran_pwd','C');
INSERT into Login values ('divya_login','divya_pwd','C');

truncate table candidate cascade;
INSERT into Candidate values (1001, 'arjun@gmail.com','arjun house address','Arjun', 9845011111,'2001-01-01','M','arjun_login');
INSERT into Candidate values (1002, 'barsha@gmail.com','barsha house address','barsha', 9845022222,'2001-02-02','F','barsha_login');
INSERT into Candidate values (1003, 'chandran@gmail.com','chandran house address','chandran', 9845033333,'2001-03-03','M','chandran_login');
INSERT into Candidate values (1004, 'divya@gmail.com','divya house address','divya', 9845044444,'2001-03-03','F','divya_login');

truncate table recruiter cascade;
INSERT into Recruiter values ('Alpha technologies',2001, 'Bangalore',08027271111,'alphatech@gmail.com','alpha_login');
INSERT into Recruiter values ('Beta digital',2002, 'Chennai',04427272222,'betadigital@gmail.com','beta_login');

truncate table Job_Profile cascade;
insert into Job_Profile values (1,'Developer','FTE','Full stack engineer',2001,'BTech',2, 'JAVA');
insert into Job_Profile values (2,'Project Manager','FTE','Manage Business Projects',2001,'MBA',8,'Project Management');
insert into Job_Profile values (3,'Tester','PTC','Conduct Unit, Performance, system testing',2002,'BE',1,'Unit testing');
insert into Job_Profile values (4,'SWE Architect','FTC','Design software architecture',2002,'BTech',15,'Software Architecture');

truncate table job_profile_job_location cascade;
insert into Job_Profile_job_location values (1,'Bangalore',5);
insert into Job_Profile_job_location values (1,'Mumbai',4);
insert into Job_Profile_job_location values (2,'Pune',6);
insert into Job_Profile_job_location values (3,'Gujarat',7);
insert into Job_Profile_job_location values (3,'Kolkata',3);
insert into Job_Profile_job_location values (4,'Delhi',2);

truncate table interview cascade;
insert into Interview values (101,1,'2018-10-01','SELECTED','It went well','Online',1001);
insert into Interview values (102,2,'2019-10-05','REJECTED','poor communication','Online',1002);
insert into Interview values (103,3,'2021-10-27','SELECTED','Good attitude and knowledge','Online',1003);
insert into Interview values (104,4,'2021-10-28','REJECTED','Poor skills','Offline',1004);

truncate table applications cascade;
insert into Applications values (10001,1,'2021-08-01',1001);
insert into Applications values (20002,2,'2021-08-01',1002);
insert into Applications values (30003,3,'2021-08-10',1003);
insert into Applications values (40004,4,'2021-08-20',1004);

truncate table resume cascade;
insert into Resume values (10011,'Arjun','BTech',1001,2);
insert into Resume values (10022,'Barsha','MBA',1002,10);
insert into Resume values (10033,'chandran','BE',1003,3);
insert into Resume values (10044,'divya','BTech',1004,20);

truncate table resume_resume_skills cascade;
insert into Resume_resume_skills values (10011,'MERN stack');
insert into Resume_resume_skills values (10011,'JAVA');
insert into Resume_resume_skills values (10022,'Project management');
insert into Resume_resume_skills values (10022,'Risk management');
insert into Resume_resume_skills values (10033,'Unit testing');
insert into Resume_resume_skills values (10033,'Debugging');
insert into Resume_resume_skills values (10044,'Software Architecture');