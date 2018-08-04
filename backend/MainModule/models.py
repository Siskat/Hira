from MeetupPoint import app, db
from flask_sqlalchemy import SQLAlchemy
# Creating a model for applications
class user_session(db.Model):
    session_id = db.Column(db.String(13), primary_key=True, default=None)
    date_created = db.Column(db.DateTime)
    no_users = db.Column(db.Integer)


    def __init__(self, unique_id, curr_date):
        self.session_id = unique_id
        self.no_users = 0
        self.date_created = curr_date
    def __str__(self):
        return self.session_id

    def __repr__(self):
        return '<Application %r>' % self.session_id

class patient(db.Model):
    first_name = db.Column(db.String(72))
    last_name = db.Column(db.String(72))
    patient_id = db.Column(db.String(10), primary_key=True)
    date_of_birth = db.Column(db.Date)
    weight = db.Column(db.Float)
    gender = db.Column(db.String(1))
  	prescription_id = db.Column(db.String(10), ForeignKey("prescription.prescription_id"))
    appointment_id = db.column

    def __init__(self, first_name, last_name, patient_id, date_of_birth, weight, gender, prescription_id, appointment_id):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = patient_id
        self.date_of_birth = date_of_birth
        self.weight = weight
        self.gender = gender
        self.prescription_id = prescription_id
        self.appointment_id = appointment_id

class prescription(db.Model):
    prescription_id = db.Column(db.String(10), primary_key=True)
    patient_id = db.Columnd(db.String(10), ForeignKey("patient.patient_id"))
    dosage = db.Column(db.Integer)
    date = db.Column(db.Date)

    def __init__(self, prescription_id, patient_id, dosage, date):
        self.prescription_id = prescription_id
        self.patient_id = patient_id
        self.dosage = dosage
        self.date = date

class doctor(db.Model):
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    doctor_id = db.Column(db.String(10), primary_key=True)
    date_of_birth = db.Column(db.Date)
    specialty = db.Column(db.String(10))

    def __init__(first_name, last_name, doctor_id, date_of_birth, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.doctor_id = doctor_id
        self.date_of_birthday = date_of_birth
        self.specialty = specialty

class nurse(db.Model):
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    nurse_id = db.Column(db.String(10), primary_key=True)
    date_of_birth = db.Column(db.Date)

    def __init__(first_name, last_name, nurse_id, date_of_birth, record_id):
        self.first_name = first_name
        self.last_name = last_name
        self.nurse_id = nurse_id
        self.date_of_birthday = date_of_birth

class appointment(db.Model):
    appointment_id = db.Column(db.String(10))
    date_of_appointment = db.Column(db.Date)
    patient_id = db.Column(db.String(10), ForeignKey("patient.patient_id"))
    doctor_id = db.Column(db.String(10), ForeignKey("doctor.doctor_id"))
    status = db.Column(db.String(20))

    def __init__(self, appointment_id, date_of_appointment, patient_id, doctor_id, status):
        self.appointment_id = appointment_id
        self.date_of_appointment = date_of_appointment
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.status = status


class notes(db.Model):
    notes_id = db.Column(db.String(10)), primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(100))

    def __init__(self, notes_id, date, status):
        self.notes_id = notes_id
        self.date = date
        self.description = description

class record(db.Model):
    record_id = db.Column(db.String(10), primary_key=True)
    appointment_id = db.Column(db.String(10), ForeignKey("appointment.appointment_id"))
    diagnosis = db.Column(db.String(20))
    status = db.Column(db.String(20))
    notes_id = db.Column(db.String(10), ForeignKey("notes.notes_id"))

    def __init__(self, record_id, appointment_id, diagnosis, status, notes_id):
        self.record_id = record_id
        self.appointment_id = appointment_id
        self.diagnosis = diagnosis
        self.status = status
        self.notes_id = notes_id
