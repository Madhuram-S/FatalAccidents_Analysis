# Dependencies
from math import sqrt

from statistics import mean


def variance(arr):
    _mean = mean(arr)
    normalized = [x - _mean for x in arr]
    squares = [x ** 2 for x in normalized]
    return sum(squares) / len(arr)


def standard_deviation(arr):
    return sqrt(variance(arr))


def z_score(arr, index):
    return (arr[index] - mean(arr)) / standard_deviation(arr)


def z_scores(arr):
    return [z_score(arr, ind) for ind in range(0, len(arr))]


def zipped_z_scores(arr):
    return list(zip(arr, z_scores(arr)))


sample = [-2, -1, 0, 1, 2]

# print(variance(sample))
# print(standard_deviation(sample))
# print(zipped_z_scores(sample))
