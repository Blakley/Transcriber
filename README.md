# Transcriber

Audio transcriber tool

## Features

* Audio transcription
* Saves output to a txt file `{my_audio_file}-transcription.txt` as well as the clipboard
* Supports both mp3 and wav audio files

## Dependencies

Have both ffmpeg and pip installed on your system then install the following using pip
```
$ pip install pydub
$ pip install ffmpeg
$ pip install pyperclip
$ pip install SpeechRecognition
```

## Usage

Run the tool by providing it with an audio file:

```
$ python transcribe.py my_audio_file.wav
```
