from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def hello(request, imie):
    return render(request, 'examples/hello.html', {"imie": imie})

# def hello(request, imie):
#     text = f"Hello {imie}"
#     return HttpResponse(text)

def about(request):
    return HttpResponse("Test website")

def cool_text(request, user_text):
    text = f"@--> {user_text.upper()} <-----"
    return HttpResponse(text)

def calc(request, operation, num1, num2):
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Błąd dzielenia przez zero"
    elif operation == "mul":
        result = num1 * num2
    else:
        result = "Nieznane działanie"
    return HttpResponse(result)

def dogs(request):
    dog_list = Dog.objects.all()
    # return HttpResponse(", ".join(str(d) for d in dog_list))
    return render(request, 'examples/dogs.html', {"dogs": dog_list})

def dog(request, id):
    dog = Dog.objects.get(id=id)
    return render(request, 'examples/dog.html', {"dog": dog})