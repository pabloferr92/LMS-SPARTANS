from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:

        if(request.POST.get("senha") == "teste123"):
            print("Usuário " + request.POST.get("email") + " entrou com sucesso!")
            return render(request, "index.html")
        else:
            print("Usuário " + request.POST.get("email") + " digitou a senha errada!")
            return render(request, "login.html")

def novocurso(request):
    return render(request, "novocurso.html")
