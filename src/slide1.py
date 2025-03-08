from manim import *

class Slide1(Scene):
    def construct(self):
        # Main title
        title = Text("Series on Effective AI Assisted Development for Teams", font_size=36)
        title.to_edge(UP, buff=0.5)
        
        # Topic subtitle with highlight color
        topic = Text("Problem Decomposition", font_size=44, color=BLUE)
        topic.next_to(title, DOWN, buff=0.4)
        
        # Create a decorative line under the topic
        underline = Line(
            start=LEFT * 4,
            end=RIGHT * 4,
            color=BLUE_B
        ).next_to(topic, DOWN, buff=0.3)
        
        # Creator and presenter information in corners
        creator = Text("Created by: AlphaLabs", font_size=24)
        presenter = Text("Presenter: Mark Avdi", font_size=24)
        
        # Position creator in bottom-left corner
        creator.to_corner(DOWN + LEFT, buff=0.5)
        
        # Position presenter in bottom-right corner
        presenter.to_corner(DOWN + RIGHT, buff=0.5)
        
        # Add a key point about problem decomposition
        key_point = Text("Breaking complex problems into manageable parts", 
                        font_size=26, color=GREEN)
        key_point.to_edge(DOWN, buff=2.0)
        
        # Animations for a smooth presentation
        # More dynamic animations with reduced run times
        self.play(AddTextLetterByLetter(title, run_time=0.5))
        self.wait(0.2)
        
        # Using Transform with a starting object for the topic
        topic_start = topic.copy().scale(0.8).set_opacity(0)
        self.add(topic_start)
        self.play(Transform(topic_start, topic, run_time=0.4))
        self.remove(topic_start)
        self.add(topic)
        
        self.play(Create(underline, run_time=0.3))
        self.wait(0.2)
        
        # Simultaneous animations for creator and presenter using FadeIn with shift
        self.play(
            FadeIn(creator, shift=LEFT*0.5, run_time=0.3),
            FadeIn(presenter, shift=RIGHT*0.5, run_time=0.3),
        )
        self.wait(0.2)
        
        # More interesting animation for the key point
        self.play(GrowFromCenter(key_point, run_time=0.4))
        self.wait(0.5)

# To render this slide:
# manim -pql slide1.py Slide1

