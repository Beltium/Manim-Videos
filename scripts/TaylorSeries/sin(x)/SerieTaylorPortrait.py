from manim import *
import numpy as np

config.pixel_height = 3840
config.pixel_width = 2160
# config.frame_height = 12  # Ajuster la hauteur du cadre
# config.frame_width = 20  # Ajuster la largeur du cadre

class SinTaylorSeriesPortrait(Scene):
    def construct(self):
        # Configuration des axes
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-10, 11, 2)},
            y_axis_config={"numbers_to_include": np.arange(-1, 2, 1)},
            y_length=5
        ).shift(DOWN * 1.25)  # Déplacer les axes vers le bas
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Fonction sin(x)
        sin_graph = axes.plot(np.sin, color=RED, x_range=[-10, 10])
        sin_label = axes.get_graph_label(sin_graph, label="\\sin(x)")

        # Ajouter les axes et le graphe de sin(x)
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sin_graph), Write(sin_label))
        self.wait(1)  # Réduit le temps d'attente initial

        # Série de Taylor de sin(x)
        taylor_series = [
            lambda x: x,
            lambda x: x - x ** 3 / np.math.factorial(3),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(7),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(
                7) + x ** 9 / np.math.factorial(9),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(
                7) + x ** 9 / np.math.factorial(9) - x ** 11 / np.math.factorial(11),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(
                7) + x ** 9 / np.math.factorial(9) - x ** 11 / np.math.factorial(11) + x ** 13 / np.math.factorial(13),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(
                7) + x ** 9 / np.math.factorial(9) - x ** 11 / np.math.factorial(11) + x ** 13 / np.math.factorial(
                13) - x ** 15 / np.math.factorial(15),
            lambda x: x - x ** 3 / np.math.factorial(3) + x ** 5 / np.math.factorial(5) - x ** 7 / np.math.factorial(
                7) + x ** 9 / np.math.factorial(9) - x ** 11 / np.math.factorial(11) + x ** 13 / np.math.factorial(
                13) - x ** 15 / np.math.factorial(15) + x ** 17 / np.math.factorial(17),
        ]

        # Termes de la série de Taylor
        taylor_terms = [
            "x",
            "x - \\frac{x^3}{3!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!} + \\frac{x^{13}}{13!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!} + \\frac{x^{13}}{13!} - \\frac{x^{15}}{15!}",
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!} + \\frac{x^{13}}{13!} - \\frac{x^{15}}{15!} + \\frac{x^{17}}{17!}"
        ]

        # Initialisation du texte et du graphe
        taylor_text = MathTex("\\sin(x) \\approx x").to_edge(UP)
        taylor_graph = axes.plot(taylor_series[0], color=YELLOW, x_range=[-10, 10])

        self.play(Write(taylor_text), Create(taylor_graph))
        self.wait(1)  # Réduit le temps d'attente initial

        # Ajouter les termes un par un avec l'animation
        for i in range(1, len(taylor_terms)):
            new_text = MathTex(f"\\sin(x) \\approx {taylor_terms[i]}").to_edge(UP)
            new_graph = axes.plot(taylor_series[i], color=YELLOW, x_range=[-10, 10])

            self.play(Transform(taylor_text, new_text), Transform(taylor_graph, new_graph))
            self.wait(0.5)  # Accélère l'ajout des termes

        # Affichage de la somme exacte de la série de Taylor
        sum_exact = MathTex(
            "\\sin(x) = \\sum_{n=0}^{\\infty} \\frac{(-1)^n x^{2n+1}}{(2n+1)!}"
        ).to_edge(UP)
        self.play(Transform(taylor_text, sum_exact))

        # Adaptation du graphe pour montrer la série complète
        full_series_graph = axes.plot(np.sin, color=YELLOW, x_range=[-10, 10])
        self.play(Transform(taylor_graph, full_series_graph))
        self.wait(2)  # Attendre un peu avant de finir


if __name__ == "__main__":
    scene = SinTaylorSeriesPortrait()
    scene.render()

