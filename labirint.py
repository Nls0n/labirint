from pygame import *
class card(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.fill_color = color
        self.rect=Rect(x,y,width,height)
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)
        
        
class pict(sprite.Sprite):
    def __init__(self, picture,width, height, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(pict):
    def __init__(self, picture, width, height, x, y, x_ms, y_ms):
        super().__init__(picture, width, height, x, y)
        self.x_ms = x_ms
        self.y_ms = y_ms
    def movement(self):
        if self.rect.x > 0 and self.x_ms < 0 or self.rect.x < 700-80 and self.x_ms > 0:
            self.rect.x += self.x_ms
        if self.rect.y > 0 and self.y_ms < 0 or self.rect.y < 500-80 and self.y_ms > 0:
            self.rect.y += self.y_ms

window = display.set_mode((700, 500))
green = (0,255,0)
#player1 = card(100,100,120,180, green) 
pic = transform.scale(image.load('way.png'), (700, 500))
back = (255,255,255)

wall1 = pict('wall.png', 150,100,100,100)
wall2 = pict('wall.png', 120,80,250,250)
wall3 = pict('wall.png', 150, 120, 390, 390)
final = pict('kotik.png', 80,80, 600, 400)
player = Player('hero.png', 100,100,0,0,0,0)
player2 = Player('spider.png', 100, 100,400,200,0,0)
player3 = Player('enemy2.png', 100,100,225,100,0,0)
player.reset()
player2.reset()
player3.reset()
win_width = 700
win_len = 500
display.set_caption('ezgame')
win = transform.scale(image.load('win.jpg'), (700,500))
loose = transform.scale(image.load('loose.jpg'), (700,500))
run = True
finish = False
direction = 'right'
while run:
    time.delay(50)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_ms=-15
            if e.key == K_DOWN:
                player.y_ms=+15
            if e.key == K_LEFT:
                player.x_ms =-10
            if e.key == K_RIGHT:
                player.x_ms =+10
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_ms = 0
            if e.key == K_DOWN:
                player.y_ms=0
            if e.key == K_LEFT:
                player.x_ms =0
            if e.key == K_RIGHT:
                player.x_ms =0
    if finish != True:

        window.blit(pic,(0,0))
        wall1.reset()
        wall2.reset()
        wall3.reset()
        #window.blit(pic, (600, 400))
        player.movement()
        player.reset()
        final.reset()
        if direction == 'right':
            if player2.rect.x<700-85:
                player2.rect.x+=7
            if player3.rect.x<700-85:
                player3.rect.x+=12
            else:
                direction = 'left'
        elif direction == 'left':
            if player2.rect.x>355:
                player2.rect.x-=7
            if player3.rect.x>230:
                player3.rect.x-=12
            else:
                direction='right'
        player2.reset()
        player3.reset()
        if sprite.collide_rect(player, final):
            finish = True 
            window.blit(win, (0,0))
            time.delay(100)
            #run = False
        if sprite.collide_rect(player, wall1):
            finish = True 
            window.blit(loose, (0,0))
            time.delay(100)
            #run = False
        if sprite.collide_rect(player, wall2):
            finish = True 
            window.blit(loose, (0,0))
            time.delay(100)
            #run = False
        if sprite.collide_rect(player, wall3):
            finish = True 
            window.blit(loose, (0,0))
            time.delay(100)
            #run = False
        if sprite.collide_rect(player, player2):
            finish = True 
            window.blit(loose, (0,0))
            time.delay(100)
        if sprite.collide_rect(player, player3):
            finish = True 
            window.blit(loose, (0,0))
            time.delay(100)

            #run = False
    display.update()

    if finish == True:
        time.delay(1000)
        break