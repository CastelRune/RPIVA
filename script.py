#!/usr/bin/env python3
print("Loading...")
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import pygame
from pygame import mixer
aiy.audio.get_recorder().start()

def main():
    assistant_name="Magic" # AI will understand your query while it is pronounced after assistant's name (in this var).
    
    pygame.init()
    recog = aiy.cloudspeech.get_recognizer()
    recog.expect_phrase(assistant_name)
    text=recog.recognize()
    if text!=None:
        print(text)
        if "music" in text:
            print("Starting to play music...")
            aiy.audio.say("Let's go !")
            pygame.display.set_mode((200,100))
            mixer.init()
            mixer.music.load("/home/pi/AIY-voice-kit-python/src/dna.mp3")
            mixer.music.play(0)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        if "repeat after me" in text:
            aiy.audio.say(text[len("repeat after me"):])
        
if __name__=='__main__':
    aiy.audio.say("Online !")
    print("Online !")
    while True:
        main()