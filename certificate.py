from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
from zipfile import ZipFile


def certificate(name, fio, date1, date2, choose):
    f = fio.split("\r\n")
    print(f)
    if choose == "ie":
        for person in f:
            doc = DocxTemplate("test_base.docx")
            context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose}
            doc.render(context)
            doc.save("{}_base.docx".format(person.rstrip()))
    else:
        for person in f:
            doc = DocxTemplate("test_project.docx")
            context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose}
            doc.render(context)
            doc.save("{}_project.docx".format(person.rstrip()))
