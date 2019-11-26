import speech_recognition as sr
import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something, im listening')
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return said


text = get_audio()

if 'hello' in text:
    speak('hello, how are you?')
elif 'what is your name' in text:
    speak('my name is Jarvis')
