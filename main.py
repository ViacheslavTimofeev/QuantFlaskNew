from flask import Flask, request, render_template
from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
import os
import shutil
from zipfile import ZipFile
from os import path
from certificate import certificate
from dogovor import dogovor
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/index', methods=['post', 'get'])
def index():
    d1 = 0
    d2 = 0
    if request.method == 'POST':
        name = request.form.get('program')
        fio = request.form.get('FullName')
        d1 = request.form.get("date1")
        d2 = request.form.get("date2")
        choose = request.form.get("browser")
        certificate(name, fio, d1, d2, choose)
    return render_template("certificate1.html")


@app.route('/dogovor', methods=['post', 'get'])
def randomf():
    d1 = 0
    d2 = 0
    if request.method == 'POST':
        name = request.form.get('program')
        fio = request.form.get('FullName')
        d1 = request.form.get("date1")
        d2 = request.form.get("date2")
        choose = request.form.get("browser")
        dogovor(name, fio, d1, d2, choose)
    return render_template("dogovor1.html")


if __name__ == '__main__':
    app.run(debug=True)

app.run(debug=True, host='0.0.0.0')