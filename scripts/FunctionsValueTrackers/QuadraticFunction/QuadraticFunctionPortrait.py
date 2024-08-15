from manim import *

config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16  # Ajuster la hauteur du cadre
config.frame_width = 9  # Ajuster la largeur du cadre

class QuadraticFunctionPortrait(Scene):
    def construct(self):
        # Configuration de la scène
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": BLUE},
            x_length=8,
            y_length=10
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Initialisation des coefficients a, b et c
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(0)

        # Définition de la fonction linéaire en fonction de a, b et c
        function = always_redraw(lambda: axes.plot(lambda x: a.get_value() * x**2 + b.get_value() * x + c.get_value(), color=RED))
        # function_label = always_redraw(lambda: axes.get_graph_label(function, label="ax^2 + bx + c"))
        function_label = MathTex("y = ", "ax^2 + bx + c").to_corner(UR).set_color_by_tex("ax^2 + bx + c", RED)

        # Affichage des coefficients a, b et c
        a_text = always_redraw(lambda: MathTex(f'a = {a.get_value():.2f}').to_corner(UL))
        b_text = always_redraw(lambda: MathTex(f'b = {b.get_value():.2f}').next_to(a_text, DOWN, aligned_edge=LEFT))
        c_text = always_redraw(lambda: MathTex(f'c = {c.get_value():.2f}').next_to(b_text, DOWN, aligned_edge=LEFT))

        # Ajout des éléments à la scène
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(function), Write(function_label))
        self.play(Write(a_text))
        self.play(Write(b_text))
        self.play(Write(c_text))

        # Animation de la variation des coefficients a, b et c
        self.play(a.animate.set_value(4), run_time=2)
        self.play(a.animate.set_value(-0.1), b.animate.set_value(-1), run_time=3)
        self.play(a.animate.set_value(-0.5), b.animate.set_value(2), c.animate.set_value(2), run_time=3)
        self.wait(1)

        self.play(FadeOut(axes, axes_labels, function, function_label, a_text, b_text, c_text))