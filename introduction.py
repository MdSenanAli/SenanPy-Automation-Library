from manim import *
from ..utility.constants import *

__all__ = ["Introduction"]


class Introduction(Scene):
    def __init__(self, name="Senan", font_size=80, **kwargs):
        super().__init__(**kwargs)
        self.name = Text(
            name.upper(), font=BOLD_FONT, font_size=font_size, color=TEXT_COLOR
        )

    def construct(self):
        self.wait(0.5)
        self.play(Write(self.name))
        self.wait(0.5)
        self.play(self.name.animate.to_edge(DOWN).shift(DOWN * 0.5).scale(0.2))
