from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Notes
# Create your views here.

def home(request):
    return render(request,'home.html')

def note_list(request):
    note=Notes.objects.all()
    
    context={
        "notes":note
    }
    return render(request,'list.html',context)
def note_create(request):
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      
      if titles == '' or descriptions == '':
         context = {
            "error":" details are required."
         }
         return render(request,'create.html', context)
      Notes.objects.create(title = titles, description = descriptions)
      return redirect('/note')
   return render(request,'create.html')

def note_edit(request, id):
   note = Notes.objects.get(id = id)
   context = {
      "note" : note
   }
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      note.title = titles
      note.descriptioin = descriptions
      note.save()
      return redirect('/note')
      
   return render(request,'edit.html', context)

# def note_delete : create a function to delete a note 
def note_delete(request, id):
    note = get_object_or_404(Notes, id=id)

    if request.method == 'POST':
        note.delete()
        return redirect('/note')  # Replace with your actual note list view name

    return render(request, 'delete.html', {'note': note}) 