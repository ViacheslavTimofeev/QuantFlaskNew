from flask import Flask, request, render_template
from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
import os
import shutil
from zipfile import ZipFile
from os import path
from certificate import certificate
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
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
    return render_template("Index.html")


if __name__ == '__main__':
    app.run(debug=True)
