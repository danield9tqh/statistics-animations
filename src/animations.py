from manim import *
from dice_stats import dice_rolls
from charting import bar_chart_data
import numpy as np

class SingleDiceRollDistribution(Scene):
    def construct(self):
        rolls = dice_rolls(10000)
        rolls_to_animate = np.concatenate((
            np.arange(10, min(100, len(rolls)+1), 10),
            np.arange(100, min(200, len(rolls)+1), 50),
            np.arange(200, min(1000, len(rolls)+1), 100),
            np.arange(1000, min(10001, len(rolls)+1), 1000),
        ))

        scene_data = [
            (bar_chart_data(rolls[:i], 1, 6, density=True), i)
            for i in rolls_to_animate
        ]

        scene_objects = [
            (
                BarChart(
                    chart_data,
                    max_value=1,
                    bar_names=labels,
                    label_y_axis=True
                ),
                DecimalNumber(i, num_decimal_places=0).to_edge(RIGHT)
            )
            for ((chart_data, labels), i) in scene_data
        ]

        chart_object, number_object = scene_objects[0]
        title = Text("Distribution of dice rolls").to_edge(UP)
        self.add(chart_object, number_object, title)

        self.wait(1)
        for (chart, number) in scene_objects[1:]:
            perc_through = (number.get_value()/len(rolls))
            print(perc_through)
            run_time = .6 - (.5)*perc_through
            self.play(
                Transform(number_object, number, run_time=.01),
                Transform(
                    chart_object,
                    chart,
                    rate_func=rate_functions.linear,
                    run_time=run_time,
                )
            )