from django.db import models
class File(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
