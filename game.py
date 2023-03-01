from . import main_settings as settings
import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(settings.WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.state = True
        self.loop = None
        self.loop_args = None
        self.loop_kwargs = None

        self.screen_color = settings.DEFAULT_SCREEN_COLOR

        self.post_init()

    def post_init(self):
        self.update_title()

    def stop(self):
        """Break a main game loop"""
        self.state = False

    def update_title(self):
        """Update window title with string from settings"""
        pg.display.set_caption(settings.WINDOW_TITLE)

    def set_loop(self, func, *args, **kwargs):
        """Set func with your game logic for call it in loop"""
        self.loop = func
        self.loop_args = args
        self.loop_kwargs = kwargs

    def get_screen(self):
        """return main screen instance"""
        return self.screen

    def get_clock(self):
        """return main clock instance"""
        return self.clock

    def run(self):
        """Start a main game loop"""
        while self.state:
            self.loop(*self.loop_args, **self.loop_kwargs)
            pg.display.flip()
            self.clock.tick(settings.FPS)

    def __del__(self):
        pg.quit()

if __name__ == "__main__":
    g = Game()

    print(dir(settings))
