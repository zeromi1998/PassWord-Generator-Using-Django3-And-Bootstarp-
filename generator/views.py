from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(req):
    return render(req,'generator/home.html')
def password(req):

    characters=list("abcdefghijklmnopqrstuwxyz")
    length=int(req.GET.get("len",12))
    if req.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUWXYZ"));

    if req.GET.get("numbers"):
        characters.extend(list("0123456789"))


    if req.GET.get("special"):
        characters.extend(list("*+^$#@!"));


    thePassword="";

    for i in range(length):
        thePassword =thePassword + random.choice(characters)
    return render(req,'generator/password.html',{"password":thePassword})

def about(req):
    return render(req,"generator/about.html")