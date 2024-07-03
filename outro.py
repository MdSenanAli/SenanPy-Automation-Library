from manim import *
from ..utility.constants import *

__all__ = ["Outro"]


class Outro(Scene):
    def __init__(self, time_duration=10, name="Senan", font_size=80, **kwargs):
        super().__init__(**kwargs)
        self.time_duration = time_duration
        self.name = (
            Text(name.upper(), font=BOLD_FONT, font_size=font_size, color=TEXT_COLOR)
            .to_edge(DOWN)
            .shift(DOWN * 0.5)
            .scale(0.2)
        )

    def construct(self):
        try:
            text = Text(
                "Watch Next".upper(),
                color=TEXT_COLOR,
                font_size=120,
                font=BOLD_FONT,
            ).to_edge(UP)

            factor = 0.4
            rectangle = Rectangle(width=16 * factor, height=9 * factor).shift(
                DOWN * 0.5
            )
            rectangle.set_stroke(color=TEXT_COLOR, width=4)
            self.add(self.name)
            self.play(Write(text), Create(rectangle))
            self.wait(self.time_duration - 2)
            self.play(Unwrite(text), Uncreate(rectangle), Unwrite(self.name))
            self.wait(0.5)
        except:
            print("Time Duration Should Be Greater Than 2")
            print("Exiting...")
            sys.exit()
