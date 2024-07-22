import pyaudio
import wave
import threading
import time
import os
from openai import OpenAI

def record_audio():
    print("Welcome to the recording studio! We'll transcribe your recording up to a max length of 15 seconds.")
    input("Press enter when ready to record> ")

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording. Press enter to stop.")
    frames = []

    is_recording = True
    start_time = time.time()

    def record():
        while is_recording:
            data = stream.read(CHUNK)
            frames.append(data)

    # Start recording in a separate thread
    record_thread = threading.Thread(target=record)
    record_thread.start()

    # Wait for user to press enter
    input()

    # Stop recording
    is_recording = False
    record_thread.join()

    duration = time.time() - start_time
    print(f"Recording stopped. Duration: {duration:.2f} seconds")

    stream.stop_stream()
    stream.close()
    p.terminate()

    filename = "_transcription.wav"
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    if duration <= 15:
        transcribe_audio(filename)
        os.remove(filename)
    else:
        print("Recording is longer than 15 seconds.")

def transcribe_audio(filename):
    client = OpenAI()
    
    with open(filename, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    print("\nHere's what you said:")
    print(transcription.text)

if __name__ == "__main__":
    record_audio()
