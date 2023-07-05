import pygame
from random import randint
from time import sleep


pygame.init()
pygame.mixer.music.load('gameadv.mp3')
pygame.mixer.music.play()
c = randint(0, 5)


print(' ')
print('\033[1;34m-=--'*30)
print(f'                                      \033[1;34mVou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=--'*30)
print(' ')

n = int(input('>>> Em que número eu pensei? '))
print('\033[4;33mPROCESSANDO...\033[m')
sleep(3)


if n > 5:
    print('\033[1;36mNÚMERO INVÁLIDO. EXECULTE NOVAMENTE E ESCOLHA UM NÚMERO ENTRE 0 E 5')
    pygame.init()
    pygame.mixer.music.load('retorne.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


else:
    if n == c:
        print('{}PARABÉNS! Você conseguiu me vencer!'.format('\033[1;32m'))
        pygame.init()
        pygame.mixer.music.load('acerto.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
    else:
        print('{}GANHEI! Eu pensei no número \033[4;31m{}\033[m\033[1;31m e não no \033[4;31m{}\033[m\033[1;31m!'.format('\033[1;31m', c, n))
        pygame.init()
        pygame.mixer.music.load('errado.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
