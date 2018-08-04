import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app
import MainModule.models

@app.route("/")
@app.route("/index")
def index():
        return render_template('index.html', sidebar=False)

@app.route("/login")
def login():
        return render_template('login.html', sidebar=False)

@app.route("/doctor_interface")
def doctor_interface():
        return render_template('doctor_interface.html', sidebar=False)

@app.route("/nurse_interface")
def  nurse_interface():
        return render_template('nurse_interface.html', sidebar=False)

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
