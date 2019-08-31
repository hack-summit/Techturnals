create TABLE Tab
(
    name varchar(111)
);


INSERT INTO
  "tab"
    (name)
VALUES
    ('Prefernce');

create TABLE Prefernce
(
    id int(111) PRIMARY KEY,
    FromValue varchar(111),
    ToValue varchar(111),
);

INSERT INTO
  "tab"
    (name)
VALUES
    ('Dept');

create TABLE Dept
(
    id int(111),
    name varchar(111)
);

INSERT INTO
  "tab"
    (name)
VALUES
    ('Doctor');

create TABLE Doctor
(
    id int(111) PRIMARY KEY,
    name varchar(111),
    DOB datetime,
    BG varchar(4),
    DeptID int(111) ,
    Seniority int(111),
    ImgLink varchar(250),
    LoginToken varchar(111),
    UserName varchar(111),
    password varchar(111),
    LastLogin datetime,
    LastLogout datetime,
    Sex varchar(111),
    Degree varchar(111),
    FOREIGN KEY (DeptID) REFERENCES Dept(id)
);

INSERT INTO
  "tab"
    (name)
VALUES
    ('Nurse');

create TABLE Nurse
(
    id int(111) PRIMARY KEY,
    name varchar(111),
    DOB datetime,
    BG varchar(4),
    DeptID int(111) ,
    ImgLink varchar(250),
    LoginToken varchar(111),
    UserName varchar(111),
    password varchar(111),
    LastLogin datetime,
    LastLogout datetime,
    Sex varchar(111),
    DoctorID int(111),
    Degree varchar(111),
    FOREIGN KEY (DeptID) REFERENCES Dept(id),
    FOREIGN KEY(DoctorID) REFERENCES Doctor(id)
);

INSERT INTO
  "tab"
    (name)
VALUES
    ('Patient');

create TABLE Patient
(
    id int(111) PRIMARY KEY,
    name varchar(111),
    DOB datetime,
    BG varchar(4),
    Height double(7,2),
    Weight double(7,2),
    Sex varchar(111),
    LastCheckDate datetime
    );

INSERT INTO
 "tab"
    (name)
VALUES
    ('AttendanceN');

create table AttendanceN
(
    id int(111) PRIMARY KEY,
    NurseID int(111),
    DateIn datetime,
    DateOut datetime,
    FOREIGN KEY (NurseID) REFERENCES Nurse(id)
);

INSERT INTO
 "tab"
    (name)
VALUES
    ('AttendanceD');

create table AttendanceD
(
    id int(111) PRIMARY KEY,
    DoctorID int(111),
    DateIn datetime,
    DateOut datetime,
    FOREIGN KEY (DoctorID) REFERENCES Doctor(id)
);

INSERT INTO
 "tab"
    (name)
VALUES
    ('Appointments');

create table Appointments
(
    id int(111) PRIMARY KEY,
    PatientID int(111),
    DoctorID int(111),
    DateIn datetime,
    DateOut datetime,
    PatientSno int(111),
    Intensity int(111),
    FOREIGN KEY (PatientID) REFERENCES Patient(id),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(id)
);

INSERT INTO
 "tab"
    (name)
VALUES
    ('VisitD');

create table VisitD
(
    id int(111) PRIMARY KEY,
    AppointmentID int(111),
    DoctorID int(111),
    DateNow datetime,
    Description varchar(111),
    Intensity int(111),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(id),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(id)
);

INSERT INTO
 "tab"
    (name)
VALUES
    ('VisitN');

create table VisitN
(
    id int(111) PRIMARY KEY,
    AppointmentID int(111),
    NurseID int(111),
    DateNow datetime,
    Description varchar(111),
    Intensity int(111),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(id),
    FOREIGN KEY (NurseID) REFERENCES Nurse(id)
);

