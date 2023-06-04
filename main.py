import play
import pygame 

pygame.init()
pygame.mixer.init()
play.set_backdrop((230, 230, 250))

text1 = play.new_text(words='It is piano', x=0, y=200,)
text1 = play.new_text(words='you can play it', x=0, y=150)

keys = []
sounds = []

for i in range(8):
    key_x = -180 + i*50
    key = play.new_box(color=(0,0,0), width=40, height=100, x=key_x, y=0,border_color=(250,250,250),border_width=3)
    keys.append(key)
    sound= pygame.mixer.Sound(str(i+1) + '.ogg')
    sounds.append(sound)

@play.when_program_starts #декоратор
def starts():
    pass
@play.repeat_forever #декоратор2
async def play_piano():
    for j in range(8):
            if keys[j].is_clicked:
                sounds[j].play()
                keys[j].color = (92, 92, 92)
                await play.timer(0.3)
                keys[j].color = (0, 0, 0)

play.start_program()