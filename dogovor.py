from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
from zipfile import ZipFile


def dogovor(name, fio, date1, date2, choose, birthdate):
    f = fio.split('\r\n')
    print(f)
    zipObj = ZipFile('sample.zip', 'w')
    if choose == "Base":
        for person in f:
                if int(birthdate) < 14:
                    doc = DocxTemplate("zayavleniye.docx")
                    context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose,
                               'Birthdate': birthdate}
                    doc.render(context)
                    doc.save("{}_base.docx".format(person.rstrip()))
                    convert("{}_base.docx".format(person.rstrip()))
                    zipObj.write('{}_base.pdf'.format(person.rstrip()))
                else:
                    doc1 = DocxTemplate("zayavleniye_new.docx")
                    context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose,
                               'Birthdate': birthdate}
                    doc1.render(context)
                    doc1.save("{}_2part_base.docx".format(person.rstrip()))
                    convert("{}_2part_base.docx".format(person.rstrip()))
                    zipObj.write('{}_2part_base.pdf'.format(person.rstrip()))

    else:
        for person in f:
                    if int(birthdate) < 14:
                        doc = DocxTemplate("zayavleniye.docx")
                        context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose,
                                   'Birthdate': birthdate}
                        doc.render(context)
                        doc.save("{}_project.docx".format(person.rstrip()))
                        convert("{}_project.docx".format(person.rstrip()))
                        zipObj.write('{}_project.pdf'.format(person.rstrip()))
                    else:
                        doc1 = DocxTemplate("zayavleniye_new.docx")
                        context = {'Program': name, 'Name': person.rstrip(), 'Date1': date1, 'Date2': date2, 'Choose': choose,
                                   'Birthdate': birthdate}
                        doc1.render(context)
                        doc1.save("{}_2part_base.docx".format(person.rstrip()))
                        convert("{}_2part_base.docx".format(person.rstrip()))
                        zipObj.write('{}_2part_base.pdf'.format(person.rstrip()))



    zipObj.close()