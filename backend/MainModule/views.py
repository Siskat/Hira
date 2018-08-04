import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app, db
from MainModule.models import patient, prescription, doctor, nurse, appointment, notes, record
import datetime

# @app.errorhandler(Exception)
# def page_not_found(e):
#     return render_template('index.html')

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

@app.route("/patients_list")
def patients_list():
    sqlQuery = "SELECT * from patient"
    patientList = db.session.execute(sqlQuery)
    print(patientList)
    return render_template('patients_list.html', patientList=patientList)

@app.route("/media")
def media():
    return render_template('media.html', sidebar=False)

@app.route("/discharge")
def discharge():
    return render_template('discharge.html', sidebar=False)

@app.route("/patient_history")
def patient_history():
    return render_template('patient_history.html', sidebar=False)
