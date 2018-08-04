import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app
<<<<<<< HEAD
import MainModule.models
import datetime

patient1 = patient("John Doe","0000000001", datetime.datetime(1990, 1, 1),80,"Male")
patient2 = patient("John Smith","0000000002", datetime.datetime(1992, 1, 1),90,"Male")
patient3 = patient("Paul Smart","0000000003", datetime.datetime(1997, 1, 1),100,"Male")
patient4 = patient("Myname Jeff","0000000004", datetime.datetime(1995, 1, 1),75,"Male")
patient5 = patient("Mary Bright","0000000005", datetime.datetime(2000, 1, 1),60,"Female")

prescription1 = prescription("0000000001","0000000001",5, datetime.datetime(1960, 1, 1))
prescription2 = prescription("0000000002","0000000002",5, datetime.datetime(8322, 1, 1))
prescription3 = prescription("0000000003","0000000003",5, datetime.datetime(1995, 1, 1))
prescription4 = prescription("0000000004","0000000004",5, datetime.datetime(8192, 1, 1))
prescription5 = prescription("0000000004","0000000005",5, datetime.datetime(2134, 1, 1))

doctor1 = doctor("Gregory House","0000000001", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor2 = doctor("Gregory House","0000000002", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor3 = doctor("Gregory House","0000000003", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor4 = doctor("Gregory House","0000000004", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor5 = doctor("Gregory House","0000000005", datetime.datetime(1980, 5, 6),"Diagnostics")


nurse1 = nurse("Lauren Klein","0000000001", datetime.datetime(1998, 2, 8))
nurse2 = nurse("Lauren Klein","0000000002", datetime.datetime(1998, 2, 8))
nurse3 = nurse("Lauren Klein","0000000003", datetime.datetime(1998, 2, 8))
nurse4 = nurse("Lauren Klein","0000000004", datetime.datetime(1998, 2, 8))
nurse5 = nurse("Lauren Klein","0000000005", datetime.datetime(1998, 2, 8))


appointment1 = appointment("0000000001", datetime.datetime(2018, 2, 5),"0000000001","0000000001","30")
appointment2 = appointment("0000000002", datetime.datetime(2018, 2, 5),"0000000002","0000000002","30")
appointment3 = appointment("0000000003", datetime.datetime(2018, 2, 5),"0000000003","0000000003","30")
appointment4 = appointment("0000000004", datetime.datetime(2018, 2, 5),"0000000004","0000000004","30")
appointment5 = appointment("0000000005", datetime.datetime(2018, 2, 5),"0000000005","0000000005","30")

notes1 = notes("00000000001", datetime.datetime(2018, 5, 8),"Very Sick")
notes2 = notes("00000000002", datetime.datetime(2018, 5, 8),"Very Sick")
notes3 = notes("00000000003", datetime.datetime(2018, 5, 8),"Very Sick")
notes4 = notes("00000000004", datetime.datetime(2018, 5, 8),"Very Sick")
notes5 = notes("00000000005", datetime.datetime(2018, 5, 8),"Very Sick")


record1 = record("0000000001","0000000001","Flu","30", "0000000001")
record2 = record("0000000002","0000000002","Flu","30", "0000000002")
record3 = record("0000000003","0000000003","Flu","30", "0000000003")
record4 = record("0000000004","0000000004","Flu","30", "0000000004")
record5 = record("0000000005","0000000005","Flu","30", "0000000005")


session.add(patient1)
session.add(patient2)
session.add(patient3)
session.add(patient4)
session.add(patient5)
session.add(prescription1)
session.add(prescription2)
session.add(prescription3)
session.add(prescription4)
session.add(prescription5)
session.add(doctor1)
session.add(doctor2)
session.add(doctor3)
session.add(doctor4)
session.add(doctor5)
session.add(nurse1)
session.add(nurse2)
session.add(nurse3)
session.add(nurse4)
session.add(nurse5)
session.add(appointment1)
session.add(appointment2)
session.add(appointment3)
session.add(appointment4)
session.add(appointment5)
session.add(notes1)
session.add(notes2)
session.add(notes3)
session.add(notes4)
session.add(notes5)
session.add(record1)
session.add(record2)
session.add(record3)
session.add(record4)
session.add(record5)

@app.errorhandler(Exception)
def page_not_found(e):
    return render_template('index.html')

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', sidebar=False)

@app.route("/login")
def login():
    return render_template('login.html', sidebar=False)

@app.route("/records")
def records():
    return render_template('records.html', sidebar=False)

@app.route("/appointments")
def appointments():
    return render_template('appointments.html', sidebar=False)

@app.route("/patient")
def patient():
    return render_template('patient.html', sidebar=False)

@app.route("/patients_list",  methods=['GET'])
def patients_list():
	test = session.query(patient.record_id, patient.full_name)
    return render_template('patients_list.html', record_id=test.record_id, patient=test.full_name)

@app.route("/patients_list",  methods=['POST'])
def patients_list():
    return render_template('patients_list.html', sidebar=False)

@app.route("/patients_list")
def patients_list():
    return render_template('patients_list.html', sidebar=False)

@app.route("/media")
def media():
    return render_template('media.html', sidebar=False)

@app.route("/discharge")
def discharge():
    return render_template('discharge.html', sidebar=False)

@app.route("/patient_history")
def patient_history():
    return render_template('patient_history.html', sidebar=False)
