#1. Chuẩn bị file input
from genericpath import isfile
from pathlib import Path
import os.path as p

def draw_maze(lv): 
    #Lấy parent của directory hiện tại
    cur = p.dirname(Path(__file__).parent.absolute())
    level = cur + '\\input\\' + lv + '\\'

    if lv == 'level_1':
    # Level_1
    # Map no.1: Mê cung thông thường
        inputDir = p.join(level,'input1.txt')
        if not p.isfile(inputDir):
            with open(inputDir, 'w') as outfile:
                outfile.write('0\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('x   x       x       x          x  x   x\n')
                outfile.write('x   x   x   x       x      x   x  x    \n')
                outfile.write('x   x   xx xx       x          x  x   x\n')
                outfile.write('x   x       xxx xxxxx   xxxx   x      x\n')
                outfile.write('x x    xx  xxxx xxx x     x   xx    x x\n')
                outfile.write('x               xx     x   x   x   x  x\n')
                outfile.write('x      x        x      x   x   x   x  x\n')
                outfile.write('x   x  x        x      x   x   x   x  x\n')
                outfile.write('x   x    xxxx   x  x           x   x  x\n')
                outfile.write('x xxxxx x       x  x   x    xxxx   x  x\n')
                outfile.write('x               x      x   x   x      x\n')
                outfile.write('xxxxxxxxx  x x        x     x         x\n')
                outfile.write('xS         x x  x x          x        x\n')
                outfile.write('xxxxx x  x x x     x                  x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    # Map no.2: Bản đồ có các bức tường song song tạo thành 2 hướng đi về đích
        inputDir = p.join(level,'input2.txt')
        if not p.isfile(inputDir):
            with open(inputDir, 'w') as outfile:
                outfile.write('0\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('x x        x     x   x    x           x\n')
                outfile.write('x x x      x     x x x x  x xxx    x  x\n')
                outfile.write('x x x   x  x     x x x x  x x x    x  x\n')
                outfile.write('xSx x   x  x  x  x x x x  xx  x       x\n')
                outfile.write('x x x   x  x  x  x x x x  x   x        \n')
                outfile.write('x x x   x  x  x  x x x x  xx  x    x  x\n')
                outfile.write('x x x   x  x  x  x x x x  x        x  x\n')
                outfile.write('x x x   x  x  x  x x x x  x        x  x\n')
                outfile.write('x x x   x x  x  x x x x  x         x  x\n')
                outfile.write('x x x   x  x  x  x x x x  x        x  x\n')
                outfile.write('x x x   x  x  x  x x x x  x  xxxx     x\n')
                outfile.write('x x x   x  x  x  x x x x  x           x\n')
                outfile.write('x   x      x  x  x x x x  x  x        x\n')
                outfile.write('x                                     x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    # Map no.3: Có đường đi 1 ngắn - 1 dài
        inputDir = p.join(level,'input3.txt')
        if not p.isfile(inputDir):
            with open(inputDir, 'w') as outfile:
                outfile.write('0\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('xS                                    x\n')
                outfile.write('x x xxxxx  x   xxx  xxxxx  x  x       x\n')
                outfile.write('x x   x x xxxxxx    x   x  x  x        \n')
                outfile.write('x xxx x x      x xxxx  xx  x  x       x\n')
                outfile.write('x       xxxxx  x    x  x   x  x    x  x\n')
                outfile.write('x xxxxxxx  x   x    x  x   x  x    x  x\n')
                outfile.write('x x        x        x  xx  xxxx    x  x\n')
                outfile.write('x x        xxxxxxxxxx   x  x          x\n')
                outfile.write('x x                     x  x     x    x\n')
                outfile.write('x xxxxxx    x  x        x  x     x    x\n')
                outfile.write('x      x    x  x xxx  x x  x     x    x\n')
                outfile.write('x      x    x  x xxx  x x  x     x    x\n')
                outfile.write('xxx         x  xxx    x xxxx     x    x\n')
                outfile.write('x   x       x    x   xx               x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    #Map no.4: Có nhiều vật chắn, ngõ cụt
        inputDir =  p.join(level,'input4.txt')
        if not p.isfile(inputDir):
            with open(inputDir, 'w') as outfile:
                outfile.write('0\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('xSx  x                 x     x    x    x\n')
                outfile.write('x x  xxxxx  x     xxxxxx   xxx    x xx x\n')
                outfile.write('x x  x      x          x     x    x  x x\n')
                outfile.write('x x  x      xxxxx   x  xxx   x    x  x x\n')
                outfile.write('x x  x      x          x     x    x  x x\n')
                outfile.write('x    x  x   x      x      x     x x  x x\n')
                outfile.write('x    x  x   x      x   x      xxx xxxx x\n')
                outfile.write('x x  x  x  xxxx    x   xxxxx    x x  x x\n')
                outfile.write('x x  x  x  xxxxxx  x   x      xxx    x x\n')
                outfile.write('x x  x  x  x    x  x   x             x x\n')
                outfile.write('x x     x  x xx x  x   xxxxxxxxxx   xx x\n')
                outfile.write('xxxxxxxxx  x x  x            x         x\n')
                outfile.write('x          x x  x       xxxxxx    x     \n')
                outfile.write('xxxx       x xxxxxxxx        x     xxx x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 

    # Map no.5: Bản đồ lớn có nhiều vật chắn nhỏ
        inputDir = p.join(level,'input5.txt')
        if not p.isfile(inputDir):
            with open(p.join(level,'input5.txt'), 'w') as outfile:
                outfile.write('0\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('x           x             x     x                   x              x      x\n')
                outfile.write('x           x             x     x        xxxxxxx    x    xxxxx     x      x\n')
                outfile.write('x   x    x           x    x     x        x          x        x     x      x\n')
                outfile.write('x   x    xxxxxxxx    x    x     xxxxx    x     xxxxxx        x     xxxxxxxx\n')
                outfile.write('x        x           x    x              x                   x            x\n')
                outfile.write('xxxx     x    xxxxxxxx    x     xxxxx    x     xxxxxx        xxxxxxxxx    x\n')
                outfile.write('xS       x                x     x        x     x                     x    x\n')
                outfile.write('xxxx     x        xxxx    x     x    xxxxx     x      xxxxxxxxxx     x    x\n')
                outfile.write('x        x                      x        x                     x     x    x\n')
                outfile.write('x     xxxx   xxxxxxxxxxxxxxx    x     xxxx     xxxxxxx         xxxxxxx    x\n')
                outfile.write('x               x               x     x        x                          x\n')
                outfile.write('xxxxxxxx        x    xxxxxxxxxxxx     x        xxxxxxxxxxxxx   xxxxxxx    x\n')
                outfile.write('x                    x                x                    x         x     \n')
                outfile.write('x      xxxxxxxxxxxxxxx                xxxxxxxxxxx     x    xxxx      x    x\n')
                outfile.write('x                                                     x                   x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
    #level 2
    if lv == 'level_2':
        inputDir = p.join(level,'input1.txt')
        if not p.isfile(inputDir):
            with open(inputDir, 'w') as outfile:
                outfile.write('2\n')
                outfile.write('6 2 -10\n')
                outfile.write('10 33 -5\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('xSx  x                 x     x    x       x\n')
                outfile.write('x x  xxxxx  x     xxxxxx   xxx    x xx    x\n')
                outfile.write('x x  x      x          x     x    x  x    x\n')
                outfile.write('x x  x      xxxxx   x  xxx   x    x  x    x\n')
                outfile.write('x x  x      x          x     x    x  x    x\n')
                outfile.write('x +  x  x   x      x      x     x x  x    x\n')
                outfile.write('x    x  x   x      x   x      xxx xxxx    x\n')
                outfile.write('x x  x  x  xxxx    x   xxxxx    x x  x    x\n')
                outfile.write('x x  x  x  xxxxxx  x   x      xxx    x    x\n')
                outfile.write('x x  x  x  x    x  x   x          +  x    x\n')
                outfile.write('x x     x  x xx x  x   xxxxxxxxxx   xx    x\n')
                outfile.write('xxxxxxxxx  x x  x            x            x\n')
                outfile.write('x          x x  x       xxxxxx    x        \n')
                outfile.write('xxxx       x xxxxxxxx        x     xxx    x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 

        inputDir = p.join(level,'input2.txt')
        if not p.isfile(inputDir):     
            with open(inputDir, 'w') as outfile:
                outfile.write('3\n')
                outfile.write('10 20 -10\n')
                outfile.write('8 1 -30\n')
                outfile.write('3 32 -5\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('xS                                    x\n')
                outfile.write('x x xxxxx  x   xxx  x  xx  x  x       x\n')
                outfile.write('x x   x x xxxxxx    x   x  x  x  +     \n')
                outfile.write('x xxx x x      x xxxx  xx  x  x       x\n')
                outfile.write('x       xxxxx  x    x  x   x  x    x  x\n')
                outfile.write('x xxxxxxx  x   x    x  x   x  x    x  x\n')
                outfile.write('x x        x        x  xx  xxxx       x\n')
                outfile.write('x+x        xxxxxxxxxx   x  x          x\n')
                outfile.write('x x                     x  x     x    x\n')
                outfile.write('x xxxxxx    x  x    +   x  x     x    x\n')
                outfile.write('x      x    x  x xxx  x x  x     x    x\n')
                outfile.write('x      x    x  x xxx  x x  x     x    x\n')
                outfile.write('xxx         x  xxx    x xxxx     x    x\n')
                outfile.write('x   x       x    x                    x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  

        inputDir = p.join(level,'input3.txt')
        if not p.isfile(inputDir):
            with open(p.join(level,'input3.txt'), 'w') as outfile:
                outfile.write('10\n')
                outfile.write('1 6 -20\n')
                outfile.write('2 36 -15\n')       
                outfile.write('5 70 -10\n')
                outfile.write('7 22 -22\n') 
                outfile.write('8 24 -22\n')
                outfile.write('9 35 -6\n')
                outfile.write('9 38 -8\n')
                outfile.write('12 10 -5\n')
                outfile.write('13 26 -3\n')
                outfile.write('15 59 -1\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                outfile.write('x     +     x             x     x                   x              x      x\n')
                outfile.write('x           x             x     x        xxxxxxx    x    xxxxx     x      x\n')
                outfile.write('x   x    x           x    x     x        x          x        x     x      x\n')
                outfile.write('x   x    xxxxxxxx    x    x     xxxxx    x     xxxxxx        x     xxxxxxxx\n')
                outfile.write('x        x           x    x              x                   x        +   x\n')
                outfile.write('xxxx     x    xxxxxxxx    x     xxxxx    x     xxxxxx        xxxxxxxxx    x\n')
                outfile.write('xS       x            +   x     x        x     x                     x    x\n')
                outfile.write('xxxx     x        xxxx  + x     x    xxxxx     x      xxxxxxxxxx     x    x\n')
                outfile.write('x        x                      x  +  +  x                     x     x    x\n')
                outfile.write('x     xxxx   xxxxxxxxxxxxxxx    x     xxxx     xxxxxxx         xxxxxxx    x\n')
                outfile.write('x               x               x     x        x                          x\n')
                outfile.write('xxxxxxxx  +     x    xxxxxxxxxxxx     x        xxxxxxxxxxxxx   xxxxxxx    x\n')
                outfile.write('x                    x                x                    x         x     \n')
                outfile.write('x      xxxxxxxxxxxxxxx                xxxxxxxxxxx     x    xxxx      x    x\n')
                outfile.write('x                                                     x    +              x\n')
                outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')