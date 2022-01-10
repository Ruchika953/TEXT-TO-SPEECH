# I have made a project text to speech
import time
from gtts import gTTS

def convert_to_audio(text):
	my_audio=gTTS(text)
	my_audio.save('text to audio.mp3')
	
k=input("\033[1;32mwhat you want to make text to speech : ")
print("\033[1;31mGENERATING...")
	
convert_to_audio(k)

print("\033[1;32mAUDIO GENERATED")

time.sleep(1)

print("\033[1;33mGO TO FILE MANAGER")
print("DEVICE STORAGE")
print("Search for")
print("text to audio.mp3")
print("\033[1;31mMADE BY PROGRAMMER O.M")