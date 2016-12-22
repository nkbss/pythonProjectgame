import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SPRITE_SCALING = 3



class myProject(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        #set up list
        self.all_sprites_list = None
        self.choco_list = None
        self.score = 0
        self.player_sprite = None

        arcade.set_background_color(arcade.color.BLACK)

    def start_game(self):
        #setup lists
        self.all_sprites_list = arcade.SpriteList()
        self.choco_list = arcade.SpriteList()
        #setup player
        self.player_sprite = arcade.Sprite("chinjung.jpg", SPRITE_SCALING)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.all_sprites_list.append(self.player_sprite)

        for i in range(20):
            choco = arcade.Sprite("choco.png",SPRITE_SCALING/3)

            choco.center_x = random.randrange(SCREEN_WIDTH)
            choco.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprites_list.append(choco)
            self.choco_list.append(choco)

        self.set_mouse_visible(False)


    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def animate(self,delta):
        self.score = 10

    def on_mouse_motion(self,x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y



if __name__ == '__main__':
    window = myProject(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_game()
    arcade.run()
