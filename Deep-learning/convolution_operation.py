import numpy as np

def convolution2d(image, kernel):
    image = np.array(image)
    kernel = np.array(kernel)

    h, w = image.shape
    kh, kw = kernel.shape

    output_h = h - kh + 1
    output_w = w - kw + 1

    output = np.zeros((output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            region = image[i:i + kh, j:j + kw]
            output[i, j] = np.sum(region * kernel)

    return output


image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

kernel = [
    [1, 0],
    [0, -1]
]

result = convolution2d(image, kernel)

print("Convolution result:")
print(result)
