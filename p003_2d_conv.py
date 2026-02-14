'''
p003. Convolution (2D, Single Channel)

Question:
Implement 2D convolution (no padding, stride = 1). Not corss-correlation. Determine shape of the output.

def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    """
    image: HxW
    kernel: kHxkW
    output: ?    
    """

Constraints:
- Kernel size ≤ 7x7


Traps:
- Bounds errors

Follow-ups:
- Add padding and stride
- Extend to multi-channel input
- FFT-based convolution?
'''

def conv2d(img: list[list[float]], ker: list[list[float]]) -> list[list[float]]:
    """
    image: HxW
    kernel: kHxkW
    output: ?    
    """
    h = len(img)
    if h==0:
      return []
    w = len(img[0])
    if w==0:
      return []
    
    kh = len(ker)
    if kh==0:
      return []
    kw = len(ker[0])
    if kw==0:
      return []

    for i in range(h):
      if len(img[i]) != w:
        raise ValueError(f"image row {i} has cols {len(img[i])}, not compatible with expected {w}")

    for i in range(kh):
      if len(ker[i]) != kw:
        raise ValueError(f"kernel row {i} has cols {len(ker[i])}, not compatible with expected {kw}")

    # important concept: in true convolution, image dimensions must be greater than kernel dimensions.
    # true convolution is not symmetric if image and kernel are swapped. conv2d(img,ker) != conv2d(ker,img).
    if kw>w or kh>h:
      raise ValueError(f"kernel width {kw} <=? image width {w}, kernel height {kh} <=? image height {h}")
    
    h_op, w_op = h-kh+1, w-kw+1
    op = [[0.0 for _ in range(w_op)] for _ in range(h_op)]    

    for i in range(h_op):
      for j in range(w_op):
        total = 0.0
        for k in range(kh):
          for p in range(kw):
            total += img[i+k][j+p] * ker[kh-1-k][kw-1-p] # flip the kernel. important.
        op[i][j] = total
    
    return op















































# Output shape: (H-kH+1) x (W-kW+1)