import numpy as np

def max_pooling(matrix, pool_size=2, stride=2):
    matrix = np.array(matrix)

    h, w = matrix.shape

    output_h = (h - pool_size) // stride + 1
    output_w = (w - pool_size) // stride + 1

    output = np.zeros((output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            start_i = i * stride
            start_j = j * stride

            region = matrix[
                start_i:start_i + pool_size,
                start_j:start_j + pool_size
            ]

            output[i, j] = np.max(region)

    return output


matrix = [
    [1, 3, 2, 4],
    [5, 6, 7, 8],
    [9, 2, 3, 1],
    [4, 5, 6, 7]
]

result = max_pooling(matrix)

print("Max pooling result:")
print(result)
