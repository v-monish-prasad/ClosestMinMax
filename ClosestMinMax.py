def findClosestMinMaxSize(array, length):
    if not array:
        return "Empty Array."

    minimum, maximum = array[0], array[0]

    for i in range(length):
        if array[i] < minimum:
            minimum = array[i]
        elif array[i] > maximum:
            maximum = array[i]

    recentMinIndex = -1
    recentMaxIndex = -1
    size = length

    for i in range(length):
        if array[i] == maximum:
            recentMaxIndex = i
            if recentMinIndex >= 0:
                size = min(size, i - recentMinIndex + 1)
        elif array[i] == minimum:
            recentMinIndex = i
            if recentMaxIndex >= 0:
                size = min(size, i - recentMaxIndex + 1)

    return size


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    length = len(array)
    print(findClosestMinMaxSize(array, length))
