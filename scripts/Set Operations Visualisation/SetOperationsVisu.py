from manim import *

config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16  # Ajuster la hauteur du cadre
config.frame_width = 9  # Ajuster la largeur du cadre


class SetOperations(Scene):
    def construct(self):
        # Define circles representing sets
        circle_A = Circle(radius=2, color=BLUE).shift(LEFT * 1.5 + UP *3)
        circle_B = Circle(radius=2, color=RED).shift(RIGHT * 1.5 + UP *3)
        label_A = MathTex("A").next_to(circle_A, UP)
        label_B = MathTex("B").next_to(circle_B, UP)
        title = Text("Set Operations").next_to(VGroup(circle_A, circle_B), UP * 4.5)

        # Show the sets A and B
        self.play(Write(title))
        self.play(Create(circle_A), Create(circle_B), Write(label_A), Write(label_B))
        self.wait(2)

        # Union (A ∪ B)
        union = Union(circle_A, circle_B, color=PURPLE, fill_opacity=0.5)

        # Intersection (A ∩ B)
        inter = Intersection(circle_A, circle_B, color=GREEN, fill_opacity=0.5)

        # Difference (A - B)
        diff = Difference(circle_A, circle_B, color=ORANGE, fill_opacity=0.5)

        # Symmetric Difference (A △ B)
        sym_diff = Exclusion(circle_A, circle_B, color=YELLOW, fill_opacity=0.5)

        # Grouping each operation
        union_group = union.copy().scale(0.4).move_to(DOWN + LEFT * 2.5)
        inter_group = inter.copy().scale(0.6).move_to(DOWN + RIGHT * 2.5)
        diff_group = diff.copy().scale(0.6).move_to(DOWN * 5 + LEFT * 2.5)
        sym_diff_group = sym_diff.copy().scale(0.4).move_to(DOWN * 5 + RIGHT * 2.5)

        union_label = MathTex(r"A \cup B").next_to(union_group, DOWN)
        inter_label = MathTex(r"A \cap B").next_to(inter_group, DOWN)
        diff_label = MathTex("A - B").next_to(diff_group, DOWN)
        sym_diff_label = MathTex(r"A \cup B - A \cap B").next_to(sym_diff_group, DOWN)


        # Display squares and their contents
        self.play(Transform(union, union_group))
        self.play(Write(union_label))
        self.wait(1)
        self.play(Transform(inter, inter_group))
        self.play(Write(inter_label))
        self.wait(1)
        self.play(Transform(diff, diff_group))
        self.play(Write(diff_label))
        self.wait(1)
        self.play(Transform(sym_diff, sym_diff_group))
        self.play(Write(sym_diff_label))

        self.wait(2)
        self.play(FadeOut(
            title, circle_A, circle_B, label_A, label_B,
            union, inter, diff, sym_diff,
            union_group, inter_group, diff_group, sym_diff_group,
            union_label, inter_label, diff_label, sym_diff_label
        ))


