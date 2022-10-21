import pygame, sys
from pygame_recorder import ScreenRecorder
from pathlib import Path
import os.path as p

def draw(x, y, color, screen, type=None):
    pygame.draw.rect(screen, color, (16*x+30+2, 16*y+80-2, 12, 14))
    pygame.display.update()
    clock = pygame.time.Clock()
    if type == 'route':
        clock.tick(30)
    else:
        clock.tick(500)

def create_video(start, end, route, bonus, walls, algo = None, level = None, map = None, heuristic = None):
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (30, 144, 255)  
    RES = 1300, 540
    FPS = 30
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(RES)
    pygame.display.set_caption('Search Algorithm')
    isPause = False

    currPath = p.dirname(Path(__file__).parent.absolute())
    map = map.strip(".txt")
    folder = currPath + '\\output\\' + level + '\\' + map + '\\' + algo + '\\'
    if level == 'level_1':    
        if (heuristic):
            if heuristic == 'Manhattan':
                name = algo + '_heuristic_1'
                recorder = ScreenRecorder(RES[0], RES[1], FPS, name, folder)
            elif heuristic == 'Euclidean':
                name = algo + '_heuristic_2'
                recorder = ScreenRecorder(RES[0], RES[1], FPS, name, folder)
        else:
            recorder = ScreenRecorder(RES[0], RES[1], FPS, algo, folder)
    elif level == 'level_2':
        recorder = ScreenRecorder(RES[0], RES[1], FPS, algo, folder)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                pygame.quit()
                sys.exit()
                

        if isPause == False:
            DISPLAYSURF.fill((255, 255, 255))

            for wall in walls:
                draw(wall[1],wall[0],BLACK,DISPLAYSURF)
            

            if bonus:
                for b in bonus:
                    draw(b[1],b[0],GREEN,DISPLAYSURF)
                    

            draw(start[1], start[0], YELLOW, DISPLAYSURF)
            #recorder.capture_frame(DISPLAYSURF)
            draw(end[1], end[0], RED, DISPLAYSURF)
            #recorder.capture_frame(DISPLAYSURF)

            route.pop(0)
            #route.pop()
            for r in route:
                draw(r[1],r[0],BLUE,DISPLAYSURF)
                recorder.capture_frame(DISPLAYSURF)
            
            if bonus:
                for b in bonus:
                    draw(b[1],b[0],GREEN,DISPLAYSURF)
                recorder.capture_frame(DISPLAYSURF)
        
        recorder.end_recording()    
        isPause = True