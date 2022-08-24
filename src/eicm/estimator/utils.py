def normalize_matrix(matrix):
    """
    Normalize matrix to [0, 1] by dividing it by its maximum value.

    :param matrix:
    :return: normalized matrix
    """
    return matrix / matrix.max()
