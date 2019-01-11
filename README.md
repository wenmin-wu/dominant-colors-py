# Dominant Colors
A python module for grabbing dominant colors from an image. It's much faster than colorthief.


## Installation

```bash
pip install dominantcolors
```

## Usage
```python
from dominantcolors import get_image_dominant_colors
dominant_colors = get_image_dominant_colors(image_path='/path/to/image_path',num_colors=3)
```

## Performance
```python
import time
from colorthief import ColorThief
from dominantcolors import get_image_dominant_colors

image_path = 'examples/image.jpg'
start_time = time.time()
color_thief = ColorThief(image_path)
dominant_colors = color_thief.get_palette(3, quality=1)
print('colorthief uses %s seconds.' % (time.time() - start_time))
#OUTPUT: colorthief uses 1.2148401737213135 seconds.

start_time = time.time()
dominant_colors = get_image_dominant_colors(image_path, 3)
print('dominantcolors uses %s seconds.' % (time.time() - start_time))
#OUPUT: dominantcolors uses 0.11298108100891113 seconds.
```

## Thanks
Thanks to AI Shack for its [original tutorial](http://aishack.in/tutorials/dominant-color/).

## Better
If you feel anything wrong, feedback or pull requests are welcome.
