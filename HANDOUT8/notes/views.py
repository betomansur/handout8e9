from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title= title, content= content)        
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

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

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()

    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)
@api_view(['GET'])
def api_note_all(request):
    try:
        note = Note.objects.all()
    except:
        raise Http404()
    serialized_note = NoteSerializer(note, many=True)
    return Response(serialized_note.data)
