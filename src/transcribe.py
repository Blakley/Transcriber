import sys
# import pprint
import pyperclip as clipboard
from pydub import AudioSegment
import speech_recognition as sr

class Transcribe():
	def __init__(self):
		self.r = sr.Recognizer()		
		self.name = ""
		self.init()
				
	# starter function
	def init(self):
		line = '---------------------------------'
		print(line)
		print("\tAudio Transcriber")
		print(line + '\n')
		
		# check file extension
		f = open(sys.argv[1], 'r')
		self.file_name = f.name[2:]
		if f.name.endswith('mp3'):
			self.convert()
		
		# save source reference
		self.source = sr.AudioFile(self.file_name)
		f.close()
		self.listen_google()

	# listens and converts audio to text
	def listen_google(self):
		with self.source as source:
			self.r.adjust_for_ambient_noise(source)
			audio = self.r.record(source)

		# self.text = self.r.recognize_google(audio, show_all=True)
		# pp = pprint.PrettyPrinter(depth = 6)
		# pp.pprint(self.text)

		self.text = self.r.recognize_google(audio)
		self.output()

	# converts mp3 audio to wav
	def convert(self):	
		sound = AudioSegment.from_mp3(self.file_name)
		dest = self.file_name[:-4] + '.wav'
		sound.export(dest, format="wav")
		os.remove(self.file_name)
		self.file_name = dest
	
	# outputs text to a file and to clipboard
	def output(self):
		clipboard.copy(self.text)
		audio_file = open(f"{self.file_name[:-4]}-transcription.txt", "w")
		audio_file.write(self.text)
		audio_file.close()

audio = Transcribe()