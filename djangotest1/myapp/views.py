from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    time = datetime.now().time()
    return render(request, "hello.html", {"time": time})


def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")


def article(request, articleId):
    text = "Displaying article Number : %s" % articleId
    return HttpResponse(text)
