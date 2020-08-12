# desafio 21
import pygame

pygame.mixer.init()
pygame.mixer.music.load('Deutschland.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass