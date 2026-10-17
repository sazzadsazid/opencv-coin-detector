# OpenCV Coin Detector

This project detects and counts coins in an image using OpenCV contour
processing. The sample input contains four coins, and the included output
image shows the detected coin boundaries and count.

## How it works

1. Loads `coin.jpg`.
2. Crops the region containing the coin tray.
3. Applies Gaussian blur to reduce image noise.
4. Converts the crop to grayscale.
5. Applies a binary threshold.
6. Finds contours and filters them by area.
7. Draws the detected contours and writes the coin count on the image.
8. Displays the result and saves it as `output.jpg`.

## Requirements

- Python 3.8 or newer
- OpenCV
- NumPy
- Matplotlib
- A desktop environment capable of displaying an OpenCV window

## Installation

Create and activate a virtual environment (recommended):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

## Usage

Keep `coin.jpg` in the same directory as `coin_detector.py`, then run:

```powershell
python coin_detector.py
```

The program opens a window named `Coin`. Press any key while that window is
focused to close it. The annotated image is also saved as `output.jpg`.

## Project files

| File | Description |
| --- | --- |
| `coin_detector.py` | Coin detection script |
| `coin.jpg` | Sample input image |
| `output.jpg` | Example generated output |

## Adjusting detection

The current settings are tuned for the included image. For a different image,
you may need to adjust:

- `img[50:600, 320:840]` to select the relevant image region
- The threshold value `227` in `cv2.threshold`
- The minimum contour area `500`
- The Gaussian blur kernel and sigma value

## Notes

`matplotlib` is included because it is imported by the current script, although
the script currently uses OpenCV for displaying and saving images.
