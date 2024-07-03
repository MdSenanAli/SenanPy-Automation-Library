from manim import *
from manim.camera.camera import Camera
from ..utility.constants import *
from ..utility.utils import *

__all__ = ["Thumbnail"]


class Thumbnail(Scene):
    def __init__(self, heading="heading", md_file=MARKDOWN_01, **kwargs):
        super().__init__(**kwargs)
        self.question = parse_markdown(md_file)[0][2:]
        self.question_tex = MathTex(self.question, color=TEXT_COLOR).scale_to_fit_width(
            config.frame_width - 1
        )

        self.heading_tex = Text(heading.upper(), font=BOLD_FONT, color=TEXT_COLOR)

    def construct(self):
        self.heading_tex.scale_to_fit_width(self.question_tex.width)

        # arrange them
        self.question_tex.next_to(self.heading_tex, DOWN).shift(DOWN)

        grp = VGroup(self.question_tex, self.heading_tex)
        grp.scale_to_fit_width(config.frame_width - 1)
        if grp.height >= config.frame_height - 1:
            grp.scale_to_fit_height(config.frame_height - 1)

        grp.move_to(ORIGIN)
        self.add(self.question_tex, self.heading_tex)
