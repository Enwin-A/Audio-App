from django.shortcuts import render
import os
from django.conf import settings
from .models import AudioFile
from core.sentiment_analysis import main as sentiment_analysis_main
from core.speech_to_text import main as speech_to_text
from .forms import AudioUploadForm

def upload_and_process_audio(request):
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']
            audio = AudioFile.objects.create(file=audio_file)
            # audio_file="C:/Users/enwin/Enwin Code/audio_processing_app/media/audio_files/"+str(audio_file)
            file_path = os.path.join(settings.MEDIA_ROOT, audio.file.name)
            file_path = str(file_path)
            if "\\" in file_path:
                file_path = file_path.replace("\\", "/")
            # file_path = "/media/audio_files/"+str(audio_file)
            print(file_path)
            text = speech_to_text(file_path)
            if text is None:
                return render(request, 'upload.html', {'form': form, 'error': 'Error processing the audio file. Please try again.'})
            sentiment_analysis = sentiment_analysis_main(text)
            
            return render(request, 'results.html', {'text': text, 'sentiment_analysis': sentiment_analysis})
    else:
        form = AudioUploadForm()
    return render(request, 'upload.html', {'form': form})
