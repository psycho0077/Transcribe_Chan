from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from pydub import AudioSegment
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded.'})

    audio_file = request.files['audio']
    filename = 'uploaded_audio.mp3'
    audio_file.save(filename)

    # Convert MP3 to WAV using pydub
    try:
        sound = AudioSegment.from_mp3(filename)
        wav_filename = 'converted_audio.wav'
        sound.export(wav_filename, format='wav')

        # Transcribe the WAV file
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)
            transcription = recognizer.recognize_google(audio)

        # Clean up temporary files
        os.remove(filename)
        os.remove(wav_filename)

        return jsonify({'transcription': transcription})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
