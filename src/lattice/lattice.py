from manim import *
import numpy as np

class LatticeContruction(Scene):
    def construct(self):
        TICK_SCALE=.3
        origin_dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [0, 0, 0], buff=0, color=BLUE, stroke_width=3)
        numberplane = NumberPlane(
            x_min=-10,
            x_max=10,
            y_min=-10,
            y_max=10,
            x_line_frequency=TICK_SCALE,
            y_line_frequency=TICK_SCALE,
            x_axis_config=None,
            y_axis_config=None,
            center_point=ORIGIN,
            number_scale_val=.1,
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "number_scale_val": .01,
                # "x_range":[0, 30, 1],
                # "y_range":[0, 30, 1],
            },
            # x_length=1,
            # y_length=1,
            # background_line_style={
            #     "stroke_color": TEAL,
            #     "stroke_width": 4,
            #     "stroke_opacity": 0.6
            # }
        )
        
        origin_text = Text('(0, 0)').next_to(origin_dot, DOWN)
        
        self.add(numberplane, origin_dot, arrow, origin_text)
        # numberplane.to_corner(DL)

        arrow1 = Arrow(ORIGIN, [0, 0, 0], buff=0, color=BLUE, stroke_width=2)
        arrow2 = Arrow(ORIGIN, [0, 0, 0], buff=0, color=RED, stroke_width=2)
        arrow1.
        self.play(Transform(arrow, Arrow(ORIGIN, [3*TICK_SCALE, 2*TICK_SCALE, 0], buff=0, color=BLUE, stroke_width=3)))
        # tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        # self.add(tip_text)
        self.wait(2)