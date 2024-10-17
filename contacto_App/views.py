from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactoForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form=ContactoForm(data=request.POST)


        if form.is_valid():
            # opción más segura (nombre=form.cleaned_data['Nombre'])
            # nombre=request.POST.get('Nombre')
            # apellido=request.POST.get('Apellido')
            # email=request.POST.get('Email') 
            # edad=request.POST.get('Edad')
            # mensaje=request.POST.get('Mensaje')
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            edad = form.cleaned_data['edad']
            mensaje = form.cleaned_data['mensaje']

            asunto = f'Nuevo mensaje de contacto de {nombre} {apellido}'
            mensaje_email = f'Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nEdad: {edad}\nMensaje: {mensaje}'
            email_origen = settings.EMAIL_HOST_USER
            email_destino = ['colombatocolegio@gmail.com']  # Pon aquí el correo al que quieres enviar el mensaje

            send_mail(asunto, mensaje_email, email_origen, email_destino, fail_silently=False)

            # GUARDA... que no es contacto.html/?valido... es contacto/?valido !!!!!!
            return redirect("/contacto/?valido")
    else:
        form=ContactoForm()

    return render(request,'contacto/contacto.html',{'form':form})
