from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getNotesList, updateNote, deleteNote, createNote, getNoteDetail

# Create your views here.


@api_view(["GET", "POST"])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


# @api_view(["GET", "POST"])
# def getNote(request, pk):
#     notes = Note.objects.get(id=pk)
#     serializer = NoteSerializer(notes)
#     return Response(serializer.data)


# @api_view(["PUT"])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(["DELETE"])
# def deleteNote(request, pk):
#     Note.objects.get(id=pk).delete()
#     return Response("Note was deleted!!!")

# @api_view(["GET"])
# def getNotes(request):
#     notes = Note.objects.all().order_by("-updated")
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)

# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     serializer = NoteSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
# ------------------------------------------

@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == 'GET':
        ''' This will run when page loads first time '''
        return getNotesList(request)

    if request.method == "POST":
        ''' This will run when user clicks on plus button (This is create API) '''
        return createNote(request)

@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == 'GET':
        ''' This will run when individual note(item) will get clicked '''
        return getNoteDetail(request, pk)

    if request.method == "PUT":
        ''' This will run when user updates the note(item) '''
        return updateNote(request, pk)
        
    if request.method == "DELETE":
        ''' This will run when user clicks on delete note(item) '''
        return deleteNote(request, pk)
    
    