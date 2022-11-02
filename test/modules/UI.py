from modulepy.Base import Base, Information, Version
from modulepy import log

from pyray import *


class UI(Base):
    information = Information("TestUI", Version(1, 0, 0))
    dependencies = [Information("Manager", Version(1, 0, 0)), Information("GPS", Version(1, 0, 0))]

    def on_start(self):
        log.debug("Initializing window")
        init_window(800, 600, "TestUI")
        set_target_fps(30)
        self.data.text = "init text"

    def on_stop(self):
        log.debug("Closing window")
        close_window()

    def work(self):
        error = self.clients["GPS"].get("error")

        if error is None:
            error = "None"

        begin_drawing()
        clear_background(BLACK)

        draw_text(error, 100, 100, 24, GREEN)
        if not error:
            draw_text("Client is not connected", 100, 120, 18, RED)
        else:
            draw_text("Connected client", 100, 120, 18, GREEN)

        end_drawing()

        tmp = window_should_close()
        self.data.set("do_run", not tmp)
        if tmp:
            print("Setting manager do_run to false")
            self.clients["Manager"].set("do_run", False)
