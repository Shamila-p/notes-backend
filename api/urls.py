from django.urls import path
from . import views


urlpatterns = [
    path('add-note',views.AddNote.as_view()),
    path('get-notes',views.GetNotes.as_view()),
    path('edit-note/<int:note_id>',views.EditNote.as_view()),
    path('delete-note/<int:note_id>',views.DeleteNote.as_view())
]