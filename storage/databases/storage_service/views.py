from django.shortcuts import render
from django.http import JsonResponse
from .models import File
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        new_file = File(name=file.name, file_path=file)
        new_file.save()
        return JsonResponse({'message': 'File Uploaded Successfully!'})
    
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def list_files(request):
    files = File.objects.all().values('id', 'name', 'file_path')
    return JsonResponse(list(files), safe=False)
