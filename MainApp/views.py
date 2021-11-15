from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def main_test(request):
    return HttpResponse("main test.")

def main_view(request):
    return HttpResponse("main veiw.")

def default_page(request):
    return HttpResponse("<h1>Default page.<h1>")