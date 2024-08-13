from manim import *
import numpy as np

config.pixel_height = 2160
config.pixel_width = 3840
# # config.frame_height = 12  # Ajuster la hauteur du cadre
# # config.frame_width = 20  # Ajuster la largeur du cadre

class HeartFunction(Scene):
    def construct(self):
        # Configuration de la scène
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 3, 1],
            axis_config={"color": BLUE},
            y_length=5
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        k = ValueTracker(0)

        def heartFunction(x, k):
            f1 = np.cbrt(x) ** 2
            f2 = 0.9 * ((3.3 - x ** 2) ** (1 / 2))
            f3 = np.sin(np.pi * x * k)
            return f1 + f2 * f3

        function = always_redraw(lambda: axes.plot(lambda x: heartFunction(x, k.get_value()),color=PINK, x_range=[-1.8165, 1.8165, 0.001]))
        # function_label = always_redraw(lambda: axes.get_graph_label(function, label="ax+b"))
        function_label = MathTex("y = ", r"x^{\frac{2}{3}} + 0.9 \left(3.3-x^2\right)^{\frac{1}{2}} \times \sin{\left(k.\pi.x\right)}").to_edge(DOWN).set_color_by_tex(r"x^{\frac{2}{3}} + 0.9 \left(3.3-x^2\right)^{\frac{1}{2}} \times \sin{\left(k.\pi.x\right)}", PINK)

        k_text = always_redraw(lambda: MathTex('k =', f'{k.get_value():.2f}').to_edge(UP).set_color_by_tex(f'{k.get_value():.2f}', PINK))


        # Ajout des éléments à la scène
        self.play(Create(axes), Write(axes_labels))
        self.play(Write(function), Write(function_label))
        self.play(Write(k_text))

        # Animation de la variation des coefficients a et b
        self.play(k.animate.set_value(10), run_time=7)
        self.wait(2)
        self.play(FadeOut(axes, axes_labels, function, function_label, k_text))