from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_x_speed,player_y_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed
    def fire(self):
        arrow = Arrow("arrow1.png",self.rect.centerx,self.rect.top,15,20,15)
        arrows.add(arrow)
class Arrow(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x > win_width+10:
            self.kill()
win_width = 1280
win_height = 700
window = display.set_mode((win_width,win_height))
display.set_caption("kakashka")

fon = transform.scale(image.load("fon.jpg"),(win_width,win_height))
arrows = sprite.Group()
hero = Player("player.png",5,win_height-80,80,80,0,0)

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                hero.x_speed = -8
            if e.key == K_RIGHT:
                hero.x_speed = 8    
            if e.key == K_UP:
                hero.y_speed = -8
            if e.key == K_DOWN:
                hero.y_speed = 8
            if e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                hero.x_speed = 0
            if e.key == K_RIGHT:
                hero.x_speed = 0   
            if e.key == K_UP:
                hero.y_speed = 0
            if e.key == K_DOWN:
                hero.x_speed = 0
    if not finish:
        window.blit(fon,(0,0))        
        hero.reset()
        hero.update()
        arrows.draw(window)
        arrows.update()
    time.delay(50)
    display.update()