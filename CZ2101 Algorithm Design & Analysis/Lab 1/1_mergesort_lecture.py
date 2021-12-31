from random import randint
import timeit
import csv

comp = 0

def createlist(n):
    """ Generates a list of size n with random integers. """
    list = []
    for i in range(n):
        list.append(randint(1, n * n))
    return list


def createBESTlist(n):
    """ Generates a list of size n with random integers. """
    list = []
    for i in range(n):
        list.append(i)
    return list


def createWORSTlist(n):
    """ Generates a list of size n with random integers. """
    list = []
    for i in range(n):
        list.append(n-i)
    return list


def mergeSort(arr):

    length = len(arr)
    mid = length // 2

    # base case: nothing to sort if array has < 1 element
    if length <= 1:
        return

    # recursive call
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)

    # merge
    merge(arr, left, right)    


def merge(arr, left, right):
    global comp
    i = 0

    while len(left) > 0 and len(right) > 0:
        comp += 1
        if left[0] < right[0]:
            arr[i] = left.pop(0)
        elif right[0] < left[0]:
            arr[i] = right.pop(0)
        else:
            arr[i] = left.pop(0)
            i += 1
            arr[i] = right.pop(0)
        i += 1
    
    # append remaining items
    while len(left) > 0:
        arr[i] = left.pop(0)
        i += 1

    while len(right) > 0:
        arr[i] = right.pop(0)
        i += 1
        

def runSort(min_n, max_n, ave_over):
    """ Runs merge sort on arrays of length n=min_n to n=max_n.
        Gets average runtime for each n from ave_over number of different arrays.
    """

    global comp

    file = open('runtimes_merge_worst.csv', 'a+')
    writer = csv.writer(file)

    for n in range(min_n, max_n+1):
        ave_runtime = 0
        comp = 0

        for j in range(ave_over):
            # print("\nSorting ", n, "-", j+1, " in progress...\n", sep="")
            list = createWORSTlist(n)

            start = timeit.default_timer()
            mergeSort(list)
            stop = timeit.default_timer()

            cpu_runtime = stop - start
            ave_runtime += cpu_runtime
        
        ave_runtime /= ave_over
        comp /= ave_over
        writer.writerow([n, ave_runtime, comp])

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
    print("runtimes_merge_worst")

    # with open('runtimes_merge_best.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['n', 'ave_runtime', 'key_comparisons'])

    min_n = 7894
    max_n = 10000
    ave_over = 1

    runSort(min_n, max_n, ave_over)
    # runSortOnce()
    