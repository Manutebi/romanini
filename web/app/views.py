from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'home.html')

def checklist(request):
    return render(request, 'checklist.html')

def otmecanicos(request):
    return render(request, 'otmecanicos.html')

def alertas(request):
    return render(request, 'alertas.html')

def solicitud(request):
    return render(request, 'solicitud.html')

def login(request):
    return render(request, 'login.html')

####################################################################
################   CREACION Y LISTADOS #############################
####################################################################



def crear_check(request):
    return render(request, 'checklist/crear_check.html')

def listar_check(request):
    return render(request, 'checklist/listar_check.html')


########################################################
def crear_alerta(request):
    data = {
        'alerta': AlarmaForm()
    }

    if request.method == 'POST':
        formulario = AlarmaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to="alertas")

        else:
            messages.error(request, "No se pudo agregar Correctamente")

    return render(request, 'alertas/crear_alerta.html', data)
    
def listar_alerta(request):
    alertas = Alerta.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(alertas, 6)
        alertas = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity':alertas,
        'paginator':paginator
    }
    return render(request, 'alertas/listar_alerta.html', data)
########################################################


def crear_solicitud(request):
    data = {
        'solicitud': SolicitudForm()
    }

    if request.method == 'POST':
        formulario1 = SolicitudForm(data=request.POST)
        if formulario1.is_valid():
            formulario1.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to="solicitud")

        else:
            messages.error(request, "No se pudo agregar Correctamente")
    
    return render(request, 'solicitud/crear_solicitud.html', data)

def listar_solicitud(request):
    solicitud = Solicitud.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(solicitud, 6)
        solicitud = paginator.page(page)

    except:
        raise Http404


    data = {
        'entity':solicitud,
        'paginator':paginator
    }
    return render(request, 'solicitud/listar_solicitud.html',data)

##############################################################

def crear_ot(request):
    return render(request, 'otmecanicos/crear_ot.html')

def listar_ot(request):
    return render(request, 'otmecanicos/listar_ot.html')

##############################################################

def crear_check(request):
    data = {
        'check': CheckForm()
    }

    if request.method == 'POST':
        formulario = CheckForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to="checklist")

        else:
            messages.error(request, "No se pudo agregar Correctamente")
    
    return render(request, 'checklist/crear_check.html', data)

def listar_check(request):
    check = Checklist.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(check, 6)
        check = paginator.page(page)

    except:
        raise Http404


    data = {
        'entity':check,
        'paginator':paginator
    }
    return render(request, 'checklist/listar_check.html',data)