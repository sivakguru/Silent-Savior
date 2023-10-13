########################################################

import sounddevice as sd
import numpy as np

# Define the sound detection parameters
sample_rate = 44100  # You may need to adjust this based on your microphone
duration = 10  # Duration of sound detection in seconds
threshold = 0.1  # Adjust this threshold as needed

def sound_callback(indata, frames, time, status):
    if status:
        print(status)
    # Calculate the root mean square (RMS) amplitude of the audio frame
    rms = np.sqrt(np.mean(indata**2))
    print(rms)
    # Check if the RMS amplitude exceeds the threshold
    if rms > threshold:
        print("Fire Alarm Detected!")

# Start the audio stream with the sound detection callback
with sd.IputStream(callback=sound_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))


########################################################

import sounddevice as sd
import numpy as np
import cv2

# Define the sound detection parameters
sample_rate = 44100
duration = 10
threshold = 0.05  # Adjust this threshold as needed

# Define the path to the video file you want to play
video_path = "/Users/skumar763/Documents/dumpyard/vid.mp4"

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
        play_video()

def play_video():
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow("Fire Alarm Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Start the audio stream with the sound detection callback
with sd.InputStream(callback=sound_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))

################################################

# %%

import sounddevice as sd
import numpy as np
import subprocess

# Define the sound detection parameters
sample_rate = 44100
duration = 20
threshold = 0.05  # Adjust this threshold as needed

# Define the URL of the video you want to play
video_url = "/Users/skumar763/Documents/dumpyard/vid.mp4"  # Replace with the actual file path

# Create a flag to indicate whether the alarm has been triggered
alarm_triggered = False


# %%

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

def play_video(video_url):
    command = f"ffplay -noautoexit {video_url}"
    process = subprocess.Popen(command, shell=True)
    # Wait for the process to exit.
    process.wait()


# %%

# Start the audio stream with the sound detection callback
with sd.InputStream(callback=sound_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))


######################################################

# %%
