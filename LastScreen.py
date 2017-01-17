import sys
import os
import pygame as pg

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

filename = 'RedAlert.jpg'

pg.init()
screen = pg.display.set_mode((1600, 900), pg.NOFRAME)
pg.display.set_caption('Console')
screen_rect = screen.get_rect()
clock = pg.time.Clock()

background_1 = pg.image.load('RedAlert.png').convert()
background_2 = pg.image.load('RedAlert2.png').convert()
background_3 = pg.image.load('Start.png').convert()
background_4 = pg.image.load('Black.png').convert()

time_till_explode = 36.1

font = pg.font.Font(None, 108)
rendered_text = font.render(str(round(time_till_explode,3)), True, pg.Color("white"))
text_rect = rendered_text.get_rect(midleft=(760, 700))  
textwidth = text_rect.width 

phase = 0
slow_down = False
super_slow_down = False
simple_stupid_counter = 0
show_console = True

done = False
while time_till_explode >= 0:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    slow_down = not slow_down
                    super_slow_down = False
                if event.key == pg.K_s:
                    slow_down = False
                    super_slow_down = not super_slow_down
                if event.key == pg.K_q:
                    time_till_explode = 0
                if event.key == pg.K_c:
                    time_till_explode = 36.1
                    show_console = False

    screen.fill(pg.Color("gray5"))
    if show_console:
        screen.blit(background_3, (0,0))
        pg.display.update()        
        clock.tick(100)
    else:
        if simple_stupid_counter <= 50:
            screen.blit(background_1, (0,0))
        else:
            screen.blit(background_2, (0,0))
        if simple_stupid_counter >= 100:
            simple_stupid_counter = 0
    
        simple_stupid_counter += 1
        
        time_till_explode -= 0.009
        if(time_till_explode >= 0):
            screen.blit(font.render(str(round(time_till_explode,3)), True, pg.Color("white")), text_rect)
        else:
            screen.blit(background_4, (0,0))
            
        pg.display.update()
        if slow_down:    
            #clock.wait(1000)
            pg.time.wait(100)
        else:
            if super_slow_down: 
                pg.time.wait(1000)
            else:
                clock.tick(100)
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        else:
            if event.type == pg.KEYDOWN:
                 if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
        screen.blit(background_4, (0,0))
        pg.display.update()
        clock.tick(60)
        
        
pg.quit()
sys.exit()