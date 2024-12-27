from django.urls import path
from .views import upload_file, list_files

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('files/', list_files, name='list_files'),
]
