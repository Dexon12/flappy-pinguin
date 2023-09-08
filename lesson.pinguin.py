import arcade
from random import *
class Window(arcade.Window):
    def __init__(self):
        super().__init__(1000,600,"Flappy pinguin")
        self.BG = arcade.load_texture("space.png")
        self.penguin_1 = Penguin()
        self.column_list = arcade.SpriteList()
        self.column_2_list = arcade.SpriteList()
        self.stop = False
        self.score = 0
        for i in range(5):
            column = Top_column()
            column.center_x = i * 200 + 1000
            column.center_y = randint(500,650)
            self.column_list.append(column)

        
            column_2 = Bottom_column()
            column_2.center_x = i *200 + 1000
            column_2.center_y = column.center_y - 500
            self.column_2_list.append(column_2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(500,300,1000,600,self.BG)
        self.penguin_1.draw()
        self.column_list.draw()
        self.column_2_list.draw()
        arcade.draw_text(f"Счет: {self.score}",50,550,arcade.color.WHITE,20)
    def update(self,delta_time):
        if self.stop == True:
            quit()
        if self.stop == False:
            list_1 = arcade.check_for_collision_with_list(self.penguin_1,self.column_list)
            if len(list_1) > 0:
                self.stop = True
                
            list_2 = arcade.check_for_collision_with_list(self.penguin_1,self.column_2_list)
            if len(list_2) > 0:
                self.stop = True
            if self.penguin_1.center_y <= 0:
                self.stop = True
            self.penguin_1.update_animation()
            self.penguin_1.center_y += self.penguin_1.change_y
            self.penguin_1.change_y -= 0.2
            if self.penguin_1.center_y >= 600:
                self.penguin_1.center_y = 600

            self.column_list.update()
            self.column_2_list.update()
            for i in range(5):
                if self.column_list[i].center_x <= 0:
                    self.column_list[i].center_x = 1000
                    self.column_list[i].center_y = randint(500,650)
                    self.score += 1
                    
                    self.column_2_list[i].center_x = 1000
                    self.column_2_list[i].center_y = self.column_list[i].center_y - 500
                
            
        
        
    def on_key_press(self,key,modifiers):
        if key == arcade.key.SPACE:
            self.penguin_1.change_y = 5
class Penguin(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()
        cadr = arcade.AnimationKeyframe(0,200,arcade.load_texture("penguin1.png"))
        self.frames.append(cadr)
        cadr_2 = arcade.AnimationKeyframe(1,200,arcade.load_texture("penguin2.png"))
        self.frames.append(cadr_2)
        cadr_3 = arcade.AnimationKeyframe(2,200,arcade.load_texture("penguin3.png"))
        self.frames.append(cadr_3)
        self.scale = 1.5
        self.center_x = 100
        self.center_y = 300
            
class Top_column(arcade.Sprite):
    def __init__(self):
        super().__init__("column_top.png", 1.5)
        self.change_x = -2
    def update(self):
        self.center_x += self.change_x
        
        
        
        

class Bottom_column(arcade.Sprite):
    def __init__(self):
        super().__init__("column_bottom.png", 1.5)
        self.change_x = -2
    def update(self):
        self.center_x += self.change_x
        




























window = Window()
arcade.run()
