

**CPIT380 HELPER Python + Jes4py**

This Python code utilizes the `jes4py` library to perform various image and sound manipulation techniques.


**Requirements:**     
- Python 3.10.6+
- after installing VScode open a new terminal and install `jes4py`
- `jes4py` library (installation: `pip install jes4py` )


**Notes:**
- Some functions (diagonal reflection and resizing) have limitations regarding square image requirements.


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


