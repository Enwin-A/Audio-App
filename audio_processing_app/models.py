from django.db import models

class AudioFile(models.Model):
    serial_number = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='audio_files/')
    # Add more fields as needed, like speaker information, etc.
    def __str__(self):
        return self.file.name
