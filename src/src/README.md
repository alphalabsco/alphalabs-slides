# Slide Rendering Guide

This directory contains slide animations created with Manim. The `render.sh` script provides a convenient way to render slides without having to manually activate the virtual environment or remember complex commands.

## Installation Prerequisites

Before using the render script, ensure you have:

1. Python and a virtual environment set up with required dependencies
2. Manim Community v0.19.0 installed
3. LaTeX installed (BasicTeX or a full LaTeX distribution)
4. Necessary LaTeX packages: standalone, preview, doublestroke, physics, amsmath, xcolor, dvisvgm

## Using the Render Script

The `render.sh` script simplifies the process of rendering slides by handling virtual environment activation and passing appropriate arguments to the Manim rendering engine.

### Basic Usage

```bash
./render.sh [options] slide_name
```

For example, to render Slide1:

```bash
./render.sh slide1
```

### Available Options

The script supports the following options:

| Option | Description |
|--------|-------------|
| `--high-quality` | Renders the slide in high quality (default is low quality for faster rendering) |
| `--no-preview` | Disables automatic preview of the rendered video (default is to preview) |
| `--list` | Lists all available slides |

### Examples

1. Render Slide1 with default settings (low quality, with preview):
   ```bash
   ./render.sh slide1
   ```

2. Render Slide2 in high quality:
   ```bash
   ./render.sh --high-quality slide2
   ```

3. Render Slide1 without automatically opening the preview:
   ```bash
   ./render.sh --no-preview slide1
   ```

4. List all available slides:
   ```bash
   ./render.sh --list
   ```

5. Render multiple slides at once:
   ```bash
   ./render.sh slide1 slide2
   ```

## Output Location

Rendered videos are saved in the `media/videos/` directory in the appropriate quality subdirectory:
- Low quality: `media/videos/{slide_file}/480p15/`
- High quality: `media/videos/{slide_file}/1080p60/`

## Troubleshooting

If you encounter permission issues with the script, ensure it's executable:

```bash
chmod +x render.sh
```

If LaTeX-related errors occur, you may need to install additional LaTeX packages:

```bash
sudo tlmgr install package_name
```

