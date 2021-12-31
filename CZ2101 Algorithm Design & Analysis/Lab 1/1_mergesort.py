from random import randint
import timeit
import csv

def createlist(n):
    """ Generates a list of size n with random integers. """
    list = []
    for i in range(n):
        list.append(randint(1, n * n))
    return list


def mergeSort(list):

    length = len(list)

    if length <= 1:
        return

    # list midpoint
    mid = length // 2
    
    # recursive call
    left = list[:mid]
    right = list[mid:]
    mergeSort(left)
    mergeSort(right)

    # merge
    l = r = i = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            list[i] = left[l]
            l += 1
        else:
            list[i] = right[r]
            r += 1
        i += 1            

    # append remaining items
    while l < len(left):
        list[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        list[i] = right[r]
        r += 1
        i += 1


def runSort(min_n, max_n, ave_over, S):
    """ Runs merge sort on arrays of length n=min_n to n=max_n.
        Gets average runtime for each n from ave_over number of different arrays.
    """

    file = open('runtimes.csv', 'a+')
    writer = csv.writer(file)

    for n in range(min_n, max_n+1):
        ave_runtime = 0

        for j in range(ave_over):
            print("\nSorting ", n, "-", j+1, " in progress...\n", sep="")
            list = createlist(n)

            start = timeit.default_timer()
            mergeSort(list, S)
            stop = timeit.default_timer()

            cpu_runtime = stop - start
            ave_runtime += cpu_runtime
        
        ave_runtime /= ave_over
        writer.writerow([n, ave_runtime])

    file.close()


def runSortOnce():
    n = int(input("Input n: "))
    list = createlist(n)
    print("Original List:\n", list, sep="")

    print("\nSorting in progress...\n", sep="")
    mergeSort(list)
    print("\nSorted List:\n", list, sep="")


# run
if __name__ == '__main__':
    print("Merge Sort")

    with open('mergesort_runtimes.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'ave_runtime'])

    min_n = 1
    max_n = 5000
    ave_over = 5

    runSort(min_n, max_n, ave_over)
    