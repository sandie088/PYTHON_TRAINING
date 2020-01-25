from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import testModelView


def hello(request):
    time = datetime.now().time()
    return render(request, "hello.html", {"time": time})


def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")


def article(request, articleId):
    text = "Displaying article Number : %s" % articleId
    return HttpResponse(text)


def dbops(request):
    # adding entry here

    testentry = testModelView(
        website="www.google.com", mail="test@google.com", name="test", phonenumber="1234567890"
    )

    testentry.save()

    # reading entries
    entries = testModelView.objects.all()
    outputstring = "Printing all entries from testModelView: <br>"

    for entry in entries:
        outputstring += entry.name + "<br>"

    # Read entry based on criteria
    test = testModelView.objects.get(name="test")
    outputstring += "Printing one entry <br>"
    outputstring += test.name

    # Update operation
    testentry = testModelView(
        website="www.google.com", mail="tester@google.com", name="tester", phonenumber="0987654321"
    )

    testentry.save()
    outputstring += "Updating entry <br>"

    testentry = testModelView.objects.get(name='tester')
    testentry.name = 'testergoogle'
    testentry.save

    return HttpResponse(outputstring)


def showallentries(request):
    entries = testModelView.objects.all()
    outputstring = "Printing all entries from db <br>"

    for entry in entries:
        outputstring += "name: " + entry.name + " mail: " + entry.mail + " website: " + entry.website + " phone number: " + str(entry.phonenumber) + "<br>"

    return HttpResponse(outputstring)
