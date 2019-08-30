from django.contrib.admin.models import DELETION, ADDITION, CHANGE, LogEntry
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.http import request, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import subir
from .models import registro
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import authenticate, AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.admin.models import LogEntry, ADDITION
from django.views import generic
from . import models


# Create your views here.
####DEFINIENDO USUARIO STAFF#####
def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


#####END#######


##########LOGS###########
@login_required(login_url='/logout')
@staff_required(login_url='/forbidden')
def logs(request):
    logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
    logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()
    return render(request, 'registros/logs.html', {'logs': logs})


#########END LOGS########


#######CONFIGURATION LOGIN#########
def login(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                if user.is_superuser:
                    return redirect('logs/')
                if user.boolean==True:
                    return redirect('home/')
                else:

                    return redirect('modificar_cuenta/')
    return render(request, 'registros/index_login.html', {'form': form})


######END CONFIGURATION LOGIN########

#######FUNCTION LOGOUT#######
def logout(request):
    do_logout(request)
    return redirect('/')
######END FUNCTION LOGUT########

######HOME########
@login_required(login_url='/logout')
def home(request):
    return render(request, 'registros/home.html')


######END HOME########

######FUNCTION ADD########
@login_required(login_url='/logout')
def agregar(request):
    add = subir()
    if request.method == "POST":
        add = subir(request.POST, request.FILES)
        if add.is_valid():
            instancia = add.save(commit=False)
            instancia.save()
            LogEntry.objects.log_action(
                user_id=request.user.pk,
                content_type_id=get_content_type_for_model(instancia).pk,
                object_id=instancia.pk,
                object_repr=str(instancia),
                action_flag=ADDITION

            )
            return redirect('/Agregar')
        else:
            HttpResponse('Verifique')
    return render(request, 'registros/agregar.html', {'add': add})


######END FUCTION ADD########

####FUNCTION SHOW#######
@login_required(login_url='/logout')
def regis(request):
    dat = registro.objects.all()
    return render(request, 'registros/registro_usuarios.html', {'dat': dat})


####END FUNCTION SHOW#######


######FUNCTION DELETED########
@login_required(login_url='/logout')
def borrar(request, registro_id):
    instancia = registro.objects.get(id=registro_id)
    instancia.delete()
    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=get_content_type_for_model(instancia).pk,
        object_id=instancia.pk,
        object_repr=str(instancia),
        action_flag=DELETION

    )
    return redirect('/Registro')


######END FUNCTION DELETED########

######FUNCTION EDIT########
@login_required(login_url='/logout')
def editar(request, registro_id):
    instancia = registro.objects.get(id=registro_id)
    form = subir(instance=instancia)
    if request.method == 'POST':
        form = subir(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            LogEntry.objects.log_action(
                user_id=request.user.pk,
                content_type_id=get_content_type_for_model(instancia).pk,
                object_id=instancia.pk,
                object_repr=str(instancia),
                action_flag=CHANGE,
            )
            return redirect('/Registro')
        else:
            print("Error")
    return render(request, 'registros/editar.html', {'form': form})


######END FUNCTION EDIT########

######FUNCTION CHANGE PASSWORD########
@login_required(login_url='/logout')
def modific(request):
    if request.method == "POST":
        mod = PasswordChangeForm(request.user, request.POST)
        if mod.is_valid():
            user = mod.save()
            update_session_auth_hash(request, user)
            user.boolean = True
            user.save()
            messages.success(request, 'Contrasenna Cambiada Correctamente')
            return redirect('/')
        else:
            messages.error(request, 'Algo salio Mal')
    else:
        mod = PasswordChangeForm(request.user)
    return render(request, 'registros/modificar_cuenta.html', {'mod': mod})


######END FUNCTION CHANGE PASSWORD########

######SHOW ACCOUNT#######
@login_required(login_url='/logout')
@staff_required(login_url='/forbidden')
def show_account(request):
    us = User.objects.all()
    return render(request, 'registros/admin/registro_cuentas.html', {'us': us})


######END SHOW ACCOUNT#####

######ADD ACCOUNT#######
@login_required(login_url='/logout')
@staff_required(login_url='/forbidden')
def add_account(request):
    formulario = UserCreationForm(request.POST)
    if request.method == "POST":
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario Agregado')
            return redirect('/add_account')
        else:
            messages.error(request, 'Algo salio Mal')
    return render(request, 'registros/admin/agregar_cuenta.html', {'formulario': formulario})


######END ADD ACCOUNT#######
######FORBIDDEN#######
def forbidden(request):
    return render(request, 'registros/forbidden.html')


###########################ADD AND REMOVE ACTIVE AND STAFF###############################
# Agregando permisos de staff al usuario por el id
def add_staff(request, pk):
    instancia = User.objects.get(pk=pk)
    instancia.is_staff = True
    instancia.save()
    return redirect('/show_account')


# Quitando permisos de staff al usuario por el id
def remove_staff(request, pk):
    instancia = User.objects.get(pk=pk)
    instancia.is_staff = False
    instancia.save()
    return redirect('/show_account')


# Habilitando cuenta
def add_active(request, pk):
    instancia = User.objects.get(pk=pk)
    instancia.is_active = True
    instancia.save()
    return redirect('/show_account')


# Desabilitando cuenta
def remove_active(reques, pk):
    instancia = User.objects.get(pk=pk)
    instancia.is_active = False
    instancia.save()
    return redirect('/show_account')
