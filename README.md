

**CPIT380 HELPER Python + Jes4py**

This Python code utilizes the `jes4py` library to perform various image and sound manipulation techniques.


**Requirements:**     
- Python 3.10.6+
- after installing VScode open a new terminal and install `jes4py`
- `jes4py` library (installation: `pip install jes4py` )
- `statistics` module (built-in)
- `numpy` library
- `matplotlib` library
- `typing` module (built-in)

**Notes:**
- Some functions (diagonal reflection and resizing) have limitations regarding square image requirements.
- All filtering functions convert the image to grayscale before applying the filter. 
- for real work I recommend using `openCV2`(for images and movies), `Librosa` (for sounds), and `nltk` (for texts)
- `playMovie()` and `playSound()` dosen't work in `jes4py` to use it you need to install `JES`


**Image Features:**

- **Mirroring:**
  - `reflect_horizontal_1(source)`: Creates a horizontally mirrored image (flips left to right).
  - `reflect_vertical_1(source)`: Creates a vertically mirrored image (flips top to bottom).
  - `reflect_horizontal_2(source)`: Creates a horizontally mirrored image with the original image on the right side.
  - `reflect_vertical_2(source)`: Creates a vertically mirrored image with the original image on the bottom side.

- **Diagonal Reflection:**
  - `reflect_diagonal_v1_d1(source)`: Creates a diagonal reflection, reflecting pixels from the upper left to the lower right (limited to square images).
  - `reflect_diagonal_v1_d2(source)`: Creates a diagonal reflection, reflecting pixels from the upper right to the lower left (limited to square images).
  - `reflect_diagonal_v2_d1(source)`: Creates a diagonal reflection, reflecting pixels from the bottom left to the top right (limited to square images).
  - `reflect_diagonal_v2_d2(source)`: Creates a diagonal reflection, reflecting pixels from the bottom right to the top left (limited to square images).

- **Rotation:**
  - `rotate_left()`: Rotates the image 90 degrees counter-clockwise.
  - `rotate_right()`: Rotates the image 90 degrees clockwise.

- **Resizing:**
  - `smaller(src, num)`: Shrinks the image by a factor of `num`.
  - `bigger(src, num)`: Enlarges the image by a factor of `num`.
  - `smallerPer(src, per)`: Shrinks the image by a percentage specified by `per` (0 to 100).
  - `biggerPer(src, per)`: Enlarges the image by a percentage specified by `per` (0 to 100).

- **Edge Detection**
  - `luminance(pixel)`: Calculates the average brightness (luminance) of a pixel.
  - `edgedetection_tlbr(source)`: Detects edges along the top-left to bottom-right diagonal. It compares the luminance of diagonally opposite pixels and sets the pixel to black if the difference exceeds a threshold (10 by default). A red text label is added to indicate the type of edge detected.
  - `edge_detection_lr(source)`: Detects edges along the left-to-right direction. Similar to `edgedetection_tlbr`, it compares luminance and sets pixels to black if the difference is significant. A red text label is added.
  - `edge_detection_tb(source)`: Detects edges along the top-to-bottom direction. It follows the same logic as the previous functions, comparing luminance and setting pixels to black for significant differences. A red text label is added.

- **Background/Foreground Replacement:**
    - `background(image, oldBackground, newBackground, threshold)`: Replaces the background in an image based on a threshold value. It iterates through each pixel, compares its color to the background color in a separate image (`oldBackground`), and replaces pixels with similar colors (within the threshold) using the corresponding pixel from a new background image (`newBackground`).
    - `foreground(image, oldBackground, newBackground, threshold)`: Isolates the foreground in an image based on a threshold value. This function works similarly to `background`, but it replaces pixels with colors dissimilar (outside the threshold) to the background in the `newBackground` image.

- **Histogram Visualization:**
  - `HistogramVisualize(Picture: Picture)`: This method generates histograms to visualize the distribution of colors across each channel (red, green, blue) within a given image.
  
- **Histogram Equalization:**
  - `HistogramEqualize(Picture: Picture) -> Picture`: This function enhances image contrast by performing histogram equalization. It creates a new image with a more balanced distribution of color intensities.
  - `HistogramEquilizeNewMapping(ValuesList: List) -> List` (Internal Helper): This helper function calculates a new mapping for histogram equalization based on the provided color value list (not intended for external use).

- **Grayscale Conversion:**
  - `MakeGrayScaledImage(Picture: Picture) -> Picture:`
    - This function converts a color image into a grayscale version.
    - It iterates through each pixel in the image and calculates the average of the red, green, and blue values. This average value is then set as the red, green, and blue components of the grayscale pixel.
    - This function is useful for preparing images for further processing, such as applying filters that work best on grayscale images.

- **Image Copying:**
  - `CreateImageCopy(Picture: Picture) -> Picture:`
    - This function creates a new image object that is a copy of the original image.
    - This can be useful for creating a working version of an image to avoid modifying the original. The copy can be filtered or manipulated without affecting the source image.

- **Image Filtering:**
  - `SimpleAverageFilter(Picture: Picture) -> Picture:`
    - This function applies a simple averaging filter to a grayscale image.
    - It uses a 3x3 window to iterate over neighboring pixels and calculates the average value. This average value is then set as the new value for the center pixel.
    - This filter has a smoothing effect, blurring sharp edges and reducing noise in the image.
  - `MedianFilter(Picture: Picture) -> Picture:`
    - This function applies a median filter to a grayscale image.
    - It uses a 3x3 window to iterate over neighboring pixels and stores their values in a list. The median value from this list is then set as the new value for the center pixel.
    - This filter is more effective than the simple average filter at preserving edges while reducing noise.
  - `MinFilter(Picture: Picture) -> Picture:`
    - This function applies a minimum value filter to a grayscale image.
    - It uses a 3x3 window to iterate over neighboring pixels and finds the minimum value. This minimum value is then set as the new value for the center pixel.
    - This filter effectively removes highlights and emphasizes dark areas in the image.
  - `MaxFilter(Picture: Picture) -> Picture:`
    - This function applies a maximum value filter to a grayscale image.
    - It uses a 3x3 window to iterate over neighboring pixels and finds the maximum value. This maximum value is then set as the new value for the center pixel.
    - This filter effectively removes shadows and emphasizes bright areas in the image.
  - `LaplacianFilter(Picture: Picture) -> Picture:`
    - This function applies a Laplacian filter to a grayscale image.
    - The Laplacian filter is used for edge detection. It uses a specific 3x3 kernel to calculate the difference between the center pixel and its neighbors. This difference is then used to determine the edge strength and is reflected in the output image.
  - `SobelFilter(Picture: Picture) -> Picture:`
    - This function applies a Sobel filter to a grayscale image.
    - The Sobel filter is another edge detection filter. It uses two 3x3 kernels to calculate the image gradient in the horizontal and vertical directions. The gradient magnitude is then used to determine the edge strength, similar to the Laplacian filter.
  - `PrewittFilter(Picture: Picture) -> Picture:`
    - This function applies a Prewitt filter to a grayscale image.
    - The Prewitt filter is similar to the Sobel filter and is used for edge detection. It also uses two 3x3 kernels to calculate the image gradient in the horizontal and vertical directions.
  - `RobertsFilter(Picture: Picture) -> Picture:`
    - This function applies a Roberts filter to a grayscale image.
    - The Roberts filter is a simpler edge detection filter that uses a 2x2 kernel. It calculates the difference between diagonally opposite pixels to detect edges.
  - `SimpleAverageFilterGeneralized(Picture: Picture, WindowSize) -> Picture:`
    - This function applies a generalized simple averaging filter to a grayscale image.
    - It allows you to specify the window size (e.g., 5x5, 7x7) for the filter kernel. The filter iterates through a window of neighboring pixels and calculates the average value, which is then set as the new value for the center pixel.
    - This function provides more flexibility compared to the basic `SimpleAverageFilter` by allowing you to adjust the filter strength based on the window size.




**Sound Features:**

- **Sound Copy and Manipulation:**
  - `CreateAudioCopyWithSpace(SourceAudio: Sound) -> Sound`: Creates a copy of a Sound Object and adds some space after it, according to its sampling rate.
  - `copy(SourceAudio: Sound, Target: Sound, StartIndex)`: Copies the source audio into the target audio, starting at the given index.
  - `increaseVolume(Sound)`: Increases the volume of a Sound object.
  - `SpliceSounds(Sound1: Sound, Sound2: Sound, increaseVolumeSet: bool = False) -> Sound`: Splice two Sound objects into one with an optional volume increase.
  - `CreateAudioCopy(SourceAudio: Sound) -> Sound`: Creates a simple copy of a Sound Object.
- **Sound Filtering:**
  - `simpleAvrgFilter(sound_for_filter, filterSize)`: Applies a simple averaging filter to a sound object.
  - `minFilter(sound_for_filter, filterSize)`: Applies a minimum value filter to a sound object.
  - `maxFilter(sound_for_filter, filterSize)`: Applies a maximum value filter to a sound object.
  - `weightedFilter_3x3(sound_for_filter, index1, index2, index3)`: Applies a weighted filter to a sound object using a 3x3 kernel with specified weights. 



