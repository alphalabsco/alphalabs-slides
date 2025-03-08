# AlphaLabs Slides

This directory contains slide presentations created with [Manim](https://www.manim.community/), a mathematical animation engine.

## Quick Start

To render slides, use the `render.sh` script provided in this directory:

```bash
./render.sh slide1
```

This will render Slide1 with default settings (low quality, with preview).

## Using render.sh

The `render.sh` script simplifies the process of rendering slides by handling virtual environment activation and managing Manim parameters.

### Basic Usage

```bash
./render.sh <slide_name>
```

Where `<slide_name>` is the name of the slide file without the `.py` extension (e.g., `slide1` for `slide1.py`).

### Available Options

| Option | Description |
|--------|-------------|
| `--high-quality` | Renders slides in high quality (default is low quality for faster rendering) |
| `--no-preview` | Disables automatic preview of the rendered video |
| `--list` | Lists all available slides |

### Examples

1. Render slide1 with default settings (low quality, with preview):
   ```bash
   ./render.sh slide1
   ```

2. Render slide2 in high quality:
   ```bash
   ./render.sh --high-quality slide2
   ```

3. Render slide1 without automatically opening the preview:
   ```bash
   ./render.sh --no-preview slide1
   ```

4. List all available slides:
   ```bash
   ./render.sh --list
   ```

5. Render multiple slides:
   ```bash
   ./render.sh slide1 slide2
   ```

## Creating New Slides

Each slide should be created as a separate Python file (e.g., `slide3.py`) with a class that extends the Manim `Scene` class. After creating a new slide file, you can render it using the same `render.sh` script.

## Slide Output

Rendered slides are saved in the `media/videos/` directory in a subfolder corresponding to the slide name and quality setting.

Default low-quality output: `media/videos/<slide_name>/480p15/<Slide_class_name>.mp4`
High-quality output: `media/videos/<slide_name>/1080p60/<Slide_class_name>.mp4`

## Troubleshooting

If you encounter any issues with the render.sh script:

1. Ensure it has executable permissions: `chmod +x render.sh`
2. Check that your virtual environment is properly set up with Manim installed
3. Verify that your slide files follow the correct Manim scene structure

