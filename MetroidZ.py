"""
Example showing how to draw text to the screen using Text objects.
This is much faster than using draw_text

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_text_objects
"""
import arcade
import math

SCREEN_WIDTH = 1320
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Drawing Text Example"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class Nave_Sprite_Front(arcade.Sprite):
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.texture = arcade.load_texture("sprites/Cutscenes_Introduction.png", x=243*5, y=3*5, height=42*5, width=142*5)
        self.hit_box = self.texture._hit_box_points
        self.sin_list = [0]*360
        for index, seno in enumerate(self.sin_list):
            self.sin_list[index] = math.sin(2*math.pi*index*1.0/360.0)

        print(self.sin_list)

class Typer():
    def __init__(self, texto = None, start_x=0, start_y=0, fps=1):
        self.texto = texto
        self.index = 0
        self.start_x = start_x
        self.start_y = start_y
        self.cursor = "_"
        self.render_text()
        self.fps = fps
        self.fps_counter = 0

    def render_text(self):
        self.texto_render = arcade.Text(
            self.texto[:self.index]+self.cursor,
            self.start_x,
            self.start_y,
            arcade.color.WHITE_SMOKE,
            DEFAULT_FONT_SIZE * 2,
            width=SCREEN_WIDTH,
            align="left",
        )
    def update(self):
        if self.fps_counter >= self.fps/2:
            self.cursor = "_"
        else:
            self.cursor = " "

        if self.fps_counter >= self.fps:
            self.fps_counter = 0
            self.index += 1
        else:
            self.fps_counter+=1
        self.render_text()  

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.typer = Typer("EMERGENCY ORDER", 300,400,12)
        self.background_color = arcade.color.BLACK_OLIVE
        self.background = arcade.load_texture("sprites/Cutscenes_Introduction.png", x=1*5,y=1*5,width=240*5, height=160*5)
        self.fps_counter = 0
        self.nave = Nave_Sprite_Front()
        self.nave.center_x = SCREEN_WIDTH/2
        # self.nave.center_y = SCREEN_HEIGHT/2
        self.nave.bottom = 100
        self.nave.scale = 0.01
    def on_update(self, delta_time):
        
        self.typer.update()
        self.fps_counter+=1
        if self.fps_counter >301 and self.fps_counter<= 600:
            self.nave.scale = self.nave.scale+0.01
            self.nave.bottom += self.nave.sin_list[self.fps_counter%360]*5

            


    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        if self.fps_counter >0 and self.fps_counter<= 300:
             self.typer.texto_render.draw()
        if self.fps_counter >301 and self.fps_counter<= 600:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT,
                                                self.background)
            self.nave.draw()
            
        

        

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()