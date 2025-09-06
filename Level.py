import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("castle_BG.png")
        self.knight = Knight(self)
        self.platforms = [Platform(self, (100, 450))]
        self.setCaption("Game")
        self.NUM_BULLETS = 5
        self.currentBullet = 0       
        self.bullets = []
        self.sprites = [self.knight, self.platforms, self.bullets]
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.knight))
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentBullet += 1
                if self.currentBullet >= self.NUM_BULLETS:
                    self.currentBullet = 0
                self.bullets[self.currentBullet].fire()

class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("Arrow.png")
        self.setSize(45,10)
        self.setBoundAction(self.HIDE)
        self.hide()
    def fire(self):
        self.show()
        self.position = self.parent.position
        self.moveAngle = self.parent.moveAngle
        self.imageAngle = self.parent.moveAngle
        self.speed = 20

class Knight(simpleGE.Sprite) :
    def __init__(self, scene):
        super().__init__(scene)     
        self.plyrWalk = simpleGE.SpriteSheet("Knight_Walking.png", (64,64), 4, 9, .2)
        self.plyrWalk.startCol = 0
        self.animRow = 3
        self.position = (50, 400)
        self.inAir = False

    def process(self):
        self.dx = 0
        walk = False
        self.shootRight = False
        if self.inAir == True:
            self.animRow = 3
            self.addForce(.2, 270)
        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy = 0
        if self.isKeyPressed(pygame.K_UP):
            if not self.inAir:
                self.addForce(6,90)
                self.inAir = True
        if not self.inAir == True:
            if self.isKeyPressed(pygame.K_LEFT):
                self.speed = 2
                walk = True
                self.animRow = 1
                self.moveAngle = 180
            if self.isKeyPressed(pygame.K_RIGHT):
                self.speed = 2
                walk = True
                self.animRow = 3
                self.moveAngle = 0
            if walk == True:
                self.copyImage(self.plyrWalk.getNext(self.animRow))
            else:
                self.copyImage(self.plyrWalk.getCellImage(0, self.animRow))
        
        for platform in self.scene.platforms:
            if self.collidesWith(platform):                
                if self.dy > 0:
                        self.bottom = platform.top
                        self.dy = 0
                        self.inAir = False

class Platform(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.colorRect("lightgreen", (10000,50))



def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()