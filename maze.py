from pygame import *
win_width=700
win_height=500
window=display.set_mode((win_width,win_height))
display.set_caption('')
bg= transform.scale(image.load('background.jpg'),(700,500))
clock=time.Clock()
fps=60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick=mixer.Sound('kick.ogg')
money=mixer.Sound('money.ogg')

font.init()
font=font.Font(None,70)
win=font.render('Kamu menang chuy',True,(255,215,0))
lose=font.render('kalaahh',True,(255,215,0))

class GamesSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GamesSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y+=self.speed

class Enemy(GamesSprite):
    direction='left'
    def update(self):
        if self.rect.x<= 470:
            self.direction='right'
        if self.rect.x >= win_width-85:
            self.direction='left'

        if self.direction=='left':
            self.rect.x-=self.speed
        else:
            self.rect.x+= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.height=wall_height
        self.width=wall_width
        self.image=Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

game=True
finish=False

tumball_1=Wall(42,205,145,120,213,8,340)
tumball_2=Wall(42,205,145,240,150,8,200)
tumball_3=Wall(42,205,145,200,340,190,8)
tumball_4=Wall(42,205,145,380,150,8,200)
tumball_5=Wall(42,205,145,490,213,8,400)

dodon = Player('hero.png',0,win_height-65,10)
aboy=Enemy('cyborg.png',500,win_height-250,5)
egy=GamesSprite('treasure.png',610,win_height-65,0)

while game :
    for e in event.get():
        if e.type==QUIT:
            game=False

    if not finish :

        window.blit(bg,(0,0))

        tumball_1.draw_wall()
        tumball_2.draw_wall()
        tumball_3.draw_wall()
        tumball_4.draw_wall()
        tumball_5.draw_wall()

        dodon.reset()
        dodon.update()
        aboy.reset()
        aboy.update()
        egy.reset()

        if sprite.collide_rect(dodon,tumball_1)or sprite.collide_rect(dodon,tumball_2)or sprite.collide_rect(dodon,tumball_3)or sprite.collide_rect(dodon,tumball_4)or sprite.collide_rect(dodon,tumball_5)or sprite.collide_rect(dodon,aboy):
            finish=True
            kick.play()
            window.blit(lose,(200,200))

        if sprite.collide_rect(dodon,egy):
            finish=True
            money.play()
            window.blit(win,(200,200))

    clock.tick(fps)
    display.update()