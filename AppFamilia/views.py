from pyexpat import model
from datetime import datetime
from django.shortcuts import render
from AppFamilia.models import Mascota, Persona



# Create your views here.

def padre(request):


    padre=Persona(name= "Oscar", 
    surname= "Rimmele", 
    fecha_nacimiento= "1975-11-21", 
    profesion="Mecanico", 
    email="OscarRimmele@hotmail.com", 
    phone=1527493716)
    padre.save()
    contexto={'padre': padre}
    return render(request, 'template1.html', contexto)

def madre(request):
    
    madre=Persona(name= "Elvira", 
    surname= "Barraza", 
    fecha_nacimiento= "1972-1-3", 
    profesion="Profesora", 
    email="ElviraBarraza@hotmail.com", 
    phone=1517433996)
    madre.save()
   
    contexto={'madre': madre}
    
    return render(request, 'template2.html', contexto)

def hermano(request):
    hermana=Persona(name= "Jacinta", 
    surname="Rimmele", 
    fecha_nacimiento= "2005-9-16", 
    profesion="Estudiante de escuela", 
    email= "JacintaRimmele@hotmail.com", 
    phone= 1528438821)
    hermana.save()
    
    contexto={'hermana': hermana}
    
    return render(request, 'template3.html', contexto)
