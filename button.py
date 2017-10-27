#!/usr/bin/env python3
print("Loading...")
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import pygame
from pygame import mixer
aiy.audio.get_recorder().start()
button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()

def main():
    pygame.init()
    aiy.audio.say("Online !")
    print("Online !")
    while True:
        assistant_name="Magic" # AI will understand your query while it is pronounced after assistant's name (in this var).
        button.wait_for_press()
        print("Got button !")
        aiy.audio.say("Playin' music")
        led.set_state(aiy.voicehat.LED.ON)
        pygame.display.set_mode((200,100))
        mixer.init()
        mixer.music.load("/home/pi/AIY-voice-kit-python/src/dna.mp3")
        mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        

if __name__=='__main__':
    main()