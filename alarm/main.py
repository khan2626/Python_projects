#!/usr/bin/env python
import time
import pygame

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

pygame.mixer.init()

def play_song():
    pygame.mixer.music.load('Grenade+1.mp3')
    pygame.mixer.music.play(-1)

def stop_song():
    pygame.mixer.music.stop()



def alarm(seconds):
    print(CLEAR)
    while True:
        end_time = 0
        if seconds > end_time:
            time.sleep(1)
            seconds -= 1
            min_left = seconds // 60
            sec_left = seconds % 60
            
            print(f'{CLEAR_AND_RETURN}Time left is {min_left:02d} : {sec_left:02d}')
        else:
            break

    play_song()
    while True:
        answer = input('press q to quit: ').lower()
        if answer == 'q':
            stop_song()
            break
print("---------------------------------------------------")
print("set your alarm ........\n")
minutes = int(input('enter minutes: '))
seconds = int(input('enter the number of seconds: '))
total_time = minutes * 60 + seconds
alarm(total_time)


