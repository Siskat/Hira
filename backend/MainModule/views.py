import json, urllib
import requests
import random, string
import urllib.request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash

@app.errorhandler(Exception)
def page_not_found(e):
    flash("Page not found")
    return render_template('index.html')


@app.route("/")
@app.route("/index")
def index():
        return render_template('index.html', sidebar=False)
