import os
import subprocess

url = input("Enter the video URL: ")
audio_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio.mp3")

# Download the video as an mp4 file
subprocess.call(['youtube-dl', '--format', 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4', '-o', 'video.mp4', url])

# Convert the mp4 file to an mp3 file
subprocess.call(['ffmpeg', '-i', 'video.mp4', '-f', 'mp3', audio_file])

# Move the converted mp3 file to the parent directory of the script
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
converted_file = os.path.join(parent_dir, 'audio.mp3')
os.rename(audio_file, converted_file)

# Remove the original video file
os.remove('video.mp4')

print('Conversion completed successfully!')
