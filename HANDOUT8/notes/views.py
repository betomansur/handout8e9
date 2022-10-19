from django.shortcuts import render, redirect
from .models import Note
from django.utils import timezone



def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title= title, content= content)        
        note.save()
        return redirect('index')
    else:
        last_note = Note.objects.order_by()
        print(last_note)
        return render(request, 'notes/index.html', {'notes': last_note.last()})

def delete_post(request):
    id = request.POST.get('id')
    post_to_delete=Note.objects.get(id=int(id))
    post_to_delete.delete()
    return redirect("/") #(#name of the view function that returns your posts page)

def update_post(request, id):
   emp = Note.objects.get(pk = id)
   #you can do this for as many fields as you like
   #here I asume you had a form with input like <input type="text" name="name"/>
   #so it's basically like that for all form fields
   emp.title = request.POST.get('title')
   emp.content = request.POST.get('content')
   emp.save()
   return render(request, 'notes/edit.html', {'note': emp})
