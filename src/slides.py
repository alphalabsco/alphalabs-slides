from manim import *
import sys
import argparse
import os
import subprocess
from slide1 import Slide1
from slide2 import Slide2

# Dictionary mapping slide names to their classes
SLIDES = {
    "slide1": Slide1,
    "slide2": Slide2
}

def render_slide(slide_name, preview=True, low_quality=True, low_res=True):
    """
    Render a specific slide with the given options using the manim command-line interface.
    
    Args:
        slide_name: Name of the slide (slide1, slide2)
        preview: Whether to preview the slide after rendering
        low_quality: Whether to use low quality for faster rendering
        low_res: Whether to use lower resolution (480p15)
    
    Note:
        Uses the syntax for Manim Community v0.19.0+: 'manim [file] [scene] [options]'
        Quality flag (-q) should be followed by a quality level (l, m, h, p, k)
    """
    if slide_name not in SLIDES:
        print(f"Error: Slide '{slide_name}' not found. Available slides: {', '.join(SLIDES.keys())}")
        return False
    
    # Get the slide class name
    slide_class = SLIDES[slide_name].__name__
    
    # Determine which module file contains the slide class
    module_file = f"{slide_name}.py"
    
    # Build manim command with appropriate flags
    command = ["manim", module_file, slide_class]
    
    # Add flags based on options
    flags = []
    if preview:
        flags.append("-p")
    
    # Add quality flag with appropriate level
    if low_quality:
        flags.append("-q")
        flags.append("l")  # 'l' for low quality
    else:
        flags.append("-q")
        flags.append("h")  # 'h' for high quality
    
    # Add all flags at once to avoid misinterpretation
    command.extend(flags)
    
    # Convert command list to string for logging, with quotes around file paths
    command_str = ' '.join(command)
    print(f"Executing: {command_str}")
    
    # Execute the manim command
    try:
        result = subprocess.run(command, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error executing manim command: {e}")
        return False

def list_slides():
    """List all available slides"""
    print("Available slides:")
    for name, slide_class in SLIDES.items():
        # Extract the slide description from the first text element in the class
        try:
            # Create a temporary instance to get the description
            slide = slide_class()
            description = "No description available"
            
            # Try to find a title or description in the construct method
            try:
                # Check if there's a title attribute in the class
                for name, attr in slide_class.__dict__.items():
                    if "title" in name.lower() and isinstance(attr, str):
                        description = attr
                        break
            except:
                pass
                
            print(f"  - {name}: {description}")
        except:
            print(f"  - {name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render slides for AI Assisted Development presentation")
    
    # Add arguments
    parser.add_argument("slide", nargs="?", help="Name of the slide to render (slide1, slide2, etc.)")
    parser.add_argument("--list", "-L", action="store_true", help="List all available slides")
    parser.add_argument("--no-preview", action="store_true", help="Don't preview the slide after rendering")
    parser.add_argument("--high-quality", action="store_true", help="Use high quality rendering (slower)")
    parser.add_argument("--high-res", action="store_true", help="Use high resolution (1080p instead of 480p)")
    
    args = parser.parse_args()
    
    # If --list is specified, list all slides and exit
    if getattr(args, 'list', False):
        list_slides()
        sys.exit(0)
    
    # If no slide is specified, show help
    if not args.slide:
        parser.print_help()
        print("\nAvailable slides:")
        for slide_name in SLIDES.keys():
            print(f"  - {slide_name}")
        sys.exit(1)
    
    # Render the specified slide
    preview = not args.no_preview
    low_quality = not args.high_quality
    low_res = not args.high_res
    
    success = render_slide(args.slide, preview, low_quality, low_res)
    sys.exit(0 if success else 1)
