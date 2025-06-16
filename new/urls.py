from django.urls import path
from .views import *

urlpatterns = [
   path('home/',home),
   path('intro/',intro),
   path('index/',index),
   path('contact/',contact),
   path('about_us/',about_us),
   path('tryy/',tryy)
]