from manim import *
from ..utility.constants import *
from ..utility.utils import *

__all__ = ["Solution"]


class Solution(Scene):
    def __init__(self, md_file, name="Senan", font_size=80, **kwargs):
        super().__init__(**kwargs)
        self.name = (
            Text(name.upper(), font=BOLD_FONT, font_size=font_size, color=TEXT_COLOR)
            .to_edge(DOWN)
            .shift(DOWN * 0.5)
            .scale(0.2)
        )
        self.solution_list = parse_markdown(md_file)

    def construct(self):
        self.add(self.name)

        main_solution, reference = self.get_AB_solution(*self.parse_solution_list())

        maths_tex_mobject = MathTex(*main_solution, color=TEXT_COLOR).shift(UP)

        # Scaling of mobject depending on the space
        frame_width = maths_tex_mobject.width
        frame_height = maths_tex_mobject.height

        ratio_based_on_width = (config.frame_width - 1) / frame_width
        ratio_based_on_height = len(maths_tex_mobject) / frame_height
        scale_ratio = min(ratio_based_on_width, ratio_based_on_height)

        maths_tex_mobject.scale(scale_ratio)

        #  Shift to top after scaling
        maths_tex_mobject.move_to(UP * 3, aligned_edge=UP)

        self.start_animation(maths_tex_mobject, reference)
        self.wait()

    def start_animation(self, maths_mobject, reference, num=3):
        init_location = maths_mobject[0].get_center()
        maths_mobject[0].move_to(ORIGIN)

        count = 3
        active_group = VGroup()
        for i in range(len(maths_mobject)):

            self.play(Write(maths_mobject[i]))
            active_group.add(maths_mobject[i])
            self.wait(1.5)
            if i == 0:
                self.play(
                    maths_mobject[0].animate.move_to(init_location), run_time=1.25
                )
                self.wait(0.5)

            self.play_reference(i, reference, active_group)

            if i != 0 and i % num == 0:
                self.play(
                    *[Unwrite(maths_mobject[i - m], run_time=1) for m in range(num)]
                )
                active_group = VGroup(maths_mobject[0])
                try:
                    location_zero = maths_mobject[0].get_center()
                    location_next = maths_mobject[i + 1].get_center()
                    displacement = (location_zero - location_next)[1]
                    maths_mobject[i + 1 :].shift(UP * displacement)
                    count = i
                except:
                    continue

        if count != len(maths_mobject) - 1:
            self.play(
                *[
                    Unwrite(maths_mobject[i])
                    for i in range(count + 1, len(maths_mobject))
                ],
                run_time=1
            )
        self.play(Unwrite(maths_mobject[0]), run_time=0.5)

    def play_reference(self, index, reference_list, active_mobjects):
        required_list = []

        for idx, refer_mobject in reference_list:
            if idx == index:
                required_list.append(refer_mobject)
        if required_list == []:
            return
        self.play(
            FadeToColor(active_mobjects, SUPPORT_COLOR),
            run_time=0.2,
        )
        for refer_mobject in required_list:
            self.play(
                FadeIn(refer_mobject),
                run_time=0.2,
            )
            self.wait(1.75)
            self.play(
                FadeOut(refer_mobject),
                run_time=0.2,
            )
        self.play(
            FadeToColor(active_mobjects, TEXT_COLOR),
            run_time=0.2,
        )

    def parse_solution_list(self):
        try:
            list_1, list_2 = zip(
                *[(sol[0], sol[1:].strip()) for sol in self.solution_list]
            )
            return list(list_1), list(list_2)
        except:
            print("Error: Encountered, list is empty I guess")
            print("Exiting...")
            sys.exit()

    def get_AB_solution(self, type_list, tex_list):
        main_solution = []
        reference = []
        count = 0
        for i, type_ in enumerate(type_list):
            if type_ == "A":
                main_solution.append(tex_list[i])
            else:
                count += 1
                reference.append(
                    (
                        i - count,
                        MathTex(
                            tex_list[i].strip(), color=TEXT_COLOR, font_size=40
                        ).move_to(DOWN * 2),
                    )
                )

        return main_solution, reference
