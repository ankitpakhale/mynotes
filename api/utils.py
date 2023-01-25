from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     serializer = NoteSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



def getNoteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return (serializer.data) 

def getNotesList(request):
    notes = Note.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return (serializer.data) 

def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return (serializer.data)

def deleteNote(request,pk):
    Note.objects.get(id=pk).delete()
    return("Note was deleted!!!")


def createNote(request):
    data = request.data
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return (serializer.data)
