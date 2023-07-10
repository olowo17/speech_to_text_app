import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import os

# Setting up the window
window = tk.Tk()
window.title('Speech to Text')
window.geometry('600x600')

def speech_to_text():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    try:
        # Perform speech recognition
        text = r.recognize_google(audio)
        if text:
            result_label.config(text="You said: " + text)

            # Convert response to speech and save as audio file
            language = 'en'
            text_to_speech = gTTS(text=text, lang=language)
            text_to_speech.save('response.mp3')
            os.system('response.mp3')
        else:
            print('nothing to translate')
    except sr.UnknownValueError:
        result_label.config(text="Speech recognition could not understand audio.")
    except sr.RequestError:
        result_label.config(text="Speech recognition service is unavailable.")



# Creating the result label
result_label = tk.Label(window, text='', font=('Arial', 12))
result_label.pack()

# Creating the button
button = tk.Button(window, text='Start', command=speech_to_text)
button.pack()

window.mainloop()
