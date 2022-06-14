from django.http import HttpResponse
from django.db import models
# def index(request):
#     return HttpResponse("Hello world!")
from django.template import loader
from django.shortcuts import render, HttpResponse
from fitz import fitz
# import nameextractor as namext
# import emailextractor as emailext
# import educationextractor as eduext
# import mobilenumberextractor as mobext
# import skillsextractor as skillext
from .educationextractor import extract_candidate_education
from .emailextractor import extract_email
from .mobilenumberextractor import extract_mobile_number
from .models import FilesUpload
from .nameextractor import extract_candidate_name
from .skillsextractor import extract_candidate_skills


def index(request):
    template = loader.get_template('upload.html')
    context = {
        'firstname': 'Aditya Aryaman',
    }
    return HttpResponse(template.render(context, request))


def handle_uploaded_file(filename):
    # doc = fitz.open(filename)
    # text = ""
    # for page in doc:
    #   text = text + str(page.get_text())
    #
    # tx = " ".join(text.split('\n'))
    return filename


def add(request):
    # mymember = Members.objects.get(id=id)
    # template = loader.get_template('update.html')
    # context = {
    #   'mymember': mymember,
    # }
    # return HttpResponse(template.render(context, request))
    template = loader.get_template('upload.html')
    # x = request.POST['first']
    # y = request.POST['last']
    file2 = request.FILES['files']

    # document = FilesUpload.objects.create(file2)
    handle_uploaded_file(file2)
    resumecontent=read_text_from_pdf('a.pdf')
    candidatename=extract_candidate_name(resumecontent)
    mob=extract_mobile_number(resumecontent)
    email=extract_email(resumecontent)
    skill=extract_candidate_skills(resumecontent)
    edu=extract_candidate_education(resumecontent)


    # z = int(x) + int(y)
    context = {
        'resume': resumecontent,
        'candidate_name': candidatename,
        'mob': mob,
        'email': email,
        'skill': skill,
        'edu': edu,

    }
    return HttpResponse(template.render(context, request))

# class FilesUpload(models.Model):
#     files = models.FileField()
def handle_uploaded_file(f):
    with open('a.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def read_text_from_pdf(filename):
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text = text + str(page.get_text())

    tx = " ".join(text.split('\n'))
    return tx