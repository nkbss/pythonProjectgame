import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

class Choco(arcade.Sprite):
        def update(self):
            self.center_y -= 8

        def animate(self,delta):
            self.update()

class MotherPlayer(arcade.Sprite):
        def update(self):
            self.center_y -= 12

        def animate(self,delta):
            self.update()

class Heart(arcade.Sprite):
        def update(self):
            self.center_y -= 15

        def animate(self,delta):
            self.update()

class myProject(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.start_game()

    def start_game(self):
        #set value
        self.all_sprites_list = None
        self.choco_list = None
        self.motherPlayer_list = None
        self.heart_list = None
        self.player_sprite = None
        self.score = 0
        self.endScore = 0
        self.heart = 3
        self.heartPlayer = 1
        self.new_game = 0

        #setBackground
        self.bg = arcade.Sprite("endInterface.png")
        self.bg.set_position(250, 400)
        arcade.set_background_color(arcade.color.BLACK)

        #set up list
        self.all_sprites_list = arcade.SpriteList()
        self.choco_list = arcade.SpriteList()
        self.motherPlayer_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()

        #set up player
        self.player_sprite = arcade.Sprite("chinjung.png")
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.all_sprites_list.append(self.player_sprite)

        #set genRandom
        self.genRandomChoco(2)
        self.genRandomMother(1)

        #set up mouse
        self.set_mouse_visible(False)

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
                self.score -= 1
                self.heart -= 1
                self.genRandomChoco(2)
                choco.kill()

    def mother_collision(self):
        for mother in self.motherPlayer_list:
            hit_mother = arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.motherPlayer_list)
            for mother in hit_mother:
                mother.kill()
                self.genRandomMother(2)
                self.heart -= 1
            if mother.bottom <= 10:
                self.score += 5
                self.genRandomMother(1)
                mother.kill()

    def heart_collision(self):
        for heart in self.heart_list:
            hit_heart = arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.heart_list)
            for heart in hit_heart:
                heart.kill()
                self.heart += 1
            if heart.bottom <= 10:
                heart.kill()

    def genRandomChoco(self,num):
        for i in range(num):
            choco = Choco("choco.png")
            choco.center_x = random.randrange(20, SCREEN_WIDTH-20)
            choco.center_y = 750
            self.all_sprites_list.append(choco)
            self.choco_list.append(choco)

    def genRandomMother(self,num):
        for i in range(num):
            motherPlayer = MotherPlayer("mother.png")
            motherPlayer.center_x = random.randrange(20, SCREEN_WIDTH-20)
            motherPlayer.center_y = 750
            self.all_sprites_list.append(motherPlayer)
            self.motherPlayer_list.append(motherPlayer)

    def genRandomHeart(self):
        for i in range(1):
            heart = Heart("heart.png")
            heart.center_x = random.randrange(20,SCREEN_WIDTH-20)
            heart.center_y = 750
            self.all_sprites_list.append(heart)
            self.heart_list.append(heart)

    def gameOver(self):
        if self.heart == 0:
            self.endScore = self.score
        if self.heart <= 0:
            return True
    def on_draw(self):
        arcade.start_render()

        if self.gameOver():
            self.bg.draw()
            outputScore = "Score: {}".format(self.endScore)
            arcade.draw_text(outputScore, 170, 300, arcade.color.BLUE, 40)
        else:
            self.all_sprites_list.draw()
            outputScore = "Score: {}".format(self.score)
            outputHeart = "Heart: {}".format(self.heart)
            arcade.draw_text(outputScore, 10, 750, arcade.color.WHITE, 25)
            arcade.draw_text(outputHeart, 350, 750, arcade.color.RED, 25)

    def animate(self,delta_time):
            self.all_sprites_list.update()
            self.choco_collision()
            self.mother_collision()
            self.heart_collision()
            self.gameOver()

            if random.randrange(0, 200) == 1:
                 self.genRandomHeart()

if __name__ == '__main__':
    window = myProject(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_game()
    arcade.run()
