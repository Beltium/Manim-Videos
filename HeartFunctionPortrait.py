from manim import *
import numpy as np

config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16  # Ajuster la hauteur du cadre
config.frame_width = 9  # Ajuster la largeur du cadre

class HeartFunctionPortrait(Scene):
    def construct(self):
        # Configuration de la scène
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2, 3, 1],
            axis_config={"color": BLUE},
            y_length=8,
            x_length=8
        ).shift(UP * 1.5)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        k = ValueTracker(0)

        def heartFunction(x, k):
            f1 = np.cbrt(x) ** 2
            f2 = 0.9 * ((3.3 - x ** 2) ** (1 / 2))
            f3 = np.sin(np.pi * x * k)
            return f1 + f2 * f3

        function = always_redraw(lambda: axes.plot(lambda x: heartFunction(x, k.get_value()),color=PINK, x_range=[-1.8165, 1.8165, 0.001]))
        # function_label = always_redraw(lambda: axes.get_graph_label(function, label="ax+b"))
        function_label = MathTex("y = ", r"x^{\frac{2}{3}} + 0.9 \left(3.3-x^2\right)^{\frac{1}{2}} \times \sin{\left(k.\pi.x\right)}").next_to(axes, DOWN).set_color_by_tex(r"x^{\frac{2}{3}} + 0.9 \left(3.3-x^2\right)^{\frac{1}{2}} \times \sin{\left(k.\pi.x\right)}", PINK)

        k_text = always_redraw(lambda: MathTex('k =', f'{k.get_value():.2f}').next_to(function_label, DOWN).set_color_by_tex(f'{k.get_value():.2f}', PINK))
        title = Text("The Heart Function").set_color(PINK).next_to(axes, UP * 4)

        # Ajout des éléments à la scène
        self.play(Write(title))
        self.play(Create(axes), Write(axes_labels))
        self.play(Write(function), Write(function_label))
        self.play(Write(k_text))

        # Animation de la variation des coefficients a et b
        self.play(k.animate.set_value(10), run_time=7)
        self.wait(2)
        self.play(FadeOut(axes, axes_labels, function, function_label, k_text, title))