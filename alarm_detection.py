import sounddevice as sd
import numpy as np
import subprocess
import os

# Define the sound detection parameters
sample_rate = 44100
duration = 20
threshold = 0.1  # Adjust this threshold as needed

file_location = 'fire_alram_media/sign_language.mp4'
# Define the URL of the video you want to play
video_url = os.path.expanduser(f'{file_location}')

# Create a flag to indicate whether the alarm has been triggered
alarm_triggered = False

def sound_callback(indata, frames, time, status):
    global alarm_triggered
    if status:
        print(status)
    rms = np.sqrt(np.mean(indata**2))
    print(rms)
    if rms > threshold and not alarm_triggered:
        print("Fire Alarm Detected!")
        alarm_triggered = True
        play_video(video_url)
        raise StopIteration
        raise SystemExit

def play_video(video_url):
    command = f"ffplay -noautoexit {video_url}"
    process = subprocess.Popen(command, shell=True)
    # Wait for the process to exit.
    process.wait()

# Start the audio stream with the sound detection callback
with sd.InputStream(callback=sound_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))
