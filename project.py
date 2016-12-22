import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.5


class Player(arcade.Sprite):
    def __init__(self):
        self.x = 200
        self.y = 200

    def update(self,dir):
        self.dir = dir
        if dir == 0:
            self.y +=20
        elif dir == 1:
            self.y -=20
        elif dir == 2:
            self.x += 20
        elif dir == 3:
            self.x -= 20

    def on_key_press(key, key_modifiers):
        if key == arcade.key.UP:
            self.update(0)
        elif key == arcade.key.DOWN:
            self.update(1)
        elif key == arcade.key.RIGHT:
            self.update(2)
        elif key == arcade.key.LEFT:
            self.update(3)


class myProject(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        #set up list
        self.player_sprite = arcade.Sprite("images/chinjung.png")
        self.choco_sprite = arcade.Sprite("images/ballBlue.png")
        self.score = 0

        arcade.set_background_color(arcade.color.BLACK)


    def player_on_key_press(self,key, key_modifiers):
        self.player.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def animate(self,delta):
        self.score = 10

if __name__ == '__main__':
    window = myProject(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
