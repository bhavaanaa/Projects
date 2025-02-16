
from gtts import gTTS, lang
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3

def text_to_speech():

       text1 = text_entry.get("1.0","end-1c")
       myobj=gTTS (text=text1, lang='en', slow =False)
       myobj.save("voice.mp3")
       song =MP3 ("voice.mp3") 
       pygame.mixer.init()
       pygame.mixer.music.load('voice.mp3')
       pygame.mixer.music.play()
       time.sleep(song.info.length)
       pygame.quit()

def speech_to_text(): 
       recorder = sr.Recognizer()
       try:
               duratio =10
       except:
               messagebox.showerror(message="Enter the duration")
               return

       messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
       with sr.Microphone() as mic: 
               
               recorder.adjust_for_ambient_noise(mic)
               audio_input = recorder.listen(mic)   
               try:                        
                       text_output =recorder.recognize_google(audio_input)
                       
                       messagebox.showinfo(message="You said:\n "+text_output)       
               except:
                        messagebox.showerror(message="Couldn't process the audio input.")

def speech_to_speech(): 
       recorder = sr.Recognizer()
       try:
               duratio =5
       except:
               messagebox.showerror(message="Enter the duration")
               return
       messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
       with sr.Microphone() as mic: 
               
               recorder.adjust_for_ambient_noise(mic)
               audio_input = recorder.listen(mic)   
               try:                      
                       text_output =recorder.recognize_google(audio_input)
                        
                       if text_output=='how are you':
                               ans='i am fine'
                       elif text_output=='whats going on':
                               ans ='just nuthing what about you'
                       elif text_output=='hows your day':
                               ans ='its good'
                       elif text_output=='what about you':
                               ans ='i am good too'

                       text1 = ans
                       myobj=gTTS (text=text1, lang='en', slow =False)
                       myobj.save("voice.mp3")
                       song =MP3 ("voice.mp3") 
                       pygame.mixer.init()
                       pygame.mixer.music.load('voice.mp3')
                       pygame.mixer.music.play()
                       time.sleep(song.info.length)
                       pygame.quit()      
               except:
                        messagebox.showerror(message="Couldn't process the audio input.")

window = Tk()
window.geometry("500x300")
window.title("Convert Speech to text and text to Speech: PythonGeeks")
title_label = Label(window, text="Convert Speech to text and text to Speech: PythonGeeks").pack()
text_label = Label(window, text="Text:").place(x=10,y=20)
text_entry = Text(window, width=35,height=8)
text_entry.place(x=80,y=20)
button1 = Button(window,text='Convert speech_to_speech', bg = 'Turquoise',fg='Red',command=speech_to_speech).place(x=175,y=250)
button2 = Button(window,text='Convert Text to Speech', bg = 'Turquoise',fg='Red',command=text_to_speech).place(x=60,y=190)
button3 = Button(window,text='Convert Speech to Text', bg = 'Turquoise',fg='Red',command=speech_to_text).place(x=305,y=190)
 
window.mainloop()

