from random import randint
import timeit
import csv

def createlist(n):
    """ Generates a list of size n with random integers. """
    list = []
    for i in range(n):
        list.append(randint(1, n * n))
    return list


def insertionSort(list, n):
    
    for i in range(1, n):
        # get last element of list subset (elements 1 to i inclusive)
        j = i
        ele = list[j]

        # in list subset, move all elements > ele backwards by 1 place
        while j > 0 and ele < list[j-1]:
            list[j] = list[j-1]
            j -= 1

        # store ele behind the 1st encounter it is larger than
        list[j] = ele


def hybridSort(list, S):

    length = len(list)

    # base case: S-element list - use insertion sort
    if length <= S:
        insertionSort(list, length)
        return

    # list midpoint
    mid = length // 2
    
    # recursive call
    left = list[:mid]
    right = list[mid:]
    hybridSort(left, S)
    hybridSort(right, S)

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
    """ Runs hybrid sort on arrays of length n=min_n to n=max_n.
        Gets average runtime for each n from ave_over number of different arrays.
        Uses the given value of S as the threshold to switch to insertion sort. """

    file = open('hybrid_runtimes.csv', 'a+')
    writer = csv.writer(file)

    for n in range(min_n, max_n+1):
        ave_runtime = 0

        for j in range(ave_over):
            print("\nSorting ", n, "-", j+1, " in progress...\n", sep="")
            list = createlist(n)

            start = timeit.default_timer()
            hybridSort(list, S)
            stop = timeit.default_timer()

            cpu_runtime = stop - start
            ave_runtime += cpu_runtime
        
        ave_runtime /= ave_over
        writer.writerow([n, ave_runtime])

    file.close()


def runSortOnce(S):
    n = int(input("Input n: "))
    list = createlist(n)
    print("Original List:\n", list, sep="")

    print("\nSorting in progress...\n", sep="")
    hybridSort(list, S)
    print("\nSorted List:\n", list, sep="")
    

# run
if __name__ == '__main__':
    print("Hybrid Sort")

    # with open('hybrid_runtimes.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['n', 'ave_runtime'])

    min_n = 10001
    max_n = 50000
    ave_over = 5
    S = 4

    runSort(min_n, max_n, ave_over, S)
    