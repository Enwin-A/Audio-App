# main.py (python example)

import os
# from dotenv import load_dotenv
from dotenv import dotenv_values
import json
from core.sentiment_analysis import main as sentiment_analysis_main
from django.conf import settings

'''
The most common audio formats and encodings we support 
include mp3, mp4, mp2, aac, wav, flac, pcm, m4a, ogg, opus, and webm,
So feel free to adjust the `MIMETYPE` variable as needed
'''

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)


# load_dotenv()

# Path to the audio file
# AUDIO_FILE = "C:/Users/enwin/Downloads/call_center_mp3.mp3"
# Load environment variables from info.env


def speech_to_text(file_path):
    env_path = "info.env"
    general_path = os.path.join(settings.BASE_DIR,"core")
    general_path = str(general_path)
    if "\\" in general_path:
        general_path = general_path.replace("\\", "/")
    print(general_path)
    print("printing general path")
    print(general_path)


    env_path = os.path.join(settings.BASE_DIR,"core",env_path)
    env_path = str(env_path)
    if "\\" in env_path:
        env_path = env_path.replace("\\", "/")
    print(env_path)
    env_vars = dotenv_values(env_path)
    API_KEY = env_vars.get("DG_API_KEY")
    print(API_KEY)
    try:
        
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)
        print(file_path)
        with open(file_path, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        # options = PrerecordedOptions(
        #     model="nova-2",
        #     smart_format=True,

        #     "punctuate"= True,
        #     "diarize"= True,
        #     "model" 'general',
        #     "tier": 'nova'
        # )

        options = {
            "punctuate": True,
            "diarize": True,
            "model": 'general',
            "tier": 'nova',
            # "smart_format": True
        }
        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        # response = deepgram.transcription.sync_prerecorded(source, options)

        # STEP 4: Print the response
        response = response.to_json(indent=4)
        general_path = general_path+"/response.json"
        with open(general_path, "w") as file:
            file.write(response) 
        # print(response)
        return response

    except Exception as e:
        print(f"Exception: {e}")

def create_transcript(response):
    general_path = os.path.join(settings.BASE_DIR,"core")
    general_path = str(general_path)
    if "\\" in general_path:
        general_path = general_path.replace("\\", "/")
    print("creating transcript")
    lines = []
    TAG = 'Speaker '
    words = response["results"]["channels"][0]["alternatives"][0]["words"]
    # print(response["results"]["channels"][0]["alternatives"][0]["words"])
    # print(response["results"]["channels"]
    curr_speaker = 0
    curr_line = ''
    for word_struct in words:
      word_speaker = word_struct["speaker"]
      word = word_struct["punctuated_word"]
      if word_speaker == curr_speaker:
        curr_line += ' ' + word
      else:
        tag = TAG + str(curr_speaker) + ':'
        full_line = tag + curr_line + '\n'
        curr_speaker = word_speaker
        lines.append(full_line)
        curr_line = ' ' + word
    lines.append(TAG + str(curr_speaker) + ':' + curr_line)
    general_path = general_path+"/output_transcript.txt"
    with open(general_path, 'w') as f:
      for line in lines:
        f.write(line)
        f.write('\n')
    # print(lines)
    with open(general_path, "r") as file:
        lines = file.read()
    return lines

# def print_transcript():
#   for filename in os.listdir(DIRECTORY):
#     if filename.endswith('.json'):
#       output_transcript = os.path.splitext(filename)[0] + '.txt'
#       create_transcript(filename, output_transcript)

# print_transcript()



def main(file_path):

    print(file_path)
    # if os.path.exists(response_file) and os.path.getsize(response_file) == 0:
    #     print("File is empty")
    #     speech_to_text(file_path)
    speech_to_text(file_path)
    response_file = "response.json"
    response_path = os.path.join(settings.BASE_DIR,"core",response_file)
    response_path = str(response_path)
    if "\\" in response_path:
        response_path = response_path.replace("\\", "/")
    print(response_path)
    with open(response_path, "r") as file:
        response = json.load(file)
    transcript = create_transcript(response)
    print(transcript)
    return transcript
    # sentiment_result = sentiment_analysis_main(transcript)
    # print(sentiment_result)
    # return transcript, sentiment_result

    


if __name__ == "__main__":
    main()
