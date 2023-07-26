from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NotesSerializer
from rest_framework import status
from .models import Notes
from rest_framework.permissions import AllowAny


class AddNote(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        print(request.data)
        serializer=NotesSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_200_OK)
        
class GetNotes(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        notes=Notes.objects.all()
        serializer=NotesSerializer(notes,many=True)
        print(serializer.data)
        return Response(serializer.data,status = status.HTTP_200_OK)

class EditNote(APIView):
    permission_classes = [AllowAny]
    def post(self,request,note_id):
        print(note_id)
        note=Notes.objects.get(id=note_id)
        serializer=NotesSerializer(data=request.data,instance=note)
        if serializer.is_valid():
            serializer.save()
            return Response( status = status.HTTP_200_OK)
        
class DeleteNote(APIView):
    permission_classes = [AllowAny]
    def post(self,request,note_id):
        note=Notes.objects.get(id=note_id)
        note.delete()
        return Response({"message": "successfully deleted"}, status = status.HTTP_200_OK)
