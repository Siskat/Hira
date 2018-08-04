import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from backend import app, db
from MainModule.models import user_session, patient, prescription, doctor, nurse, appointment, notes, record
import datetime

#for recording audio
from time import sleep
import sounddevice as sd
import soundfile as sf
import numpy
import io
import os
import os.path

#Imports the Google Cloud client library
from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# @app.errorhandler(Exception)
# def page_not_found(e):
#     return render_template('index.html')

record1 = record("0000000001", "0000000001", "Flu", "On-Going", "0000000001")
record2 = record("0000000002", "0000000002", "Flu", "Completed", "0000000002")
record3 = record("0000000003", "0000000003", "Flu", "Completed", "0000000003")
record4 = record("0000000004", "0000000004", "Flu", "Completed", "0000000004")

db.session.add(record1)
db.session.add(record2)
db.session.add(record3)
db.session.add(record4)

db.session.commit

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', sidebar=False)

@app.route("/getAllPatients")
def getAllPatients():
    patientList = patient.query.filter_by().all()
    resultList = []
    for u in patientList:
        curr_dic = u.__dict__
        del curr_dic['_sa_instance_state']
        resultList.append(curr_dic)
        #print(curr_dic)

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

@app.route("/records/<string:id>")
def records(id):
    sqlQuery = "SELECT * FROM record JOIN appointment ON appointment.appointment_id = record.appointment_id JOIN patient ON patient.patient_id = appointment.patient_id WHERE record.record_id='" + id + "'"
    record = db.session.execute(sqlQuery)
    return render_template('records.html', record=record)

@app.route("/appointments/<string:id>")
def appointments(id):
    sqlQuery = "SELECT * from appointment JOIN patient WHERE appointment.doctor_id='" + id + "'"
    appointment = db.session.execute(sqlQuery)

    return render_template('appointments.html', appointment=appointment)

@app.route("/patient_access/<string:id>")
def patient_access(id):
    sqlQuery = "SELECT * from patient WHERE patient_id='" + id + "'"
    patient = db.session.execute(sqlQuery)
    for x in patient:
        sqlAppointments = "SELECT * from appointment JOIN record ON appointment.appointment_id = record.appointment_id WHERE appointment.patient_id='" + id + "'"
        appointment = db.session.execute(sqlAppointments)

        return render_template('patient.html', patient=x, appointment=appointment)

@app.route("/patients_list")
def patients_list():
    sqlQuery = "SELECT * from patient"
    patientList = db.session.execute(sqlQuery)
    #print(patientList)
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

@app.route("/record_audio")
def redirect_to_record_audio():
    return render_template('record_audio.html', sidebar=False)

@app.route("/record_audio", methods=['POST'])
def record_audio():
    recording_time = request.form['recording_time']

    try:
        recording_time = int(recording_time)
    except ValueError:
        return render_template('incorrect_time.html', sidebar=False)

    if (recording_time <= 0):
        return render_template('incorrect_time.html', sidebar=False)

    #Setting up audio specifications
    sampling_frequency = 44100
    duration = recording_time #seconds
    channels = 1 #mono audio

    #Setting up defaults as our specifications
    sd.default.samplerate = sampling_frequency
    sd.default.channels = channels

    #prints all available devices for sound input and output
    #> for current input device
    #< for current output device
    #print(sd.query_devices())

    #records for the duration in seconds, and pauses the running of the file while doing so
    #print("Start recording")
    my_recording = sd.rec((duration * sampling_frequency), blocking=True)
    #print("Finished recording")

    #plays back the recording, need to sleep(duration) in order to pause the file while listening
    #not needed to pause but is nice to listen without file running
    #sd.play(my_recording)
    #sleep(duration)

    #need to save the numpy array (thats what my_recording is) as an audio file to be used for google
    #speech to text API
    file_name_wav = 'recordings/output.wav'
    sf.write(file_name_wav, my_recording, sampling_frequency)

    #google speech to text setup and processing
    #Sets up credentials from API key
    credentials = service_account.Credentials.from_service_account_file('recordings/494e73d46153.json')

    #Instantiates a client
    client = speech.SpeechClient(credentials=credentials)

    #Loads the audio into memory
    with io.open(file_name_wav, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,sample_rate_hertz=sampling_frequency,language_code='en-US')

    #Detects speech in the audio file
    response = client.recognize(config, audio)

    #Prints the
    transcript = ""
    for result in response.results:
        transcript = transcript + result.alternatives[0].transcript

#print("Transcript")
#print(transcript)

    return render_template('/record_audio.html', sidebar=False, message=transcript);
