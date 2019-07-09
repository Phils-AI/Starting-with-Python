import random
import time
from matplotlib import pyplot as plt
from matplotlib import animation


def swap(number, i, j):
    if i != j:
        number[i], number[j] = number[j], number[i]

def bubblesort(number):
    if len(number) == 1:
        return

    isNumberSwapped = True
    for i in range(len(number) - 1):
        if not isNumberSwapped:
            break
        isNumberSwapped = False
        for j in range(len(number) - 1 - i):
            if number[j] > number[j + 1]:
                swap(number, j, j + 1)
                isNumberSwapped = True
            yield number

def insertionsort(number):
    for i in range(1, len(number)):
        j = i
        while j > 0 and number[j] < number[j - 1]:
            swap(number, j, j - 1)
            j -= 1
            yield number

def mergesort(number, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(number, start, mid)
    yield from mergesort(number, mid + 1, end)
    yield from merge(number, start, mid, end)
    yield number

def merge(number, start, mid, end):
    merged = []
    leftNumber = start
    rightNumber = mid + 1

    while leftNumber <= mid and rightNumber <= end:
        if number[leftNumber] < number[rightNumber]:
            merged.append(number[leftNumber])
            leftNumber += 1
        else:
            merged.append(number[rightNumber])
            rightNumber += 1

    while leftNumber <= mid:
        merged.append(number[leftNumber])
        leftNumber += 1

    while rightNumber <= end:
        merged.append(number[rightNumber])
        rightNumber += 1

    for i, sorted_val in enumerate(merged):
        number[start + i] = sorted_val
        yield number

def quicksort(number, start, end):
    if start >= end:
        return

    pivot = number[end]
    pivotNumber = start

    for i in range(start, end):
        if number[i] < pivot:
            swap(number, i, pivotNumber)
            pivotNumber += 1
        yield number
    swap(number, end, pivotNumber)
    yield number

    yield from quicksort(number, start, pivotNumber - 1)
    yield from quicksort(number, pivotNumber + 1, end)

def selectionsort(number):
    if len(number) == 1:
        return

    for i in range(len(number)):
        minVal = number[i]
        minNumber = i
        for j in range(i, len(number)):
            if number[j] < minVal:
                minVal = number[j]
                minNumber = j
            yield number
        swap(number, i, minNumber)
        yield number

if __name__ == "__main__":
    inputNumbers = int(input("\nHow much numbers you want to sort:\n"))
    method_msg = "\nEnter the method of interest:\n(1) BubbleSort\n(2) InsertionSort\n(3) MergeSort \
        \n(4) QuickSort\n(5) SelectionSort\n"
    method = input(method_msg)

    number = [x + 1 for x in range(inputNumbers)]
    random.seed(time.time())
    random.shuffle(number)

    if method == "1":
        title = "Bubble sort"
        generator = bubblesort(number)
    elif method == "2":
        title = "Insertion sort"
        generator = insertionsort(number)
    elif method == "3":
        title = "Merge sort"
        generator = mergesort(number, 0, inputNumbers - 1)
    elif method == "4":
        title = "Quicksort"
        generator = quicksort(number, 0, inputNumbers - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(number)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(number)), number, align="edge")

    ax.set_xlim(0, inputNumbers)
    ax.set_ylim(0, int(1.07 * inputNumbers))

    text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

    iteration = [0]
    def update_fig(number, rects, iteration):
        for rect, val in zip(rects, number):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("Number of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()
