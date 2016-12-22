import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SPRITE_SCALING = 2

class Choco(arcade.Sprite):

        def update(self):
            self.center_y -= 5

        def animate(self,delta):
            self.update()
            self.randomChoco()

class MotherPlayer(arcade.Sprite):
        def update(self):
            self.center_y -= 8
        def animate(self,delta):
            self.update()





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
        self.motherPlayer_list = arcade.SpriteList()

        #setup player
        self.player_sprite = arcade.Sprite("chinjung.jpg")
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.all_sprites_list.append(self.player_sprite)
        self.genRandomChoco(2)
        self.genRandomMother(1)
        self.set_mouse_visible(False)


    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 20)

    def animate(self,delta_time):
        self.all_sprites_list.update()
        self.choco_collision()


    def on_mouse_motion(self,x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def choco_collision(self):
        for choco in self.choco_list:
            hit_choco = arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.choco_list)
            for choco in hit_choco:
                choco.kill()
                self.genRandomChoco(1)
                self.score += 1

            if choco.bottom <= 10:
                self.score -=1
                self.genRandomChoco(1)
                choco.kill()


    def genRandomChoco(self,num):
        for i in range(num):
            choco = Choco("choco.png")
            choco.center_x = random.randrange(20,SCREEN_WIDTH-20)
            choco.center_y = 750
            self.all_sprites_list.append(choco)
            self.choco_list.append(choco)

    def genRandomMother(self,num):
        for i in range(num):
            motherPlayer = MotherPlayer("Ghost.png")
            motherPlayer.center_x = random.randrange(20,SCREEN_WIDTH-20)
            motherPlayer.center_y = 750
            self.all_sprites_list.append(motherPlayer)
            self.motherPlayer_list.append(motherPlayer)



if __name__ == '__main__':
    window = myProject(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_game()
    arcade.run()
