#!/usr/bin/python


'''
Need to do:
Add a win condition
Add graphics
Add music
If ball gets past top, eliminate ball player.die()
'''

import sys, logging, pygame, random, os
import level_generator
from Color import Color
from Sound import Sound
from Player import Player
from Enemy import Enemy
from Level import Level, Floor
from itertools import repeat
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
#made the window bigger to reduce difficulty and let players know what's next
screen_size = (800,800)
FPS = 60
gravity = 1.5
friction = 0.3
lives = 1


def main():

        pygame.init()
        won = False
        screen = pygame.display.set_mode(screen_size)
        screen_rect = screen.get_rect()
        clock = pygame.time.Clock()

        offset = repeat((0, 0))

        sound = Sound()
        '''
        Add whatever soundtrack files you want to the mp3 folder, and then add them to the soundtrack by calling

        sound.add_music('Ambient_Blues_Joe_ID_773.mp3') # replace with whatever the filename is

        Once you have added the tracks you want, just call

        sound.play_music()

        When the song finishes, the library will queue up and play the next one in the order you added them

        ---------------------------------

        You can add sounds to the sound library by calling

        sound.add_sound('footstep','footstep_sound.mp3')

        It assumes the sounds are in the mp3 folder
        To play sounds in the library, you can call

        sound.play_sound('footstep')
        '''

        level = Level('level_random.game') #a game level definition
        players = pygame.sprite.Group()
        player = Player(level.get_player_starting_position(),lives,level.block_size,gravity,friction)
        players.add(player)
        enemies = pygame.sprite.Group()
        for e in level.get_enemies():
                enemy = Enemy(gravity,e,level.block_size)
                enemies.add(enemy)
        floors = pygame.sprite.Group()
        for f in level.get_floor():
                floor = Floor(gravity,f,level.block_size)
                floors.add(floor)



        while True:
                clock.tick(FPS)
                screen.fill(Color.black)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                if event.type == sound.event():
                        song.play_music()

                keys = pygame.key.get_pressed()

                if player.lives == 0:
                        screen.fill(Color.black)
                        font = pygame.font.SysFont("arial", 64)
                        f = font.render('GAME OVER', True, Color.white)
                        screen.blit(f, (230, 400))
                        pygame.display.flip()

                elif won:
                    screen.fill(Color.green_5)
                    font = pygame.font.SysFont("arial", 64)
                    f = font.render('YOU WIN', True, Color.yellow_4)
                    screen.blit(f, (230, 400))
                    pygame.display.flip()

                else:
                # a complete list of the pygame key constants can be found here: https://www.pygame.org/docs/ref/key.html
                    if keys[pygame.K_LEFT]:
                        player.move(-1)
                    elif keys[pygame.K_RIGHT]:
                        player.move(1)
                    #I removed the player's ability to move left or stop
                    #this adds challenge and an "infinite" element to the game
                    #makes it similar to canabalt in a way
                    if keys[pygame.K_UP]:
                            player.jump()

                    floors.update()
                    enemies.update()
                    players.update(level,enemies,floors)

                    full_screen = level.get_full_screen()
                    floors.draw(full_screen)
                    enemies.draw(full_screen)
                    players.draw(full_screen)

                    for x in enemies:
                            if player.rect.colliderect(x.rect):
                                    won = True

                    if level.screen_shake:
                            offset = level.shake()
                            level.screen_shake = False

                    screen.blit(level.get_screen(),next(offset),level.get_rect(screen_size,player))
                    pygame.display.flip()

if __name__ == '__main__':
        main()
