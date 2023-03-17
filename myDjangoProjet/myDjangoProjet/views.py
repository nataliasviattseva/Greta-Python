from django.http import HttpResponse
from django.shortcuts import render

import myDjangoProjet.file_manager as FM
import myDjangoProjet.data_manager as DM


def index(request):
    print("\t- Index.htmL -")
    return render(request, 'index.html')


def read_courriel():
    print("- read courriel :")
    file_path = FM.FilePath("./static/txt/courriel.txt")
    print("filePath : " + str(file_path))
    fch = open(str(file_path), 'r')
    courriel = fch.read()
    print("fch courriel : " + courriel)
    return courriel


def check_courriel(request):
    print("- check courriel :")
    rsps = request.GET['mailInput']
    print("rsps : " + rsps)
    courriel = read_courriel()
    if rsps == courriel:
        chk = "OK"
        print("courriel OK")
    else:
        print("courriel NO")
        chk = "NO"
    return render(request, "courriel_check.html", {"rsps": rsps, "chk": chk})


def data_access_sqlite(request):
    data_base = DM.SQLite("../myDjangoProjet/dbGreta78.db")
    data_base.set_connexion()
    data_set = data_base.select_all("tbCartoons")
    print("data_access_sqlite.data_set: " + str(data_set))
    data_base.close_connexion()
    return render(request, 'data_display_sqlite.html', {'data_list': data_set})


def data_access_postgresql(request):
    data_base = DM.PostgreSQL("db_greta78")
    data_base.set_connexion()
    data_set = data_base.select_all("tb_formateur")
    print("data_access_postgresql.data_set: " + str(data_set))
    data_base.close_connexion()
    return render(request, 'data_display_postgresql.html', {'data_list': data_set})


# def check_courriel_avant_model(request):
#     print("- check courriel :")
#     rsps = request.GET['mailInput']
#     print("rsps : " + rsps)
#     courriel = read courriel()
#     if rsps == courriel:
#         print("Courriel OK !")
#         html = """
#                 <h4 style='text-align: center'>""" + rsps + """ : OK</h4>
#                 <br/><br/>
#                 <section id='indexSection' style='text-align: center'>
#                 <a href='http://127.0.0.1:8000/'>index</a>
#                 </section>
#                 """
#     else:
#         print("Courriel NOT OK !")
#         html = """
#                 <h4 style='text-align: center'>""" + rsps + """ : NO</h4>
#                 <br/><br/>
#                 <section id='indexSection' style='text-align: center'>
#                 <a href='http://127.0.0.1:8000/'>index</a>
#                 </section>
#                 """
#     print(html)
#     return HttpResponse(html)


'''
def index_1(request):
    html = """
    <!Doctype html>
    <html lang='fr'>
    <html>
    <head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=width-device-width, initial-scale=1.0'>
    <title>Hello World</title>
    </head>
    <body>
    <h4 style='text-align:center;'>! Hello World !</h4>
    <a href='../bonjour'>bonjour</a>
    </body>
    </html>
    return HttpResponse(html)
'''


def bonjour(request):
    html = """
    <!Doctype html>
    <html lang='fr'>
    <html>
    <head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=width-device-width, initial-scale=1.0'>
    <title>Bonjour Monde</title>
    </head>
    <body>
    <h4 style='text-align:center;'>! Bonjour Monde !</h4>
    <a href='../index'>index</a>
    </body>
    </html>
    """
    return HttpResponse(html)
