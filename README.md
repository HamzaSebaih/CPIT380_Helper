

**CPIT380 HELPER Python + Jes4py**

This Python code utilizes the `jes4py` library to perform various image manipulation techniques on pictures you select.

**Features:**

- **Mirroring:**
  - `reflect_horizontal_1()`: Creates a horizontally mirrored image (flips left to right).
  - `reflect_vertical_1()`: Creates a vertically mirrored image (flips top to bottom).
  - `reflect_horizontal_2()`: Creates a horizontally mirrored image with the original image on the right side.
  - `reflect_vertical_2()`: Creates a vertically mirrored image with the original image on the bottom side.
- **Diagonal Reflection:**
  - `reflect_diagonal_v1_d1()`: Creates a diagonal reflection, reflecting pixels from the upper left to the lower right (limited to square images).
  - `reflect_diagonal_v1_d2()`: Creates a diagonal reflection, reflecting pixels from the upper right to the lower left (limited to square images).
  - `reflect_diagonal_v2_d1()`: Creates a diagonal reflection, reflecting pixels from the bottom left to the top right (limited to square images).
  - `reflect_diagonal_v2_d2()`: Creates a diagonal reflection, reflecting pixels from the bottom right to the top left (limited to square images).
- **Rotation:**
  - `rotate_left()`: Rotates the image 90 degrees counter-clockwise.
  - `rotate_right()`: Rotates the image 90 degrees clockwise.
- **Resizing:**
  - `smaller(src, num)`: Shrinks the image by a factor of `num`.
  - `bigger(src, num)`: Enlarges the image by a factor of `num`.
  - `smallerPer(src, per)`: Shrinks the image by a percentage specified by `per` (0 to 100).
  - `biggerPer(src, per)`: Enlarges the image by a percentage specified by `per` (0 to 100).

**Requirements:**

- Python 3
- `jes4py` library (installation: `pip install jes4py`)



**Notes:**
- Some functions (diagonal reflection and resizing) have limitations regarding square image requirements.


