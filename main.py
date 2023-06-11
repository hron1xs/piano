import play #імпорт бібліотек
import pygame 

pygame.init()
pygame.mixer.init()
play.set_backdrop((230, 230, 250))
#створення текстових спрайтів

text1 = play.new_text(words='It is piano', x=0, y=200,)
text1 = play.new_text(words='you can play it', x=0, y=150)

piano_on = play.new_circle(color=(250, 250, 250),x = -185,y = -90,radius=7,border_color=(0, 0, 0),border_width=4)
piano_txt = play.new_text(words='piano', x = -150, y = -90, font_size=25)

flute_on = play.new_circle(color=(250, 250, 250),x = -85,y = -90,radius=7,border_color=(0, 0, 0),border_width=4)
flute_txt = play.new_text(words='flute', x = -55, y = -90, font_size=25)

guitar_on = play.new_circle(color=(250, 250, 250),x = 15 ,y = -90,radius=7,border_color=(0, 0, 0),border_width=4)
guitar_txt = play.new_text(words='guitar', x = 50, y = -90, font_size=25)

violin_on = play.new_circle(color=(250, 250, 250),x = 115 ,y = -90,radius=7,border_color=(0, 0, 0),border_width=4)
violin_txt = play.new_text(words='violin', x = 150, y = -90, font_size=25)

keys = [] #список для клавіш
sounds = [] #список для звуків
for s in range(4):
    sounds.append([])

for i in range(8): #цикл для створення 8 клавіш
    key_x = -180 + i*50 #розміщення клавіш
    key = play.new_box(color=(0,0,0), width=40, height=100, x=key_x, y=0,border_color=(250,250,250),border_width=3) #створення клавіш
    keys.append(key) #додавання клавіш в кінець списку
    sound= pygame.mixer.Sound(str(i+1) + '.ogg')
    sounds[0].append(sound)
    sound= pygame.mixer.Sound('f' + str(i+1) + '.ogg')
    sounds[1].append(sound)
    sound= pygame.mixer.Sound('g' + str(i+1) + '.ogg')
    sounds[2].append(sound)#додавання звуків в кінець списку
    sound= pygame.mixer.Sound('v' + str(i+1) + '.ogg')
    sounds[3].append(sound)#додавання звуків в кінець списку

get_instrument = 0




@play.when_program_starts #декоратор
def starts():
    pass
    


@piano_on.when_clicked
def piano_on():
    global get_instrument
    get_instrument = 0
    piano_on.color = (250, 250, 250)
    flute_on.color = (0, 0, 0)
    guitar_on.color = (0, 0, 0)
    violin_on.color = (0, 0, 0)

def flute_on():
    global get_instrument
    get_instrument = 1
    piano_on.color = (0, 0, 0)
    flute_on.color = (250, 250, 250)
    guitar_on.color = (0, 0, 0)
    violin_on.color = (0, 0, 0)

def guitar_on():
    global get_instrument
    get_instrument = 2
    piano_on.color = (0, 0, 0)
    flute_on.color = (0, 0, 0)
    guitar_on.color = (250, 250, 250)
    violin_on.color = (0, 0, 0)

def violin_on():
    global get_instrument
    get_instrument = 3
    piano_on.color = (0, 0, 0)
    flute_on.color = (0, 0, 0)
    guitar_on.color = (0, 0, 0)
    violin_on.color = (250, 250, 250)

@play.repeat_forever #декоратор2
async def play_piano():
        for j in range(8):      
            if keys[j].is_clicked:
                sounds[j].play()
                keys[j].color = (92, 92, 92)
                await play.timer(0.3)
                keys[j].color = (0, 0, 0)

play.start_program() 