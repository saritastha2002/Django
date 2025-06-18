from django.urls import path
from .views import *
urlpatterns = [
    path('note/home/',home),
    path('note/',note_list),
    path('create/',note_create),
    path('note/<id>/edit',note_edit),
    path('note/<id>/delete',note_delete)
]
