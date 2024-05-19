from django import forms
# from .models import AudioFile

# class AudioUploadForm(forms.ModelForm):
#     class Meta:
#         model = AudioFile
#         fields = ['file']


class AudioUploadForm(forms.Form):
    audio_file = forms.FileField(label='Select an MP3 file')