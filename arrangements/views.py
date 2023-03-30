# from shortcuts import View
from django.views import View

from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body> It is {now} now.</body></html>"
    return HttpResponse(html)

def greeting(request,name):
    return HttpResponse(f"<h1> Hello {name}</body.</h1>")

# def year_archive(request,year):
#     print(request)
#     return HttpResponse(f"<h1>{year}</h1>")


class Example(View):
    def get(self, request):
        return HttpResponse('<h1>this is class base view</h1>')

