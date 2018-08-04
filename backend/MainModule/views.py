import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app

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

@app.route("/doctor_interface")
def doctor_interface():
        return render_template('doctor_interface.html', sidebar=False)

@app.route("/nurse_interface")
def  nurse_interface():
        return render_template('nurse_interface.html', sidebar=False)

@app.route("/patient")
def patient():
        return render_template('patient.html', sidebar=False)
