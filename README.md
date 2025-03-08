# AlphaLabs Slides

This project contains mathematical slide animations created with Manim.

## Prerequisites

To run this project, you need to install:

1. Python 3.7 or higher
2. Manim Community Edition

## Installation

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Manim
pip install manim

# Install additional dependencies (if needed)
pip install numpy
```

## Project Structure

- `src/slides.py`: Contains the slide animations
  - `Slide1`: Mathematical function graph animation
  - `Slide2`: Network graph visualization

## Running the Slides

To render the slides with low quality (for faster previewing):

```bash
# Render Slide 1
manim -pql src/slides.py Slide1

# Render Slide 2
manim -pql src/slides.py Slide2
```

For higher quality renders:

```bash
# Render Slide 1 in high quality
manim -pqh src/slides.py Slide1

# Render Slide 2 in high quality
manim -pqh src/slides.py Slide2
```

## Slide Descriptions

### Slide 1: Graph Analysis
- Shows a parabola function (f(x) = x²)
- Animates transformation to f(x) = 0.5x²
- Highlights key points on the graph

### Slide 2: Network Graph
- Visualizes a network with 6 nodes and 8 connections
- Animates a path through the network
- Changes node colors to show activation

## Output

The rendered videos will be saved in the `media/videos/` directory.