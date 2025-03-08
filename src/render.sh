#!/bin/bash

# Script to render slides easily

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Default options
QUALITY="l"
PREVIEW=true

# Function to show usage information
function show_usage {
  echo "Usage: ./render.sh [OPTIONS] SLIDE_NAME [SLIDE_NAME...]"
  echo ""
  echo "Options:"
  echo "  --high-quality    Render in high quality (default is low quality)"
  echo "  --no-preview      Don't preview the rendered slide"
  echo "  --help            Show this help message"
  echo ""
  echo "Examples:"
  echo "  ./render.sh slide1                   # Render slide1 in low quality with preview"
  echo "  ./render.sh --high-quality slide2    # Render slide2 in high quality with preview"
  echo "  ./render.sh slide1 slide2            # Render both slide1 and slide2"
  echo ""
  exit 1
}

# Process command line arguments
SLIDES=()
while [[ $# -gt 0 ]]; do
  case $1 in
    --high-quality)
      QUALITY="h"
      shift
      ;;
    --no-preview)
      PREVIEW=false
      shift
      ;;
    --help)
      show_usage
      ;;
    *)
      SLIDES+=("$1")
      shift
      ;;
  esac
done

# Check if any slides were specified
if [ ${#SLIDES[@]} -eq 0 ]; then
  echo "Error: No slides specified."
  show_usage
fi

# Activate the virtual environment and go to the source directory
cd "$PROJECT_DIR" && source venv/bin/activate && cd src

# Render each slide
for SLIDE in "${SLIDES[@]}"; do
  echo "Rendering $SLIDE..."
  
  # Build the command with appropriate flags
  CMD="python slides.py $SLIDE"
  
  # Add quality flag
  if [ "$QUALITY" = "h" ]; then
    CMD="$CMD --high-quality"
  fi
  
  # Add preview flag if needed
  if ! $PREVIEW; then
    CMD="$CMD --no-preview"
  fi
  
  # Execute the command
  echo "Executing: $CMD"
  eval "$CMD"
done

echo "All slides rendered successfully."

