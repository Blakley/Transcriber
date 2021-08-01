'''
dependencies
pip install SpeechRecognition

description
Provide it with the audio file and it'll
output the text to an audio.txt file
maybe run it through the program a few times and select the text that has the most matches: make some type of accuracy measurement

format
WAV: must be in PCM/LPCM format
'''

import pprint
import speech_recognition as sr

r = sr.Recognizer()

jackhammer = sr.AudioFile('../audio/jackhammer.wav')
with jackhammer as source:
	r.adjust_for_ambient_noise(source, duration=0.5)
	audio = r.record(source)

text = r.recognize_google(audio, show_all=True)


pp = pprint.PrettyPrinter(depth=6)
pp.pprint(text)
# print(text)