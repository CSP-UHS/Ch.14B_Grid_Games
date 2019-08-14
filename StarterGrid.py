import arcade

SW = 500
SH = 600

class MyGame(arcade.Window):

    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):

        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

def main():

    window = MyGame(SW, SH, "Starter Grid Game")
    arcade.run()

if __name__ == "__main__":
    main()
