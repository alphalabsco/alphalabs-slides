from manim import *

class Slide2(Scene):
    def construct(self):
        # Title
        title = Text("Network Graph Visualization", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create network graph
        vertices = [
            [-3, -1, 0], [-1, 1, 0], [1, 1, 0], [3, -1, 0], 
            [-1, -2, 0], [1, -2, 0]
        ]
        
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 5), (5, 4), (4, 0),
            (1, 5), (2, 4)
        ]
        
        # Create a vertex group
        vertex_dots = VGroup(*[Dot(point=np.array(vertex), radius=0.2) for vertex in vertices])
        
        # Add labels
        labels = VGroup(
            *[Text(f"{i+1}", font_size=20).move_to(vertex_dots[i].get_center()) 
              for i in range(len(vertices))]
        )
        
        # Create the edges
        edge_lines = VGroup(
            *[Line(
                vertex_dots[edge[0]].get_center(), 
                vertex_dots[edge[1]].get_center()
            ).set_stroke(BLUE, 2) for edge in edges]
        )
        
        # Display the network
        self.play(Create(edge_lines), run_time=2)
        self.play(Create(vertex_dots), Write(labels), run_time=1.5)
        self.wait()
        
        # Highlight path through network
        path_edges = [0, 1, 2, 3]  # Indices of edges to highlight
        highlighted_path = VGroup(
            *[edge_lines[i].copy().set_stroke(YELLOW, 4) for i in path_edges]
        )
        
        self.play(Create(highlighted_path), run_time=2)
        self.wait()
        
        # Change vertex colors to show activation
        self.play(
            vertex_dots[0].animate.set_color(YELLOW),
            vertex_dots[1].animate.set_color(YELLOW),
            vertex_dots[2].animate.set_color(YELLOW),
            vertex_dots[3].animate.set_color(YELLOW),
            run_time=1.5
        )
        self.wait(2)

# To render this slide:
# manim -pql slide2.py Slide2

