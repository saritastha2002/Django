

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("welcome")

def intro(request):
   return HttpResponse("Hello i am dia")

def index(request):
   return render(request,'index.html')

# contact, about_us .. use httpresponse
# introduction, ---create a template(intro.html) and show your introduction
def contact(request):
    return HttpResponse("This is the Contact page. You can reach us at stha.sarita.39@example.com.")

def about_us(request):
    return HttpResponse("Welcome to the About Us page")