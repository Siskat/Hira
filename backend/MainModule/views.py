import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app, db
from MainModule.models import user_session, patient, prescription, doctor, nurse, appointment, notes, record 
import datetime

@app.route("/")
@app.route("/index")
def index():

    return render_template('index.html', sidebar=False)

@app.route("/getAllPatients")
def getAllPatients():
    print("Hi")
    patientList = patient.query.filter_by().all()
    resultList = []
    for u in patientList:
        curr_dic = u.__dict__
        del curr_dic['_sa_instance_state']
        resultList.append(curr_dic)
        print(curr_dic)
        

    return jsonify(resultList)

@app.route("/login")
def login():
    return render_template('login.html', sidebar=False)

@app.route("/nurseLogin")
def nurseLogin():
    session["user"] = "Nurse"
    return render_template('index.html')

@app.route("/doctorLogin")
def doctorLogin():
    session["user"] = "Doctor"
    return render_template('index.html')

@app.route("/logout")
def logout():
    session["user"] = None
    return render_template('login.html')

@app.route("/records")
def records():
    return render_template('records.html', sidebar=False)

@app.route("/appointments")
def appointments():
    return render_template('appointments.html', sidebar=False)

@app.route("/patient_access")
def patient_access():
    return render_template('patient.html', sidebar=False)

@app.route("/patients_list",  methods=['GET'])
def patients_list():
	# test = db.session.query(patient.record_id, patient.full_name)
	return render_template('patients_list.html')

@app.route("/media")
def media():
    return render_template('media.html', sidebar=False)

@app.route("/discharge")
def discharge():
    return render_template('discharge.html', sidebar=False)

@app.route("/patient_history")
def patient_history():
    return render_template('patient_history.html', sidebar=False)
