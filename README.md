Game Overview-
 The game is a 2D platformer with a medieval theme. The player character is a knight with a crossbow and arrows. 

Sprites-
    Knight is the player character. The animation is controlled by a sprite sheet. The sprite is always alive because it is the main player character. The player character can move left and right, and can jump. When the player hits the edge of the screen it just wraps back to the other side. The player collides with the platform to stand on it like ground.

    Arrow is a projectile sprite that the knight fires. The life span is a max of 5 projectiles on screen or hitting the edge of the screen. When arrow hits the edge of the screen it hides it so a new arrow can be fired.

Game Initialization-
    The game starts up with a castle in the background, a platform in the foreground with the knight player character on top.

Game Class Behavior-
    The game class handles the firing of the projectiles and the collision of the player with the ground.

Game Assets-
    Character sprite from universal LPC character generator
    Background from Kenny's assets
    Arrow sprite from Open game art
