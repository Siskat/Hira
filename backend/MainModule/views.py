import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app
import MainModule.models
import datetime

patient1 = Patient("John","Doe","0000000001", datetime.datetime(1990, 1, 1),80,"Male","0000000000","0000000000")
patient2 = Patient("John","Smith","0000000002", datetime.datetime(1992, 1, 1),90,"Male","0000000000","0000000000")
patient3 = Patient("Paul","Smart","0000000003", datetime.datetime(1997, 1, 1),100,"Male","0000000000","0000000000")
patient4 = Patient("Myname","Jeff","0000000004", datetime.datetime(1995, 1, 1),75,"Male","0000000000","0000000000")
patient5 = Patient("Mary","Bright","0000000005", datetime.datetime(2000, 1, 1),60,"Female","0000000000","0000000000")

prescription1 = Prescription("0000000001","0000000001",5)
prescription2 = Prescription("0000000002","0000000002",5)
prescription3 = Prescription("0000000003","0000000003",5)
prescription4 = Prescription("0000000004","0000000004",5)
prescription5 = Prescription("0000000004","0000000005",5)

doctor1 = Doctor("Gregory","House","0000000001", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor2 = Doctor("Gregory","House","0000000002", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor3 = Doctor("Gregory","House","0000000003", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor4 = Doctor("Gregory","House","0000000004", datetime.datetime(1980, 5, 6),"Diagnostics")
doctor5 = Doctor("Gregory","House","0000000005", datetime.datetime(1980, 5, 6),"Diagnostics")


nurse1 = Nurse("Lauren","Klein","0000000001", datetime.datetime(1998, 2, 8))
nurse2 = Nurse("Lauren","Klein","0000000002", datetime.datetime(1998, 2, 8))
nurse3 = Nurse("Lauren","Klein","0000000003", datetime.datetime(1998, 2, 8))
nurse4 = Nurse("Lauren","Klein","0000000004", datetime.datetime(1998, 2, 8))
nurse5 = Nurse("Lauren","Klein","0000000005", datetime.datetime(1998, 2, 8))


appointment1 = Appointment("0000000001", datetime.datetime(2018, 2, 5),"0000000001","0000000001","30")
appointment2 = Appointment("0000000002", datetime.datetime(2018, 2, 5),"0000000002","0000000002","30")
appointment3 = Appointment("0000000003", datetime.datetime(2018, 2, 5),"0000000003","0000000003","30")
appointment4 = Appointment("0000000004", datetime.datetime(2018, 2, 5),"0000000004","0000000004","30")
appointment5 = Appointment("0000000005", datetime.datetime(2018, 2, 5),"0000000005","0000000005","30")

notes1 = Notes("00000000001", datetime.datetime(2018, 5, 8),"Very Sick")
notes2 = Notes("00000000002", datetime.datetime(2018, 5, 8),"Very Sick")
notes3 = Notes("00000000003", datetime.datetime(2018, 5, 8),"Very Sick")
notes4 = Notes("00000000004", datetime.datetime(2018, 5, 8),"Very Sick")
notes5 = Notes("00000000005", datetime.datetime(2018, 5, 8),"Very Sick")


record1 = Record("0000000001","0000000001","Flu","30", "0000000001")
record2 = Record("0000000002","0000000002","Flu","30", "0000000002")
record3 = Record("0000000003","0000000003","Flu","30", "0000000003")
record4 = Record("0000000004","0000000004","Flu","30", "0000000004")
record5 = Record("0000000005","0000000005","Flu","30", "0000000005")


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

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', sidebar=False)

@app.route("/login")
def login():
    return render_template('login.html', sidebar=False)

@app.route("/appointments")
def appointments():
    return render_template('appointments.html', sidebar=False)

@app.route("/patient")
def patient():
    return render_template('patient.html', sidebar=False)

@app.route("/patients_list",  methods=['GET', 'POST'])
def patients_list():
    return render_template('patients_list.html', sidebar=False)

@app.route("/retrieveSearch",  methods=['GET', 'POST'])
def retrieveSearch():
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
