# Importing all the necessary modules
from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
import speech_recognition as sr

# Creating the python text to speech and speech to text functions
def speak(text: str):
    engine = pyttsx3.init()

    engine.setProperty('rate', 10)
    engine.setProperty('volume', 100)

    engine.say(text)
    engine.runAndWait()


def record():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-IN")
        except Exception as e:
            showinfo(title='Error!', message=e)
            speak("I am sorry, I did not get that, but could you please repeat that")

            return "Nothing"
        return query


# Creating the main TTS and STT functions and the instruction functions
def TTS():
    tts_wn = Toplevel(root)
    tts_wn.title('Text-to-Speech Converter')
    tts_wn.geometry("350x250")
    tts_wn.configure(bg='Brown')

    Label(tts_wn, text='Text-to-Speech Converter', font=("Comic Sans MS", 15), bg='Brown').place(x=50)

    text = Text(tts_wn, height=5, width=30, font=12)
    text.place(x=7, y=60)

    speak_btn = Button(tts_wn, text='Record', bg='LightCoral', command=lambda: speak(str(text.get(1.0, END))))
    speak_btn.place(x=140, y=200)


def STT():
    stt_wn = Toplevel(root)
    stt_wn.title('Speech-to-Text Converter')
    stt_wn.geometry("350x200")
    stt_wn.configure(bg='IndianRed')

    Label(stt_wn, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='IndianRed').place(x=50)

    text = Text(stt_wn, font=12, height=3, width=30)
    text.place(x=7, y=100)

    record_btn = Button(stt_wn, text='Record', bg='Sienna', command=lambda: text.insert(END, record()))
    record_btn.place(x=140, y=50)


def instruction():
    instructions = '''
These are the instructions:
1. Wait for some time because STT and TTS conversions take time.
2. Pause for 2 seconds to end your phrase in STT conversion, because that is the pause_threshold amount.
'''
    showinfo("Instructions before beginning", instructions)


# GUI
root = Tk()
root.title('ProjectGurukul python text to speech and speech to text Converter')
root.geometry('300x300')
root.resizable(0, 0)
root.configure(bg='Salmon')

# Placing all the components
Label(root, text='ProjectGurukul Text-To-Speech and Speech-To-Text Converter',
      font=('Comic Sans MS', 16), bg='Salmon', wrap=True, wraplength=300).place(x=15, y=0)

tts_btn = Button(root, text='TTS Conversion', font=('Helvetica', 16), bg='MediumPurple', command=TTS)
tts_btn.place(x=60, y=150)

stt_btn = Button(root, text='STT Conversion', font=('Helvetica', 16), bg='MediumPurple', command=STT)
stt_btn.place(x=60, y=200)

instruction_btn = Button(root, text='Instructions before starting', font=('Helvetica', 16), bg='MediumPurple',
                         command=instruction)
instruction_btn.place(x=15, y=250)

# Updating main window
root.update()
root.mainloop()