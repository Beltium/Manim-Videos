from manim import *

config.pixel_height = 2160
config.pixel_width = 3840
# # config.frame_height = 12  # Ajuster la hauteur du cadre
# # config.frame_width = 20  # Ajuster la largeur du cadre

class LinearFunction(Scene):
    def construct(self):
        # Configuration de la scène
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Initialisation des coefficients a et b
        a = ValueTracker(1)
        b = ValueTracker(0)

        # Définition de la fonction linéaire en fonction de a et b
        function = always_redraw(lambda: axes.plot(lambda x: a.get_value() * x + b.get_value(), color=RED))
        # function_label = always_redraw(lambda: axes.get_graph_label(function, label="ax+b"))
        function_label = MathTex("y = ", "ax+b").to_corner(UR).set_color_by_tex("ax+b", RED)

        # Affichage des coefficients a et b
        a_text = always_redraw(lambda: MathTex(f'a = {a.get_value():.2f}').to_corner(UL))
        b_text = always_redraw(lambda: MathTex(f'b = {b.get_value():.2f}').next_to(a_text, DOWN, aligned_edge=LEFT))

        # Ajout des éléments à la scène
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(function), Write(function_label))
        self.play(Write(a_text), Write(b_text))

        # Animation de la variation des coefficients a et b
        self.play(a.animate.set_value(2), run_time=3)
        self.play(b.animate.set_value(-2), run_time=3)
        self.play(a.animate.set_value(0.5), b.animate.set_value(1), run_time=3)
        self.wait(2)