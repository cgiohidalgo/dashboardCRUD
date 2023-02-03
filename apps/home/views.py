# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

import psycopg2
import psycopg2.extras

@login_required(login_url="/login/")
def index(request):

    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        if load_template == 'personas.html':
            context = personas(request)
        else:
            context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def personas(request):
    datos = ''
    cedula = "".join(request.POST.getlist('cedula'))
    nombre = "".join(request.POST.getlist('nombre'))
    print(nombre)
    
    try:
        idper = request.POST.getlist('editar')[0]
    
        if connection() != None:
            if request.POST.getlist('editar')[0] == "":
                cur = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
                cur.execute("INSERT INTO personas (cedula, nombre) VALUES ('"+cedula+"', '"+nombre+"')")
            else:
                cur = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
                cur.execute("UPDATE personas SET cedula = '"+cedula+"', nombre = '"+nombre+"' WHERE idper = '"+idper+"'")
    except:
        print('No se ejecuto una operación de adicionar o de editar')

    if connection() != None:
        cur2 = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
        cur2.execute("SELECT * FROM personas ORDER BY cedula")
        datos = cur2.fetchall()
    
    context = {"datos": datos, "segment": 'personas'}
    return context

def new_persona(request):
    return render(request, '../templates/home/new_persona.html', context={})

def edit_persona(request, id):
    if connection() != None:
        cur = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM personas WHERE idper='"+str(id)+"'")
        datos = cur.fetchall()
    
    context = {"datos": datos}
    return render(request, '../templates/home/new_persona.html', context=context)


def delete_persona(request, id):
    if connection() != None:
        cur = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
        cur.execute("DELETE FROM personas WHERE idper='"+str(id)+"'")

        cur2 = connection().cursor(cursor_factory= psycopg2.extras.DictCursor)
        cur2.execute("SELECT * FROM personas ORDER BY cedula")
        datos = cur2.fetchall()
    
    context = {"datos": datos}
    return render(request, '../templates/home/personas.html', context=context)

def connection():
    hostname = 'localhost'
    database = 'crud'
    username = 'postgres'
    pwd = 'root'
    port_id = 5432

    conn = None

    try:
        conn = psycopg2.connect (
            host = hostname,
            database = database,
            user = username,
            password = pwd,
            port = port_id
        )
        conn.set_session(autocommit=True)
        
    except Exception as error:
        print('Mensaje de error: ', error)
    
    return conn
